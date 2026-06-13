# Sales Analytics Dashboard - Demo Project

Interactive Streamlit dashboard for monitoring daily sales performance. KPI cards, trend charts, day-of-week breakdown, and monthly revenue comparison.

**Live Demo:** https://harsh-data-analytics-portfolio.streamlit.app

## Tech Stack

- Python 3.8+
- Streamlit 1.28+ - Web application framework
- Pandas 2.0+ - Data manipulation
- NumPy 1.24+ - Data generation
- Plotly 5.10+ - Interactive charts

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/sales-dashboard.git
cd sales-dashboard
pip install -r requirements.txt
```

### Running Locally

```bash
streamlit run dashboard.py
```

Your browser opens at `http://localhost:8501`.

### Deploy on Streamlit Cloud

1. Push this repo to GitHub.
2. Go to https://share.streamlit.io.
3. Sign in with GitHub.
4. Click "New app".
5. Select this repository, branch `main`, file `dashboard.py`.
6. Click "Deploy".

Your app is live at `https://[username]-[repo]-dashboard.streamlit.app`.

## Features

### KPI Cards
- Total revenue over 180 days.
- Average daily revenue.
- Peak day value with date.
- Last 7 days average.

### Sales Trend Chart
- Interactive Plotly line chart.
- 7-day rolling average overlay.
- 30-day rolling average overlay.
- Zoom, pan, and hover for details.

### Day of Week Analysis
- Bar chart of average sales by day.
- Sorted Monday through Sunday.
- Highlights best and worst days.

### Monthly Revenue
- Bar chart comparing all months.
- Shows growth and decline patterns.

### Raw Data Export
- Expandable data table.
- CSV download button.

## Project Structure

```
sales-dashboard/
  dashboard.py          Streamlit application
  requirements.txt      Python dependencies
  README.md             This file
  docs/
    architecture.md     Design and methodology
    runbook.md          Operations guide
```

## Configuration

### Data Source

The dashboard currently generates synthetic data. To use real data, replace the generation block (lines 14-26) with:

```python
import pandas as pd
df = pd.read_csv('your_sales_data.csv')
```

Required columns: `date`, `sales`.

### Visual Settings

- Page title: Change `st.set_page_config(page_title=...)`.
- Color scheme: Edit Plotly template or Streamlit theme in `.streamlit/config.toml`.

## Requirements

```
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.10.0
streamlit>=1.28.0
```

## License

MIT
