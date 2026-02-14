"""
Visualization script for homelessness data.

Creates comprehensive visualizations showing homelessness trends
in Canada, BC, and Vancouver.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import get_processed_data_dir, get_visualizations_dir

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

class HomelessnessVisualizer:
    """Creates visualizations for homelessness data."""
    
    def __init__(self):
        self.processed_data_dir = get_processed_data_dir()
        self.viz_dir = get_visualizations_dir()
        
    def load_data(self):
        """Load the combined homelessness data."""
        filepath = self.processed_data_dir / 'combined_homelessness_data.csv'
        if not filepath.exists():
            raise FileNotFoundError(
                f"Data file not found: {filepath}\n"
                "Please run data_pipeline.py first to collect data."
            )
        
        df = pd.read_csv(filepath)
        logger.info(f"Loaded {len(df)} records from {filepath}")
        return df
    
    def plot_homelessness_trends(self, df):
        """
        Plot homelessness count trends for Canada, BC, and Vancouver.
        """
        logger.info("Creating homelessness trends visualization...")
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Plot 1: Absolute counts
        for region in ['Canada', 'British Columbia', 'Vancouver']:
            region_data = df[df['region'] == region]
            ax1.plot(region_data['year'], region_data['homeless_count'], 
                    marker='o', linewidth=2, label=region, markersize=4)
        
        ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Homeless Count', fontsize=12, fontweight='bold')
        ax1.set_title('Homelessness Trends in Canada, BC, and Vancouver (2005-2024)', 
                     fontsize=14, fontweight='bold', pad=20)
        ax1.legend(fontsize=11, loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Add data source note
        ax1.text(0.02, 0.02, 'Note: Sample data for demonstration purposes', 
                transform=ax1.transAxes, fontsize=8, style='italic', 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
        
        # Plot 2: Rates per 10,000 population
        for region in ['Canada', 'British Columbia', 'Vancouver']:
            region_data = df[df['region'] == region]
            ax2.plot(region_data['year'], region_data['homelessness_rate_per_10k'], 
                    marker='s', linewidth=2, label=region, markersize=4)
        
        ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Homeless Rate per 10,000 Population', fontsize=12, fontweight='bold')
        ax2.set_title('Homelessness Rates per 10,000 Population (2005-2024)', 
                     fontsize=14, fontweight='bold', pad=20)
        ax2.legend(fontsize=11, loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save figure
        filepath = self.viz_dir / 'homelessness_trends.png'
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        logger.info(f"Saved visualization to {filepath}")
        
        return fig
    
    def plot_comparative_analysis(self, df):
        """
        Create comparative analysis charts.
        """
        logger.info("Creating comparative analysis visualization...")
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Plot 1: Year-over-year change in homeless count
        ax1 = axes[0, 0]
        for region in ['Canada', 'British Columbia', 'Vancouver']:
            region_data = df[df['region'] == region].sort_values('year')
            yoy_change = region_data['homeless_count'].pct_change() * 100
            ax1.plot(region_data['year'].iloc[1:], yoy_change.iloc[1:], 
                    marker='o', label=region, linewidth=2)
        
        ax1.set_xlabel('Year', fontweight='bold')
        ax1.set_ylabel('Year-over-Year Change (%)', fontweight='bold')
        ax1.set_title('Year-over-Year Change in Homeless Count', fontweight='bold')
        ax1.legend()
        ax1.axhline(y=0, color='black', linestyle='--', alpha=0.3)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Latest year comparison (2024)
        ax2 = axes[0, 1]
        latest_data = df[df['year'] == df['year'].max()]
        regions = latest_data['region'].values
        counts = latest_data['homeless_count'].values
        bars = ax2.bar(regions, counts, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        ax2.set_ylabel('Homeless Count', fontweight='bold')
        ax2.set_title(f'Homeless Count Comparison ({df["year"].max()})', fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height):,}',
                    ha='center', va='bottom', fontweight='bold')
        
        # Plot 3: Homelessness rate comparison
        ax3 = axes[1, 0]
        rates = latest_data['homelessness_rate_per_10k'].values
        bars = ax3.bar(regions, rates, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        ax3.set_ylabel('Rate per 10,000 Population', fontweight='bold')
        ax3.set_title(f'Homelessness Rate Comparison ({df["year"].max()})', fontweight='bold')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontweight='bold')
        
        # Plot 4: Trend over time periods
        ax4 = axes[1, 1]
        
        # Calculate averages for different periods
        periods = {
            '2005-2009': (2005, 2009),
            '2010-2014': (2010, 2014),
            '2015-2019': (2015, 2019),
            '2020-2024': (2020, 2024)
        }
        
        for region in ['Canada', 'British Columbia', 'Vancouver']:
            period_avgs = []
            for period_name, (start, end) in periods.items():
                period_data = df[(df['region'] == region) & 
                               (df['year'] >= start) & 
                               (df['year'] <= end)]
                avg = period_data['homelessness_rate_per_10k'].mean()
                period_avgs.append(avg)
            
            ax4.plot(list(periods.keys()), period_avgs, 
                    marker='o', label=region, linewidth=2)
        
        ax4.set_xlabel('Period', fontweight='bold')
        ax4.set_ylabel('Average Rate per 10,000', fontweight='bold')
        ax4.set_title('Average Homelessness Rate by Period', fontweight='bold')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)
        
        plt.tight_layout()
        
        # Save figure
        filepath = self.viz_dir / 'comparative_analysis.png'
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        logger.info(f"Saved visualization to {filepath}")
        
        return fig
    
    def plot_vancouver_detailed(self, df):
        """
        Create detailed Vancouver-specific visualizations.
        """
        logger.info("Creating Vancouver detailed visualization...")
        
        vancouver_data = df[df['region'] == 'Vancouver'].copy()
        
        if 'sheltered_count' not in vancouver_data.columns:
            logger.warning("Sheltered/unsheltered data not available for detailed plot")
            return None
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Plot 1: Sheltered vs Unsheltered
        ax1.plot(vancouver_data['year'], vancouver_data['sheltered_count'], 
                marker='o', linewidth=2, label='Sheltered', color='#2ca02c')
        ax1.plot(vancouver_data['year'], vancouver_data['unsheltered_count'], 
                marker='s', linewidth=2, label='Unsheltered', color='#d62728')
        ax1.set_xlabel('Year', fontweight='bold')
        ax1.set_ylabel('Count', fontweight='bold')
        ax1.set_title('Vancouver: Sheltered vs Unsheltered Homeless Population', 
                     fontweight='bold', fontsize=13)
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Stacked area chart
        ax2.fill_between(vancouver_data['year'], 0, 
                        vancouver_data['sheltered_count'], 
                        label='Sheltered', alpha=0.7, color='#2ca02c')
        ax2.fill_between(vancouver_data['year'], 
                        vancouver_data['sheltered_count'],
                        vancouver_data['homeless_count'], 
                        label='Unsheltered', alpha=0.7, color='#d62728')
        ax2.set_xlabel('Year', fontweight='bold')
        ax2.set_ylabel('Count', fontweight='bold')
        ax2.set_title('Vancouver: Homeless Population Composition', 
                     fontweight='bold', fontsize=13)
        ax2.legend(fontsize=11)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save figure
        filepath = self.viz_dir / 'vancouver_detailed.png'
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        logger.info(f"Saved visualization to {filepath}")
        
        return fig
    
    def generate_summary_report(self, df):
        """Generate a text summary report."""
        logger.info("Generating summary report...")
        
        report_lines = []
        report_lines.append("="*70)
        report_lines.append("HOMELESSNESS DATA SUMMARY REPORT")
        report_lines.append("="*70)
        report_lines.append("")
        
        for region in ['Canada', 'British Columbia', 'Vancouver']:
            region_data = df[df['region'] == region].sort_values('year')
            
            report_lines.append(f"\n{region.upper()}")
            report_lines.append("-"*70)
            report_lines.append(f"Years covered: {region_data['year'].min()} - {region_data['year'].max()}")
            report_lines.append(f"Total records: {len(region_data)}")
            report_lines.append("")
            
            # Latest year stats
            latest = region_data[region_data['year'] == region_data['year'].max()].iloc[0]
            report_lines.append(f"Latest year ({int(latest['year'])}):")
            report_lines.append(f"  - Homeless count: {int(latest['homeless_count']):,}")
            report_lines.append(f"  - Rate per 10,000: {latest['homelessness_rate_per_10k']:.2f}")
            report_lines.append("")
            
            # Historical stats
            report_lines.append("Historical summary:")
            report_lines.append(f"  - Average homeless count: {region_data['homeless_count'].mean():.0f}")
            report_lines.append(f"  - Maximum: {int(region_data['homeless_count'].max()):,} (year {int(region_data.loc[region_data['homeless_count'].idxmax(), 'year'])})")
            report_lines.append(f"  - Minimum: {int(region_data['homeless_count'].min()):,} (year {int(region_data.loc[region_data['homeless_count'].idxmin(), 'year'])})")
            
            # Trend
            first_year_count = region_data.iloc[0]['homeless_count']
            last_year_count = region_data.iloc[-1]['homeless_count']
            pct_change = ((last_year_count - first_year_count) / first_year_count) * 100
            report_lines.append(f"  - Overall change: {pct_change:+.1f}%")
            report_lines.append("")
        
        report_lines.append("="*70)
        report_lines.append("Data sources: Sample/simulated data for demonstration")
        report_lines.append(f"Report generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("="*70)
        
        report_text = "\n".join(report_lines)
        
        # Save report
        filepath = self.viz_dir / 'summary_report.txt'
        with open(filepath, 'w') as f:
            f.write(report_text)
        logger.info(f"Saved summary report to {filepath}")
        
        # Also print to console
        print("\n" + report_text)
        
        return report_text
    
    def visualize_all(self):
        """Generate all visualizations."""
        logger.info("="*60)
        logger.info("Starting visualization generation")
        logger.info("="*60)
        
        try:
            # Load data
            df = self.load_data()
            
            # Generate visualizations
            self.plot_homelessness_trends(df)
            self.plot_comparative_analysis(df)
            self.plot_vancouver_detailed(df)
            
            # Generate summary report
            self.generate_summary_report(df)
            
            logger.info("\n" + "="*60)
            logger.info("All visualizations generated successfully!")
            logger.info(f"Visualizations saved to: {self.viz_dir}")
            logger.info("="*60)
            
            print(f"\n\nVisualization files created in: {self.viz_dir}")
            print("- homelessness_trends.png")
            print("- comparative_analysis.png")
            print("- vancouver_detailed.png")
            print("- summary_report.txt")
            
        except Exception as e:
            logger.error(f"Visualization failed: {str(e)}", exc_info=True)
            raise

if __name__ == '__main__':
    visualizer = HomelessnessVisualizer()
    visualizer.visualize_all()
