# Sales Analytics Dashboard

Interactive Streamlit dashboard for monitoring daily sales performance. KPI cards, trend charts, day-of-week breakdown, and monthly revenue comparison.

## Live Demo

[https://harsh-data-analytics-portfolio.streamlit.app](https://harsh-data-analytics-portfolio.streamlit.app)

## Features

- **KPI Row**: Total revenue, daily average, peak day value, last 7 days average.
- **Sales Trend Chart**: Interactive Plotly line chart with 7-day and 30-day rolling averages.
- **Day of Week Analysis**: Bar chart showing average sales by day.
- **Monthly Revenue**: Bar chart comparing total revenue across months.
- **Raw Data Export**: Expandable data table with CSV download button.

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

Your browser opens automatically at `http://localhost:8501`.

## Deploy on Streamlit Cloud

1. Push this repo to GitHub.
2. Go to share.streamlit.io.
3. Sign in with GitHub.
4. Click "New app".
5. Select this repo, branch `main`, file `dashboard.py`.
6. Click "Deploy".

## Data

Dashboard uses synthetic daily sales data spanning 180 days. Generated with built-in trend, seasonality, and realistic noise.

## Tech Stack

Python, Streamlit, Pandas, NumPy, Plotly

## License

MIT
