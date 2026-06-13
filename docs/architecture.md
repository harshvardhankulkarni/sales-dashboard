# Architecture: Sales Analytics Dashboard

## Context

Business owners need a real-time view of their sales performance. A static spreadsheet is not enough. A dashboard provides instant visibility into revenue trends, peak days, and monthly performance.

## Goals

- Display key sales metrics in a single screen.
- Provide interactive charts for trend analysis.
- Allow data export for further analysis.
- Deploy as a web app with zero infrastructure management.

## Design

### Component Architecture

```
Streamlit Application (dashboard.py)
  |
  +-- SyntheticDataGenerator
  |     Generates 180 days of sales data
  |     with trend + seasonality + noise
  |
  +-- KPICards (4 columns)
  |     Total Revenue | Daily Avg | Peak Day | Last 7 Days
  |
  +-- SalesTrendChart (Plotly line)
  |     Daily sales + 7-day avg + 30-day avg
  |
  +-- DayOfWeekChart (Plotly bar)
  |     Average sales by day
  |
  +-- MonthlyChart (Plotly bar)
  |     Total revenue per month
  |
  +-- RawDataExpander
        Data table + CSV download
```

### Data Flow

```
Startup
  |
  v
Generate/load DataFrame (180 rows)
  |
  v
Compute KPIs (total, avg, peak, recent)
  |
  v
Render Streamlit UI (4 columns, 2 rows)
  |
  v
Wait for user interaction (filter, zoom, download)
```

### Visualization Rendering

- All charts use Plotly for interactivity.
- Streamlit's `st.plotly_chart` handles the rendering.
- `use_container_width=True` makes charts responsive.

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Streamlit instead of Django/Flask | Fastest path to interactive dashboard. No frontend code needed. Built-in deployment. |
| Plotly instead of Matplotlib | Interactive charts (zoom, hover, pan). Better for exploratory data analysis. |
| Synthetic data | Self-contained. No database needed. Reproducible. |
| Single file app | Easy to understand and modify. No complex project structure. |
| CSV download | Gives users control over the underlying data. No API needed. |

## Trade-offs

- **Streamlit vs custom frontend**: Streamlit is fast to build but limited in customization. A React dashboard would be more flexible but take 10x longer.
- **Synthetic vs live data**: Live data needs a database connection, authentication, and refresh logic. The trade-off is simplicity vs realism.
- **Plotly vs Vega-Lite**: Plotly has better Python ergonomics. Vega-Lite would be more performant on large datasets.
- **Single file vs modular**: Single file is simple for demos. For production, split into lib/, components/, and config/.

## Integration Points

- **Data input**: Currently self-generates. For production, connect to PostgreSQL, BigQuery, or a REST API.
- **Export**: CSV download button provides raw data for Excel or BI tools.
- **Embedding**: The dashboard URL can be embedded in Notion, Confluence, or company portals via iframe.

## Performance

- Data: 180 rows, negligible load time.
- Charts: Plotly renders client-side. No server load after initial page load.
- Memory: < 100MB RAM.
- Scalability: Handles up to 10K rows before noticeable lag. Above that, aggregate before rendering.

## Dependencies

- streamlit, pandas, numpy, plotly
