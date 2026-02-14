# Quick Start Guide

Get started with the Harm Reduction Data Pipeline in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection (optional, for web scraping)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/qcx201/harmreduction.git
cd harmreduction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- pandas (data manipulation)
- matplotlib & seaborn (visualization)
- requests & beautifulsoup4 (web scraping)
- openpyxl (Excel file support)

## Running the Pipeline

### Option 1: Run Everything (Recommended)

Collect data and generate all visualizations:

```bash
python scripts/data_pipeline.py && python scripts/visualize_data.py
```

### Option 2: Step by Step

**Step 1: Collect Data**

```bash
python scripts/data_pipeline.py
```

This will:
- Collect homelessness data for Canada, BC, and Vancouver
- Save processed data to `data/processed/`
- Generate summary statistics

**Step 2: Generate Visualizations**

```bash
python scripts/visualize_data.py
```

This creates:
- `visualizations/homelessness_trends.png` - Time series charts
- `visualizations/comparative_analysis.png` - Multi-panel comparison
- `visualizations/vancouver_detailed.png` - Sheltered vs unsheltered breakdown
- `visualizations/summary_report.txt` - Statistical summary

### Option 3: Run Individual Collectors

```bash
# Canada data only
python scripts/scrape_canada_data.py

# BC data only
python scripts/scrape_bc_data.py

# Vancouver data only
python scripts/scrape_vancouver_data.py
```

## Viewing Results

### Data Files

Processed data is saved in `data/processed/`:

```bash
# View combined data
cat data/processed/combined_homelessness_data.csv

# View summary statistics
cat data/processed/summary_statistics.csv
```

### Visualizations

Open the PNG files in `visualizations/` directory:

```bash
# On Linux/Mac
open visualizations/homelessness_trends.png

# Or use your image viewer
```

### Summary Report

Read the text summary:

```bash
cat visualizations/summary_report.txt
```

## Understanding the Data

### Data Sources

All data comes from official government reports:
- **Canada**: Canadian Observatory on Homelessness, Infrastructure Canada
- **BC**: BC Housing homeless count reports (2005-2018)
- **Vancouver**: Metro Vancouver homeless counts (2005-2018)

**See `docs/CITATIONS.md` for complete bibliographic references.**

### Data Quality Ratings

Each data point is tagged with quality rating:
- `official_count`: From actual point-in-time counts
- `research`: From peer-reviewed research
- `estimate`: Interpolated from trends

### Time Coverage

- **Years**: 2005-2023 (18 years)
- **Regions**: Canada, British Columbia, Vancouver
- **Records**: 30 total (10 per region)

## Adding Your Own Data

### Manual Data Files

Place CSV or Excel files in `data/raw/`:

```bash
# Example: Download a Statistics Canada table
# Save as: data/raw/statcan_housing_2023.csv

# Run pipeline - it will automatically detect and process new files
python scripts/data_pipeline.py
```

### File Naming Conventions

For automatic detection, use descriptive names:
- `*canada*.csv` - Canadian data
- `*bc*.csv` or `*british*columbia*.csv` - BC data
- `*vancouver*.csv` - Vancouver data

## Common Issues

### Issue: Missing data directories

```bash
mkdir -p data/raw data/processed visualizations
```

### Issue: Import errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Issue: Visualization display

If charts don't display, they are saved as PNG files:
```bash
ls -lh visualizations/*.png
```

## Next Steps

### Explore the Data

Use pandas to analyze the data:

```python
import pandas as pd

# Load combined data
df = pd.read_csv('data/processed/combined_homelessness_data.csv')

# Explore
print(df.info())
print(df.describe())
print(df.groupby('region')['homeless_count'].mean())
```

### Customize Visualizations

Edit `scripts/visualize_data.py` to:
- Change colors and styles
- Add new chart types
- Filter specific time periods
- Compare different metrics

### Add More Regions

Follow the pattern in existing scripts:
1. Create `scripts/scrape_<region>_data.py`
2. Add to `scripts/data_pipeline.py`
3. Update visualizations

## Getting Help

- **Documentation**: See `README.md` for complete documentation
- **Data Sources**: See `docs/DATA_SOURCES.md` for source details
- **Citations**: See `docs/CITATIONS.md` for bibliographic references
- **Changelog**: See `CHANGELOG.md` for version history

## Example Output

After running the pipeline, you should see:

```
Summary Statistics:
          region years_covered  total_records  avg_homeless_count  max_homeless_count
British Columbia     2005-2023             10              3444.2                4200
          Canada     2005-2023             10             33150.0               38000
       Vancouver     2005-2023             10              1938.9                2236

Total records collected: 30
Regions covered: 3
Years covered: 2005 - 2023

Visualization files created in: /path/to/visualizations
- homelessness_trends.png
- comparative_analysis.png
- vancouver_detailed.png
- summary_report.txt
```

## Tips

1. **Run regularly**: Official counts are published every 2-3 years
2. **Check for updates**: Visit source websites for new data releases
3. **Validate estimates**: Years marked as "estimate" should be verified
4. **Cite properly**: Always cite original sources when using this data

## Quick Reference

| Command | Purpose |
|---------|---------|
| `python scripts/data_pipeline.py` | Collect all data |
| `python scripts/visualize_data.py` | Generate all visualizations |
| `cat visualizations/summary_report.txt` | View summary |
| `ls data/processed/` | List processed data files |
| `head data/processed/combined_homelessness_data.csv` | Preview data |

---

**Ready to go!** Run the pipeline and explore Canadian homelessness trends.

For questions, see the main README or open an issue on GitHub.
