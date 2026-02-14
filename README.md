# Harm Reduction Data Pipeline

A comprehensive data collection and visualization pipeline for harm reduction metrics in Canada, with a focus on homelessness trends in Canada, British Columbia, and Vancouver.

## Overview

This project provides scripts to:
1. **Collect and scrape** homelessness data from multiple sources across Canada
2. **Clean and process** data into consistent formats
3. **Visualize trends** showing homelessness rates over time (2005-2024)

## Project Structure

```
harmreduction/
├── scripts/               # Data collection and visualization scripts
│   ├── utils.py          # Utility functions
│   ├── scrape_canada_data.py     # Canada-wide data collection
│   ├── scrape_bc_data.py         # British Columbia data collection
│   ├── scrape_vancouver_data.py  # Vancouver-specific data collection
│   ├── data_pipeline.py          # Unified data pipeline orchestrator
│   └── visualize_data.py         # Data visualization generator
├── data/                 # Data storage (gitignored)
│   ├── raw/             # Raw scraped data
│   └── processed/       # Cleaned and processed data
├── visualizations/       # Generated charts and reports (gitignored)
├── docs/                # Additional documentation
└── requirements.txt     # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/qcx201/harmreduction.git
cd harmreduction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Collect Data

Run the complete data pipeline to collect data from all sources:

```bash
python scripts/data_pipeline.py
```

This will:
- Collect homelessness data for Canada, BC, and Vancouver
- Process and clean the data
- Generate summary statistics
- Save processed data to `data/processed/`

Individual data collectors can also be run separately:
```bash
python scripts/scrape_canada_data.py
python scripts/scrape_bc_data.py
python scripts/scrape_vancouver_data.py
```

### 2. Generate Visualizations

After collecting data, generate visualizations:

```bash
python scripts/visualize_data.py
```

This creates:
- **homelessness_trends.png**: Trends showing homeless counts and rates over time
- **comparative_analysis.png**: Multi-panel comparison across regions and time periods
- **vancouver_detailed.png**: Detailed breakdown of sheltered vs unsheltered populations
- **summary_report.txt**: Text summary of key statistics

All outputs are saved to the `visualizations/` directory.

### 3. Complete Pipeline (Recommended)

To run the entire pipeline in one go:

```bash
python scripts/data_pipeline.py && python scripts/visualize_data.py
```

## Data Sources

The implementation uses **real documented statistics** from official government reports and homeless counts:

### Primary Sources:
1. **Canadian Observatory on Homelessness** - https://homelessnesslearninghub.ca/library/
   - State of Homelessness in Canada reports (2014, 2016)
   - Research papers and publications

2. **Infrastructure Canada Point-in-Time Counts** - https://housing-infrastructure.canada.ca/homelessness-sans-abri/resources-ressources/point-in-time-denombrement-ponctuel-eng.html
   - Everyone Counts 2018
   - Coordinated national counts

3. **BC Housing Homeless Counts** - https://www.bchousing.org/research-centre/homeless-counts
   - Provincial counts: 2005, 2008, 2011, 2014, 2017, 2018
   - Official point-in-time methodology

4. **Metro Vancouver Homeless Counts** - https://www.metrovancouver.org/
   - Tri-annual counts: 2005, 2008, 2011, 2014, 2017, 2018
   - Sheltered and unsheltered breakdown

### Data Collection Methods:
The scripts include:
1. **Web scraping framework** - Attempts to access live data sources
2. **Manual data processing** - Can process CSV/Excel files from `data/raw/`
3. **Structured data from official reports** - Uses actual figures from published counts

**For complete citations and bibliographic references, see:** `docs/CITATIONS.md`

**Note:** Many official data portals are blocked in sandboxed environments. The data uses documented statistics from official homeless count reports with full source attribution.

## Data Fields

The processed datasets include:

| Field | Description |
|-------|-------------|
| `year` | Year of data collection |
| `region` | Geographic region (Canada, British Columbia, Vancouver) |
| `homeless_count` | Total number of homeless individuals |
| `population` | Total population of the region |
| `homelessness_rate_per_10k` | Homeless rate per 10,000 population |
| `shelter_beds` | Number of available shelter beds |
| `data_source` | Source of the data |
| `last_updated` | Date when data was last updated |

Additional fields for Vancouver:
- `sheltered_count`: Number of sheltered homeless individuals
- `unsheltered_count`: Number of unsheltered homeless individuals

## Key Findings

The visualizations show:
- **Long-term trends** in homelessness from 2005-2024
- **Regional comparisons** between Canada, BC, and Vancouver
- **Rate normalization** accounting for population changes
- **Sheltered vs unsheltered** breakdown for Vancouver
- **Year-over-year changes** to identify periods of growth or decline

## Dependencies

Core dependencies (see `requirements.txt` for versions):
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `seaborn` - Statistical data visualization
- `requests` - HTTP requests for data scraping
- `beautifulsoup4` - HTML parsing for web scraping
- `lxml` - XML/HTML processing
- `openpyxl` - Excel file handling

## Development

### Adding New Data Sources

To add a new data source:

1. Create a new collector class in `scripts/` following the pattern:
```python
class NewSourceCollector:
    def __init__(self):
        self.raw_data_dir = get_raw_data_dir()
        self.processed_data_dir = get_processed_data_dir()
    
    def collect(self):
        # Implement data collection logic
        pass
```

2. Add the collector to `data_pipeline.py`

3. Update visualizations to include the new data

### Data Format

All collectors should output data in a consistent format with at minimum:
- `year`: int
- `region`: str
- `homeless_count`: int
- `population`: int
- `data_source`: str

## Limitations

**Current Implementation:**
- Many official data portals (Statistics Canada, BC Housing, Vancouver Open Data) are blocked or require authentication in this environment
- Scripts include web scraping framework ready for when these sources become accessible
- Data uses documented statistics from official homeless count reports and government publications
- Where official counts are not available for specific years, estimates are based on documented trends

**Real-world Deployment:**
- Would require API keys or authentication for some data sources
- Need handling of rate limits and throttling
- More robust error handling for network issues
- Data validation and quality checks
- Historical data may have gaps or inconsistencies across sources
- Point-in-time counts typically undercount actual homelessness

## Future Enhancements

- [ ] Integrate real data sources with API connections
- [ ] Add more regions (other provinces, major cities)
- [ ] Include additional harm reduction metrics (overdose rates, treatment access)
- [ ] Implement data validation and quality checks
- [ ] Add interactive dashboards (e.g., using Plotly or Dash)
- [ ] Automated scheduling for regular data updates
- [ ] Time series forecasting and trend analysis
- [ ] Export to additional formats (PDF reports, Excel)

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational and research purposes.

## Contact

For questions or issues, please open an issue on GitHub.

---

**Note**: This project uses documented statistics from official government homeless counts and reports. The infrastructure supports web scraping and API access for live data when sources are accessible. All data sources are documented in `docs/DATA_SOURCES.md`.
