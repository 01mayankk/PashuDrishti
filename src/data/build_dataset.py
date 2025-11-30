"""
Split dataset into train/validation/test sets.
"""
import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split
import yaml


def load_config():
    """Load configuration from config.yaml"""
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)


def split_dataset(source_dir, output_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    """
    Split dataset into train/val/test sets.
    
    Args:
        source_dir: Path to source images directory
        output_dir: Path to output directory
        train_ratio: Proportion of data for training
        val_ratio: Proportion of data for validation
        test_ratio: Proportion of data for testing
    """
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6, "Ratios must sum to 1.0"
    
    # Get all image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
    all_files = []
    for ext in image_extensions:
        all_files.extend(Path(source_dir).rglob(f'*{ext}'))
    
    # Split into train/val/test
    train_files, temp_files = train_test_split(
        all_files, test_size=(1 - train_ratio), random_state=42
    )
    val_files, test_files = train_test_split(
        temp_files, test_size=(test_ratio / (val_ratio + test_ratio)), random_state=42
    )
    
    # Copy files to respective directories
    for split_name, files in [('train', train_files), ('val', val_files), ('test', test_files)]:
        split_dir = Path(output_dir) / split_name
        split_dir.mkdir(parents=True, exist_ok=True)
        
        for file_path in files:
            # Preserve directory structure (breed name)
            relative_path = file_path.relative_to(source_dir)
            dest_path = split_dir / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, dest_path)
        
        print(f"{split_name}: {len(files)} files")


if __name__ == "__main__":
    config = load_config()
    source_dir = config['data']['source_dir']
    output_dir = config['data']['processed_dir']
    
    split_dataset(
        source_dir,
        output_dir,
        train_ratio=config['data']['train_ratio'],
        val_ratio=config['data']['val_ratio'],
        test_ratio=config['data']['test_ratio']
    )

