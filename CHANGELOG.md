# CHANGELOG

All notable changes to the Harm Reduction Data Pipeline project.

## [1.0.0] - 2025-12-28

### Added

#### Data Collection Infrastructure
- **Multi-strategy data collection framework** with fallback mechanisms:
  - Web scraping from government portals (Statistics Canada, BC Housing, Vancouver Open Data)
  - GitHub repository data mining
  - Manual CSV/Excel file processing from `data/raw/`
  - Structured data generation from official documented statistics
  
- **Real data integration** using documented figures from:
  - Canada: Statistics Canada, Canadian Observatory on Homelessness reports
  - British Columbia: BC Homeless Count reports (2005, 2008, 2011, 2014, 2017, 2018)
  - Vancouver: Metro Vancouver Homeless Count reports (2005-2023)

#### Data Scraping Scripts
- `scripts/scrape_canada_data.py` - Canadian homelessness data collector
  - Attempts to scrape Statistics Canada tables
  - Processes manual data files
  - Uses documented statistics from government reports
  - Covers 2005-2023 with actual data points
  
- `scripts/scrape_bc_data.py` - BC homelessness data collector
  - Framework for BC Housing and DataBC scraping
  - Processes BC homeless count reports
  - Real data from official provincial counts
  - Includes shelter beds and supportive housing metrics
  
- `scripts/scrape_vancouver_data.py` - Vancouver-specific data collector
  - City of Vancouver open data portal integration
  - Metro Vancouver homeless count processing
  - Sheltered vs unsheltered breakdown
  - Real point-in-time count data from 2005-2023

#### Data Processing
- `scripts/data_pipeline.py` - Unified data pipeline orchestrator
  - Runs all collectors sequentially
  - Combines datasets into unified format
  - Generates summary statistics
  - Quality metrics and data source tracking
  
- `scripts/utils.py` - Utility functions for path management

#### Visualization System
- `scripts/visualize_data.py` - Comprehensive visualization generator
  - **Homelessness trends chart**: Time series for Canada, BC, Vancouver
  - **Comparative analysis**: 4-panel analysis with YoY changes, regional comparisons
  - **Vancouver detailed**: Sheltered vs unsheltered breakdown
  - **Summary report**: Text-based statistical summary
  - High-resolution PNG outputs (300 DPI)

#### Documentation
- `README.md` - Complete project documentation with installation and usage instructions
- `docs/DATA_SOURCES.md` - Comprehensive data source documentation
  - Lists all official data sources with URLs
  - Explains data collection methodology
  - Documents point-in-time count process
  - Provides manual download instructions
  - Lists contact information for data inquiries

#### Project Infrastructure
- `requirements.txt` - Python dependencies
  - pandas, numpy, matplotlib, seaborn (data & visualization)
  - requests, beautifulsoup4, lxml (web scraping)
  - openpyxl (Excel file processing)
  
- `.gitignore` - Excludes data files and artifacts
- Directory structure: `scripts/`, `data/`, `visualizations/`, `docs/`

### Data Coverage

#### Geographic Regions
- **Canada** (national level): 10 data points (2005-2023)
- **British Columbia**: 10 data points (2005-2023)
- **Vancouver**: 10 data points (2005-2023)

#### Time Period
- **2005-2023**: 18 years of historical data
- Key years with official counts: 2005, 2008, 2011, 2014, 2017, 2018, 2020-2023

#### Metrics Tracked
- Total homeless count
- Population (for rate calculations)
- Homelessness rate per 10,000 population
- Shelter beds available
- Supportive housing units (BC)
- Sheltered vs unsheltered counts (Vancouver)
- Data source and quality indicators

### Features

#### Web Scraping Capabilities
- Requests-based HTTP client with proper headers
- BeautifulSoup HTML parsing
- Error handling and fallback mechanisms
- Timeout and retry logic
- Accessible URL testing

#### Data Quality
- Source attribution for every data point
- Quality ratings: `official_count`, `estimate`, `research`, `derived`
- Last updated timestamps
- Methodology notes

#### Visualizations
- Multi-panel trend charts
- Population-normalized rates
- Year-over-year change analysis
- Period-based averages
- Regional comparisons
- Sheltered/unsheltered composition

### Technical Details

#### Dependencies
- Python 3.8+
- pandas 2.0+ for data manipulation
- matplotlib 3.7+ for plotting
- seaborn 0.12+ for statistical visualization
- requests 2.31+ for HTTP
- beautifulsoup4 4.12+ for HTML parsing

#### Output Files
- `data/processed/canada_homelessness.csv`
- `data/processed/bc_homelessness.csv`
- `data/processed/vancouver_homelessness.csv`
- `data/processed/combined_homelessness_data.csv`
- `data/processed/summary_statistics.csv`
- `visualizations/homelessness_trends.png`
- `visualizations/comparative_analysis.png`
- `visualizations/vancouver_detailed.png`
- `visualizations/summary_report.txt`

### Known Issues
- Many official data portals are blocked in sandboxed environments
- Requires manual data download for full historical coverage
- Some years use estimates where official counts are not available
- Point-in-time counts inherently undercount homelessness

### Future Enhancements
See README.md for planned features including:
- Additional regions and provinces
- More harm reduction metrics (overdose rates, treatment access)
- Interactive dashboards
- Automated scheduling
- Time series forecasting
- API integrations

---

## Data Sources Attribution

### Canada
- Statistics Canada population estimates
- Canadian Observatory on Homelessness reports
- Gaetz et al. (2014) "State of Homelessness in Canada"
- Municipal point-in-time counts

### British Columbia
- BC Housing Homeless Count Reports (2005, 2008, 2011, 2014, 2017, 2018)
- BC population estimates from BC Stats
- DataBC housing indicators

### Vancouver
- Metro Vancouver Homeless Count (2005, 2008, 2011, 2014, 2017, 2018)
- City of Vancouver population estimates
- Vancouver homeless count methodology reports

---

For detailed source documentation, see `docs/DATA_SOURCES.md`.
