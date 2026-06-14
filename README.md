<!-- GSD -->

# Sales Analytics Dashboard

Interactive Streamlit dashboard for daily sales monitoring. Displays KPI cards, interactive Plotly charts (sales trend with rolling averages, day-of-week breakdown, monthly comparison), and raw data export with CSV download. Uses synthetic data generated on load.

**Live demo:** https://harsh-data-analytics-portfolio.streamlit.app

---

## Features

- **KPI cards** — Total revenue, daily average, peak day (with date), last 7 days average
- **Sales trend chart** — Interactive line chart with 7-day and 30-day rolling average overlays
- **Sales by day of week** — Bar chart sorted Monday–Sunday, highlighting weekend performance
- **Monthly revenue** — Bar chart comparing total sales per month
- **Raw data expander** — View first 50 rows, download full dataset as CSV

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| App framework | Streamlit 1.31.0 |
| Data manipulation | Pandas 2.2.0 |
| Numeric computation | NumPy 1.26.3 |
| Interactive charts | Plotly 5.18.0 |
| Static charts (dev) | Matplotlib 3.8.3, Seaborn 0.13.2 |
| Deployment | Streamlit Cloud |
| Version control | GitHub |

---

## Quick Start

```bash
git clone https://github.com/harshvardhankulkarni/sales-dashboard.git
cd sales-dashboard
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
streamlit run dashboard.py
```

Your browser opens at `http://localhost:8501`.

---

## Live Demo

- **Streamlit Cloud:** https://harsh-data-analytics-portfolio.streamlit.app
- **GitHub Pages:** https://harshvardhankulkarni.github.io/sales-dashboard/

---

## Project Structure

```
sales-dashboard/
  dashboard.py          Streamlit application (single-file app)
  sales_dashboard.ipynb Jupyter notebook version
  index.html            GitHub Pages landing page
  requirements.txt      Pinned Python dependencies
  README.md             This file
  docs/
    ARCHITECTURE.md     Architecture and design decisions
    GETTING-STARTED.md  Setup and first run guide
    DEVELOPMENT.md      Development guide and contribution
    TESTING.md          Testing and validation
    CONFIGURATION.md    Configuration reference
```

---

## Demo Note

This is a portfolio / demo project. All data is synthetic — generated at runtime via NumPy with a reproducible seed (`np.random.seed(42)`). Not intended for production use.

---

## License

MIT
