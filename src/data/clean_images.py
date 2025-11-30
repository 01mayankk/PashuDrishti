"""
Clean images: remove duplicates, noise, and invalid files.
"""
import os
import hashlib
from pathlib import Path
from PIL import Image
import numpy as np


def calculate_image_hash(image_path):
    """Calculate MD5 hash of image file."""
    with open(image_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def is_valid_image(image_path):
    """
    Check if image is valid and can be opened.
    
    Returns:
        bool: True if image is valid, False otherwise
    """
    try:
        img = Image.open(image_path)
        img.verify()
        return True
    except Exception:
        return False


def remove_duplicates(directory):
    """
    Remove duplicate images based on file hash.
    
    Args:
        directory: Path to directory containing images
    """
    seen_hashes = {}
    duplicates = []
    
    for image_path in Path(directory).rglob('*.{jpg,jpeg,png,JPG,JPEG,PNG}'):
        if not is_valid_image(image_path):
            print(f"Invalid image: {image_path}")
            image_path.unlink()
            continue
        
        file_hash = calculate_image_hash(image_path)
        
        if file_hash in seen_hashes:
            duplicates.append(image_path)
            print(f"Duplicate found: {image_path} (same as {seen_hashes[file_hash]})")
        else:
            seen_hashes[file_hash] = image_path
    
    # Remove duplicates
    for dup in duplicates:
        dup.unlink()
    
    print(f"Removed {len(duplicates)} duplicate images")


def filter_small_images(directory, min_size=(32, 32)):
    """
    Remove images smaller than minimum size.
    
    Args:
        directory: Path to directory containing images
        min_size: Minimum (width, height) in pixels
    """
    removed = 0
    for image_path in Path(directory).rglob('*.{jpg,jpeg,png,JPG,JPEG,PNG}'):
        try:
            with Image.open(image_path) as img:
                if img.size[0] < min_size[0] or img.size[1] < min_size[1]:
                    print(f"Removing small image: {image_path} (size: {img.size})")
                    image_path.unlink()
                    removed += 1
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            image_path.unlink()
            removed += 1
    
    print(f"Removed {removed} images smaller than {min_size}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean images in dataset')
    parser.add_argument('--directory', type=str, required=True, help='Directory to clean')
    parser.add_argument('--remove-duplicates', action='store_true', help='Remove duplicate images')
    parser.add_argument('--filter-small', action='store_true', help='Filter small images')
    parser.add_argument('--min-size', type=int, nargs=2, default=[32, 32], help='Minimum image size')
    
    args = parser.parse_args()
    
    if args.remove_duplicates:
        remove_duplicates(args.directory)
    
    if args.filter_small:
        filter_small_images(args.directory, tuple(args.min_size))

