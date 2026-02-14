"""
Unified data pipeline for harm reduction data collection.

This script orchestrates the collection, cleaning, and processing of 
homelessness data from multiple sources.
"""
import pandas as pd
import logging
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from scrape_canada_data import CanadaHomelessnessDataCollector
from scrape_bc_data import BCHomelessnessDataCollector
from scrape_vancouver_data import VancouverHomelessnessDataCollector
from utils import get_processed_data_dir

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataPipeline:
    """Orchestrates data collection from all sources."""
    
    def __init__(self):
        self.processed_data_dir = get_processed_data_dir()
        
    def run_all_collectors(self):
        """Run all data collectors."""
        logger.info("="*60)
        logger.info("Starting comprehensive data collection pipeline")
        logger.info("="*60)
        
        # Collect Canada data
        logger.info("\n--- Collecting Canada data ---")
        canada_collector = CanadaHomelessnessDataCollector()
        canada_df = canada_collector.collect()
        
        # Collect BC data
        logger.info("\n--- Collecting BC data ---")
        bc_collector = BCHomelessnessDataCollector()
        bc_df = bc_collector.collect()
        
        # Collect Vancouver data
        logger.info("\n--- Collecting Vancouver data ---")
        vancouver_collector = VancouverHomelessnessDataCollector()
        vancouver_df = vancouver_collector.collect()
        
        return canada_df, bc_df, vancouver_df
    
    def combine_datasets(self, canada_df, bc_df, vancouver_df):
        """Combine all datasets into a unified format."""
        logger.info("\n--- Combining datasets ---")
        
        # Ensure consistent columns
        all_dfs = []
        
        for df, name in [(canada_df, 'Canada'), 
                         (bc_df, 'British Columbia'), 
                         (vancouver_df, 'Vancouver')]:
            df_copy = df.copy()
            df_copy['region_level'] = name
            all_dfs.append(df_copy)
        
        combined_df = pd.concat(all_dfs, ignore_index=True)
        combined_df = combined_df.sort_values(['year', 'region'])
        
        # Save combined dataset
        filepath = self.processed_data_dir / 'combined_homelessness_data.csv'
        combined_df.to_csv(filepath, index=False)
        logger.info(f"Saved combined dataset to {filepath}")
        
        return combined_df
    
    def generate_summary_statistics(self, combined_df):
        """Generate summary statistics."""
        logger.info("\n--- Generating summary statistics ---")
        
        summary_stats = []
        
        for region in combined_df['region'].unique():
            region_data = combined_df[combined_df['region'] == region]
            
            stats = {
                'region': region,
                'years_covered': f"{region_data['year'].min()}-{region_data['year'].max()}",
                'total_records': len(region_data),
                'avg_homeless_count': region_data['homeless_count'].mean(),
                'max_homeless_count': region_data['homeless_count'].max(),
                'min_homeless_count': region_data['homeless_count'].min(),
                'avg_rate_per_10k': region_data['homelessness_rate_per_10k'].mean(),
            }
            summary_stats.append(stats)
        
        summary_df = pd.DataFrame(summary_stats)
        
        # Save summary
        filepath = self.processed_data_dir / 'summary_statistics.csv'
        summary_df.to_csv(filepath, index=False)
        logger.info(f"Saved summary statistics to {filepath}")
        
        return summary_df
    
    def run(self):
        """Run the complete pipeline."""
        try:
            # Collect all data
            canada_df, bc_df, vancouver_df = self.run_all_collectors()
            
            # Combine datasets
            combined_df = self.combine_datasets(canada_df, bc_df, vancouver_df)
            
            # Generate summary statistics
            summary_df = self.generate_summary_statistics(combined_df)
            
            logger.info("\n" + "="*60)
            logger.info("Pipeline completed successfully!")
            logger.info("="*60)
            
            print("\n\nSummary Statistics:")
            print(summary_df.to_string(index=False))
            
            print(f"\n\nTotal records collected: {len(combined_df)}")
            print(f"Regions covered: {combined_df['region'].nunique()}")
            print(f"Years covered: {combined_df['year'].min()} - {combined_df['year'].max()}")
            
            return combined_df, summary_df
            
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}", exc_info=True)
            raise

if __name__ == '__main__':
    pipeline = DataPipeline()
    pipeline.run()
