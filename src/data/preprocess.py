"""
Image preprocessing functions: resize, normalize, augmentation.
"""
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras


def resize_image(image_path, target_size=(224, 224)):
    """
    Resize image to target size.
    
    Args:
        image_path: Path to image file
        target_size: Target (width, height)
    
    Returns:
        PIL Image object
    """
    img = Image.open(image_path)
    img = img.resize(target_size, Image.Resampling.LANCZOS)
    return img


def normalize_image(img_array):
    """
    Normalize image array to [0, 1] range.
    
    Args:
        img_array: numpy array of image
    
    Returns:
        Normalized numpy array
    """
    return img_array.astype(np.float32) / 255.0


def create_augmentation_pipeline():
    """
    Create data augmentation pipeline using TensorFlow/Keras.
    
    Returns:
        keras.Sequential augmentation model
    """
    return keras.Sequential([
        keras.layers.RandomRotation(0.1),
        keras.layers.RandomZoom(0.1),
        keras.layers.RandomFlip(mode='horizontal'),
        keras.layers.RandomBrightness(0.1),
        keras.layers.RandomContrast(0.1),
    ])


def preprocess_for_training(image_path, target_size=(224, 224), augment=False):
    """
    Preprocess image for training.
    
    Args:
        image_path: Path to image file
        target_size: Target image size
        augment: Whether to apply augmentation
    
    Returns:
        Preprocessed image array
    """
    # Load and resize
    img = resize_image(image_path, target_size)
    img_array = np.array(img)
    
    # Normalize
    img_array = normalize_image(img_array)
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    # Apply augmentation if requested
    if augment:
        aug_pipeline = create_augmentation_pipeline()
        img_array = aug_pipeline(img_array, training=True)
    
    return img_array


def create_data_generator(directory, target_size=(224, 224), batch_size=32, 
                          augment=False, shuffle=True):
    """
    Create data generator for training.
    
    Args:
        directory: Path to image directory
        target_size: Target image size
        batch_size: Batch size
        augment: Whether to apply augmentation
        shuffle: Whether to shuffle data
    
    Returns:
        tf.keras.utils.Sequence or generator
    """
    datagen = keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        rotation_range=20 if augment else 0,
        width_shift_range=0.1 if augment else 0,
        height_shift_range=0.1 if augment else 0,
        horizontal_flip=augment,
        zoom_range=0.1 if augment else 0,
    )
    
    generator = datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=shuffle
    )
    
    return generator

