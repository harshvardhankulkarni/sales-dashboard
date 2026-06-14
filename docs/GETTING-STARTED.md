<!-- GSD -->

# Getting Started

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

```bash
# Clone the repository
git clone https://github.com/harshvardhankulkarni/sales-dashboard.git
cd sales-dashboard

# Create and activate a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

## Running Locally

```bash
streamlit run dashboard.py
```

Your browser opens at `http://localhost:8501`. The dashboard loads immediately with synthetic sales data for 180 days.

## Live Demo

Access the deployed version anytime:

https://harsh-data-analytics-portfolio.streamlit.app

No installation required. Dashboard loads in-browser.

## Expected Dashboard View

When you launch the dashboard, you should see:

1. **Title** — "Business Performance Dashboard" with subtitle "Daily sales monitoring across 180 days."
2. **4 KPI cards** — Total Revenue (~Rs.12,100,000), Daily Average (~Rs.67,000), Peak Day (~Rs.150,000+ on a specific date), Last 7 Days Avg
3. **Sales Trend chart** — Interactive line chart with daily sales (blue), 7-day rolling average (red), and 30-day rolling average (green)
4. **Sales by Day of Week** — Bar chart showing Saturday as the highest-performing day
5. **Monthly Revenue** — Bar chart showing increasing trend from Jan to Jun
6. **"View Raw Data" expander** — Expand to see the first 50 rows and download the full CSV
