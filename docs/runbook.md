# Runbook: Sales Analytics Dashboard

## When to Use This Runbook

- Running the dashboard for the first time.
- Deploying to Streamlit Cloud.
- Switching from synthetic to real data.
- Troubleshooting deployment or rendering issues.

## Prerequisites

- Python 3.8+ installed.
- Git installed.
- GitHub account (for deployment).
- Streamlit Cloud account (sign in with GitHub).

## Procedure

### Option A: Run Locally

#### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 2: Start the Dashboard

```bash
streamlit run dashboard.py
```

#### Step 3: Open Browser

Visit `http://localhost:8501`. The dashboard loads with synthetic data.

### Option B: Deploy to Streamlit Cloud

#### Step 1: Push to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

#### Step 2: Deploy

1. Go to https://share.streamlit.io.
2. Click "New app".
3. Select repository, branch `main`, file `dashboard.py`.
4. Click "Deploy".

#### Step 3: Verify

Visit the deployment URL. It looks like:

`https://[username]-[repo]-dashboard.streamlit.app`

### Option C: Connect Real Data

#### Step 1: Replace Data Generation

Remove lines 14-26 in `dashboard.py` and add:

```python
import pandas as pd
df = pd.read_csv('your_sales.csv')
```

#### Step 2: Adjust Columns

Ensure your CSV has at least these columns:

- `date` - Date in YYYY-MM-DD format.
- `sales` - Numeric sales value.

#### Step 3: Commit and Redeploy

```bash
git add dashboard.py your_sales.csv
git commit -m "Switch to real data"
git push
```

Streamlit Cloud auto redeploys on push.

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| App not found | Wrong file path in deployment | Check `dashboard.py` is in the repo root |
| Charts blank | Empty DataFrame | Check data generation or CSV import |
| ModuleNotFoundError | Missing requirements | Verify `requirements.txt` includes all packages |
| Slow loading | Too much data | Aggregate data before passing to Plotly |
| Streamlit Cloud error | Build failure | Check deployment logs in Streamlit dashboard |
| Data not updating | Static generation | Add `st.cache_data` or database refresh |

## Common Tasks

### Update the Dashboard

1. Edit `dashboard.py` locally.
2. Test with `streamlit run dashboard.py`.
3. Commit and push. Streamlit Cloud auto redeploys.

### Add a New Chart

```python
st.subheader('New Chart Name')
fig = px.line(df, x='date', y='column_name', title='Title')
st.plotly_chart(fig, use_container_width=True)
```

### Change the Color Theme

Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#31333F"
font = "sans serif"
```

## Escalation

If the dashboard fails to deploy or render:

1. Check Streamlit Cloud status at https://status.streamlit.io.
2. Review app logs in Streamlit Cloud dashboard.
3. Open a GitHub issue with:
   - Deployment URL (if applicable).
   - Error message from logs.
   - Steps to reproduce.
