"""
Configuration utilities for reading config.yaml.
"""
import yaml
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str = None) -> Dict[str, Any]:
    """
    Load configuration from config.yaml.
    
    Args:
        config_path: Path to config file. If None, uses default location.
    
    Returns:
        Dictionary containing configuration
    """
    if config_path is None:
        # Default: config/config.yaml relative to project root
        project_root = Path(__file__).parent.parent.parent
        config_path = project_root / 'config' / 'config.yaml'
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    return config


def get_data_config(config: Dict[str, Any] = None) -> Dict[str, Any]:
    """Get data-related configuration."""
    if config is None:
        config = load_config()
    return config.get('data', {})


def get_model_config(config: Dict[str, Any] = None) -> Dict[str, Any]:
    """Get model-related configuration."""
    if config is None:
        config = load_config()
    return config.get('model', {})


def get_training_config(config: Dict[str, Any] = None) -> Dict[str, Any]:
    """Get training-related configuration."""
    if config is None:
        config = load_config()
    return config.get('training', {})


if __name__ == "__main__":
    # Test loading config
    config = load_config()
    print("Configuration loaded successfully!")
    print(f"Data config: {get_data_config(config)}")
    print(f"Model config: {get_model_config(config)}")

