# PashuDrishti - Project Summary

## Overview
PashuDrishti is a cattle breed classification system using deep learning. The project has been structured with a clean, production-ready architecture suitable for SIH (Smart India Hackathon) and professional deployment.

---

## Project Structure

```
PashuDrishti/
├── data/
│   ├── raw/              # Raw images (cattle/buffalo)
│   ├── interim/          # Cleaned images
│   └── processed/        # Train/Val/Test splits
│       ├── train/
│       ├── val/
│       └── test/
├── src/
│   ├── data/            # Data processing modules
│   ├── models/          # Model training & evaluation
│   ├── api/             # FastAPI REST API
│   └── utils/           # Configuration utilities
├── notebooks/           # Jupyter notebooks for EDA & experiments
├── config/              # Configuration files
├── models/              # Trained model files (gitignored)
└── requirements.txt     # Python dependencies
```

---

## Key Components

### 1. Data Processing Pipeline
- **`build_dataset.py`**: Splits dataset into train/validation/test (70/15/15)
- **`clean_images.py`**: Removes duplicates, validates images, filters small images
- **`preprocess.py`**: Image resizing, normalization, and data augmentation

### 2. Model Training
- **`train_cnn.py`**: CNN model with 4 convolutional layers + dense layers
  - Automatic model checkpointing
  - Early stopping to prevent overfitting
  - Learning rate reduction on plateau
- **`baselines_ml.py`**: Traditional ML models (SVM, MLP, Random Forest, KNN) for comparison
- **`evaluate.py`**: Comprehensive evaluation with confusion matrix, F1-scores, and visualizations

### 3. API Deployment
- **`main_fastapi.py`**: REST API server with `/predict` endpoint
  - Accepts image uploads
  - Returns top 3 predictions with confidence scores
  - Production-ready error handling

### 4. Configuration Management
- **`config.yaml`**: Centralized configuration for all settings
- **`config.py`**: Utility functions to load and access configuration

### 5. Analysis Notebooks
- **`01_eda_dataset.ipynb`**: Exploratory data analysis
- **`02_cnn_experiments.ipynb`**: CNN architecture experiments

---

## Features

✅ **Clean Architecture**: Modular, maintainable code structure  
✅ **Production-Ready**: Error handling, logging, best practices  
✅ **Data Pipeline**: Automated cleaning, splitting, preprocessing  
✅ **Multiple Models**: CNN + baseline ML models for comparison  
✅ **REST API**: FastAPI server for real-time predictions  
✅ **Evaluation Tools**: Comprehensive metrics and visualizations  
✅ **Git Protection**: `.gitignore` prevents pushing large data/models  

---

## Workflow

1. **Data Cleaning**: Run `clean_images.py` to remove duplicates/invalid images
2. **Dataset Splitting**: Run `build_dataset.py` to create train/val/test splits
3. **Model Training**: Run `train_cnn.py` to train the CNN model
4. **Evaluation**: Use `evaluate.py` to analyze model performance
5. **Deployment**: Run `main_fastapi.py` to serve predictions via API

---

## Technology Stack

- **Deep Learning**: TensorFlow/Keras
- **ML Libraries**: scikit-learn
- **API Framework**: FastAPI
- **Data Processing**: NumPy, Pandas, PIL
- **Visualization**: Matplotlib, Seaborn
- **Configuration**: PyYAML

---

## Next Steps

1. Install dependencies: `pip install -r requirements.txt`
2. Configure paths in `config/config.yaml`
3. Run EDA notebook to understand dataset
4. Clean and split the dataset
5. Train the CNN model
6. Evaluate and compare with baseline models
7. Deploy API for predictions

---

## Team Notes

- All code follows production best practices
- Comprehensive error handling and validation
- Well-documented with docstrings
- Ready for SIH submission
- Scalable architecture for future enhancements

---

**Status**: ✅ Project structure complete, ready for development and training

