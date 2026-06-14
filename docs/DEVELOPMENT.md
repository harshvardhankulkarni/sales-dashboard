<!-- GSD -->

# Development

## Project Structure

```
sales-dashboard/
  dashboard.py          ──► Streamlit app. All code in one file.
  sales_dashboard.ipynb ──► Jupyter notebook (development reference).
  index.html            ──► GitHub Pages landing page.
  requirements.txt      ──► Pinned dependencies.
```

## How to Add New KPIs

KPIs are defined at lines 41–50 of `dashboard.py`. Each KPI is a `st.metric()` inside a `st.columns()` layout.

**Pattern:**

```python
col1, col2, col3, col4, col5 = st.columns(5)   # add a column

new_metric = df['sales'].<your_aggregation>()    # compute value
col5.metric('Label', f'Rs.{new_metric:,.0f}')   # render
```

**Example — add median daily sales:**

```python
col1, col2, col3, col4, col5 = st.columns(5)
...
median_daily = df['sales'].median()
col5.metric('Median Daily', f'Rs.{median_daily:,.0f}')
```

Steps:
1. Add a new `colN` variable and update `st.columns(N)` count
2. Compute the value from `df['sales']` (supported aggregations: `.min()`, `.median()`, `.std()`, `.quantile(0.75)`, etc.)
3. Call `colN.metric(label, value)` with Rs. formatting

## How to Add New Charts

Charts are defined at lines 52–75. Pattern uses `px.<chart_type>` or `go.Figure`:

```python
st.subheader('Chart Title')
fig = px.<chart_type>(df, x='col_x', y='col_y', title='Title')
st.plotly_chart(fig, use_container_width=True)
```

**Add a new chart below Monthly Revenue:**

```python
st.subheader('Revenue Distribution')
fig4 = px.histogram(df, x='sales', nbins=20, title='Sales Distribution')
st.plotly_chart(fig4, use_container_width=True)
```

To add a chart inside the two-column layout, place it inside one of the existing `with col_left:` or `with col_right:` blocks, or add a new `st.columns(2)` section.

## Modify Synthetic Data Generation

Data generation is at lines 15–34 of `dashboard.py`.

| Parameter | Line | Description |
|-----------|------|-------------|
| `np.random.seed(42)` | 16 | Set random seed for reproducibility |
| `range(180)` | 17 | Number of days to generate |
| `base_sales = 50000` | 18 | Baseline daily sales |
| `trend = np.linspace(0, 20000, 180)` | 19 | Linear upward trend over the period |
| `dow_map = np.array([1.0, 1.0, 1.0, 1.1, 1.2, 1.5, 1.3])` | 21 | Day-of-week multipliers (Mon–Sun) |
| `noise = np.random.normal(0, 5000, 180)` | 23 | Gaussian noise, std=5000 |
| `floor = 10000` | 24 | Minimum daily sales |

To use real data instead, replace lines 15–34 with:

```python
import pandas as pd
df = pd.read_csv('your_sales_data.csv')
# Ensure columns: date, sales
df['date'] = pd.to_datetime(df['date'])
df['day_name'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.strftime('%b')
df['7_day_avg'] = df['sales'].rolling(7).mean()
df['30_day_avg'] = df['sales'].rolling(30).mean()
```

## Deployment to Streamlit Cloud

1. Push the repository to GitHub (`main` branch)
2. Go to https://share.streamlit.io and sign in with GitHub
3. Click "New app"
4. Select: repository `harshvardhankulkarni/sales-dashboard`, branch `main`, file `dashboard.py`
5. Click "Deploy"

The app deploys at `https://harsh-data-analytics-portfolio.streamlit.app` (custom subdomain configured in Streamlit Cloud settings).

No additional configuration file is needed — `requirements.txt` is auto-detected by Streamlit Cloud for dependency installation.
