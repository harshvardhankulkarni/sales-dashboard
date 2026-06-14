<!-- GSD -->

# Configuration

## Dependencies (requirements.txt)

Pinned versions for reproducible builds on Streamlit Cloud:

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | 2.2.0 | DataFrame operations, rolling averages, groupbys |
| numpy | 1.26.3 | Synthetic data generation, random noise, linear trends |
| matplotlib | 3.8.3 | (Not used directly in dashboard; available for dev work) |
| seaborn | 0.13.2 | (Not used directly in dashboard; available for dev work) |
| plotly | 5.18.0 | Interactive chart rendering |
| streamlit | 1.31.0 | Web application framework |

To update: edit `requirements.txt` and redeploy. Streamlit Cloud auto-detects and installs from this file.

## Inline Configuration (dashboard.py)

All configuration is inline in `dashboard.py`. There is no separate config file or `.streamlit/config.toml`.

### Data Generation Parameters (lines 16–24)

| Setting | Value | Line | Effect |
|---------|-------|------|--------|
| `np.random.seed` | 42 | 16 | Ensures reproducible data across runs |
| Number of days | 180 | 17 | Total rows in the dataset |
| Start date | 2024-01-01 | 17 | First date in the time series |
| `base_sales` | 50,000 | 18 | Baseline daily sales amount |
| Trend range | 0 to 20,000 | 19 | Linear upward drift over 180 days |
| Day-of-week multipliers | Mon 1.0, Tue 1.0, Wed 1.0, Thu 1.1, Fri 1.2, Sat 1.5, Sun 1.3 | 21 | Weekend uplift pattern |
| Noise std | 5,000 | 23 | Gaussian noise standard deviation |
| Sales floor | 10,000 | 24 | Minimum daily sales cap |

### Rolling Window Parameters (lines 33–34)

| Setting | Value | Description |
|---------|-------|-------------|
| `7_day_avg` | `.rolling(7).mean()` | 7-day rolling window for short-term trend |
| `30_day_avg` | `.rolling(30).mean()` | 30-day rolling window for long-term trend |

### Page Configuration (line 13)

```python
st.set_page_config(page_title='Sales Analytics Dashboard', layout='wide')
```

- `page_title` — Browser tab title
- `layout='wide'` — Uses full browser width instead of narrow centered layout

## Streamlit Cloud Deployment Settings

| Setting | Value |
|---------|-------|
| Entry point | `dashboard.py` |
| Python version | 3.8+ (auto-detected from runtime) |
| Dependency file | `requirements.txt` (auto-detected) |
| Deployment URL | https://harsh-data-analytics-portfolio.streamlit.app |
| Custom domain | Configured via Streamlit Cloud settings |
| Instance type | Free tier (single worker, shared resources) |

No `streamlit_app.py` wrapper is needed — Streamlit Cloud can launch `dashboard.py` directly.

## Changing Visual Settings

- **Page config** — Edit `st.set_page_config(...)` at line 13
- **Chart colors** — Modify Plotly template via `px.defaults.template` or pass `template=` to chart calls
- **Streamlit theme** — Create `.streamlit/config.toml` in the repo root to override Streamlit's default theme colors
