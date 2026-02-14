"""
Utility functions for data scraping and processing.
"""
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def get_data_dir():
    """Get the data directory path."""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    data_dir.mkdir(exist_ok=True)
    return data_dir

def get_raw_data_dir():
    """Get the raw data directory path."""
    raw_dir = get_data_dir() / 'raw'
    raw_dir.mkdir(exist_ok=True)
    return raw_dir

def get_processed_data_dir():
    """Get the processed data directory path."""
    processed_dir = get_data_dir() / 'processed'
    processed_dir.mkdir(exist_ok=True)
    return processed_dir

def get_visualizations_dir():
    """Get the visualizations directory path."""
    base_dir = Path(__file__).parent.parent
    viz_dir = base_dir / 'visualizations'
    viz_dir.mkdir(exist_ok=True)
    return viz_dir
