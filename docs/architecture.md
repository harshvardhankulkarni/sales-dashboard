<!-- GSD -->

# Sales Dashboard — Architecture

## Context and Goals

Interactive Streamlit dashboard for sales analytics. Generates synthetic daily sales data and renders KPI cards, interactive charts, and a raw data table. Deployed on Streamlit Cloud as a live demo.

## Architecture

Single-page Streamlit application with inline data generation. No backend, no database, no API layer.

## Data Flow

```
Synthetic Data Generation (180 days)
  → Pandas DataFrame
  → KPI calculations (total, avg, peak, 7-day avg)
  → Plotly chart generation (trend, day-of-week, monthly)
  → Streamlit rendering
  → CSV export on demand
```

## Components

| Unit | File | Role |
|------|------|------|
| App entry | `dashboard.py` | Streamlit app: KPI cards, Plotly charts, data table, CSV export |
| Data layer | `dashboard.py` (inline) | Generates 180 days of synthetic sales data on app load |
| Visualization | `dashboard.py` (inline) | 3 Plotly charts: trend line, day-of-week bar, monthly comparison |
| Development | `sales_dashboard.ipynb` | Jupyter notebook for exploration |
| Dependencies | `requirements.txt` | Pinned Python packages for Streamlit Cloud |

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| Single-file app | Simple deployment, easy to understand |
| Inline data generation | No external data source needed for demo |
| Plotly for charts | Interactive charts with hover, zoom, built-in theming |
| Streamlit Cloud | Free hosting for live demo |
| 180-day window | Matches the sales-trend-analysis project for consistency |

## Trade-offs

- Synthetic data only — no real data connection
- No persistent storage — data regenerates on each load
- No authentication — publicly accessible
- Single-file limits modularity for larger applications
- No caching for repeated views

## File Organization

```
sales-dashboard/
├── dashboard.py
├── sales_dashboard.ipynb
├── requirements.txt
├── index.html
└── docs/
    ├── ARCHITECTURE.md
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```
