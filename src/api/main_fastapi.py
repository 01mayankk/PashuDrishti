"""
FastAPI endpoint for cattle breed prediction.
"""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import tensorflow as tf
from pathlib import Path
import sys
import io

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))
from data.preprocess import resize_image, normalize_image

app = FastAPI(title="PashuDrishti API", version="1.0.0")

# Load model (lazy loading)
model = None
class_names = None


def load_model(model_path='models/best_cnn.h5'):
    """Load the trained model."""
    global model, class_names
    if model is None:
        model_path = Path(__file__).parent.parent.parent / model_path
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found at {model_path}")
        model = tf.keras.models.load_model(model_path)
        
        # Load class names (you'll need to save this during training)
        # For now, placeholder
        class_names = [f"Class_{i}" for i in range(model.output_shape[1])]
    
    return model, class_names


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "PashuDrishti Cattle Breed Classification API"}


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Predict cattle breed from uploaded image.
    
    Args:
        file: Image file (jpg, png, etc.)
    
    Returns:
        JSON with predicted breed and confidence
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Preprocess
        image = resize_image(image, target_size=(224, 224))
        img_array = np.array(image)
        img_array = normalize_image(img_array)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Load model
        model, class_names = load_model()
        
        # Predict
        predictions = model.predict(img_array, verbose=0)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_idx])
        
        # Get class name
        predicted_class = class_names[predicted_class_idx]
        
        # Get top 3 predictions
        top_3_indices = np.argsort(predictions[0])[-3:][::-1]
        top_3_predictions = [
            {
                "breed": class_names[idx],
                "confidence": float(predictions[0][idx])
            }
            for idx in top_3_indices
        ]
        
        return JSONResponse({
            "predicted_breed": predicted_class,
            "confidence": confidence,
            "top_3_predictions": top_3_predictions
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

