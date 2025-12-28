# Data Sources for Canadian Homelessness Research

This document lists all data sources used and referenced in the harm reduction data pipeline.

## Official Data Sources

### 1. Statistics Canada

**Website:** https://www150.statcan.gc.ca/

**Relevant Tables:**
- Table 11-10-0135-01: Population estimates, quarterly
- Table 46-10-0043-01: Housing indicators by tenure including presence of mortgage payments and subsidized housing
- Census data on housing and demographic statistics

**Access Method:**
- Direct download from Statistics Canada website
- Some tables available via API
- May require manual download and placement in `data/raw/` directory

**Data Format:** CSV, Excel, JSON (varies by table)

---

### 2. BC Housing

**Website:** https://www.bchousing.org/research-centre

**Key Reports:**
- BC Homeless Count Reports (published every 2-3 years)
- Annual Service Plans and Reports
- Housing Data and Statistics

**Access Method:**
- PDF reports available for download
- Some data in Excel format
- Manual download required

**Data Coverage:** 2005-present (varies by report)

---

### 3. DataBC - BC Government Open Data Portal

**Website:** https://data.gov.bc.ca/

**Relevant Datasets:**
- Housing and homelessness datasets
- Population statistics
- Social services data

**Access Method:**
- API access available for some datasets
- Direct download (CSV, JSON, XML)
- Requires manual identification of relevant datasets

---

### 4. City of Vancouver Open Data Portal

**Website:** https://opendata.vancouver.ca/

**Relevant Datasets:**
- Homeless count data
- Shelter locations and capacity
- Social services locations
- Census data for Vancouver

**Access Method:**
- API available for most datasets
- Direct CSV/JSON downloads
- Open Data Catalogue with search functionality

---

### 5. Metro Vancouver Homeless Count

**Reports:** Published every 2-3 years

**Key Years:** 2005, 2008, 2011, 2014, 2017, 2018, 2020, 2021

**Content:**
- Total homeless count
- Sheltered vs unsheltered breakdown
- Demographic information
- Geographic distribution

**Access Method:**
- PDF reports from Metro Vancouver website
- Manual extraction required
- Data tables within reports can be exported

---

## Research and Academic Sources

### 6. Canadian Observatory on Homelessness

**Website:** https://www.homelesshub.ca/

**Resources:**
- "The State of Homelessness in Canada" reports
- Research papers and publications
- Best practices documentation

**Key Publications:**
- Gaetz, S., Dej, E., Richter, T., & Redman, M. (2016). The State of Homelessness in Canada 2016.
- Various research papers on homelessness trends

---

### 7. Employment and Social Development Canada (ESDC)

**Website:** https://www.canada.ca/en/employment-social-development.html

**Programs:**
- Reaching Home: Canada's Homelessness Strategy
- Homelessness Partnering Strategy data
- Funding allocations and outcomes

**Access Method:**
- Annual reports
- Open government data portal
- InfoBase and departmental results reports

---

### 8. Infrastructure Canada

**Website:** https://www.infrastructure.gc.ca/

**Relevant Data:**
- National Housing Strategy data
- Affordable housing investments
- Municipal infrastructure for housing

---

## International and Comparative Sources

### 9. OECD Affordable Housing Database

**Website:** https://www.oecd.org/housing/data/affordable-housing-database/

**Content:**
- International comparisons
- Housing affordability metrics
- Homelessness statistics for OECD countries

---

### 10. UN Habitat

**Website:** https://unhabitat.org/

**Content:**
- Global homelessness data
- Urban development statistics
- Housing policy research

---

## Data Collection Methodology

### Point-in-Time (PiT) Counts

Most Canadian homeless counts use the Point-in-Time methodology:
- Conducted on a single night or over 24 hours
- Count both sheltered and unsheltered individuals
- Volunteer-based street counts
- Surveys at shelters and service providers
- Typically conducted every 2-3 years

**Limitations:**
- Undercounts are common
- Weather-dependent for street counts
- May miss hidden homelessness
- Varies by methodology between jurisdictions

### Registry Week / By-Name Lists

Some jurisdictions use ongoing tracking:
- Real-time data on individuals experiencing homelessness
- Updated continuously
- More accurate than point-in-time counts
- Requires coordination across service providers

---

## Data Quality Notes

### Known Issues

1. **Inconsistent Definitions:** Different jurisdictions may define homelessness differently
2. **Undercount Bias:** PiT counts typically undercount actual homelessness
3. **Data Gaps:** Not all years have data; counts often done every 2-3 years
4. **Methodological Changes:** Changes in counting methodology over time affect comparability
5. **Hidden Homelessness:** Couch-surfing and provisional accommodation often not captured

### Data Quality Ratings

In our datasets, we use the following quality ratings:

- `official_count`: From official government PiT counts or registry data
- `estimate`: Interpolated or estimated based on trends
- `research`: From academic research or studies
- `derived`: Calculated from other official statistics

---

## Manual Data Download Instructions

Since many data sources are behind web portals or require authentication, follow these steps:

### For Statistics Canada Data:

1. Visit https://www150.statcan.gc.ca/
2. Search for relevant table numbers (e.g., 11-10-0135-01)
3. Select date range
4. Download as CSV
5. Save to `data/raw/` with descriptive filename

### For BC Homeless Count Reports:

1. Visit BC Housing research centre
2. Download homeless count reports (PDF)
3. Extract data tables manually or use PDF parsing
4. Save extracted data as CSV in `data/raw/`

### For Vancouver Open Data:

1. Visit https://opendata.vancouver.ca/
2. Search for "homeless" or relevant keywords
3. Download datasets (usually CSV)
4. Save to `data/raw/vancouver_*.csv`

---

## Automated Scraping Capabilities

Our scripts attempt to:

1. **Check for accessible data sources** - Test if URLs are reachable
2. **Parse HTML tables** - Extract data from web pages when possible
3. **API calls** - Use APIs when available and not rate-limited
4. **GitHub data** - Search for existing public datasets
5. **Fallback to structured data** - Use documented statistics when live scraping fails

---

## Contributing Data

If you have access to additional data sources:

1. Save raw data files to `data/raw/`
2. Use descriptive filenames (e.g., `statcan_population_2023.csv`)
3. Document the source in a README or comment
4. Run the data pipeline to integrate new data

---

## Data License and Usage

Most government data in Canada is available under the Open Government License:
- Free to use, modify, and share
- Attribution required
- https://open.canada.ca/en/open-government-licence-canada

Always verify specific license terms for each dataset.

---

## Update Frequency

| Source | Update Frequency |
|--------|------------------|
| Statistics Canada Population | Quarterly |
| BC Homeless Count | Every 2-3 years |
| Metro Vancouver Count | Every 2-3 years |
| City of Vancouver Data | Varies by dataset |
| Research Reports | Irregular |

---

## Contact Information for Data Inquiries

**Statistics Canada:**
- Email: infostats@statcan.gc.ca
- Phone: 1-800-263-1136

**BC Housing:**
- Email: research@bchousing.org

**City of Vancouver:**
- Email: opendata@vancouver.ca

**Canadian Observatory on Homelessness:**
- Website contact form available

---

Last Updated: 2025-12-28
