<!-- GSD -->

# Testing

## Current Status

This project has **no automated test suite**. The application is a single-file Streamlit demo with synthetic data — testing relies entirely on manual validation.

## Manual Validation Checklist

Run the dashboard locally or access the live demo, then verify each item:

### KPI Cards

- [ ] **Total Revenue** displays a positive number (~Rs.12,100,000)
- [ ] **Daily Average** displays a positive number (~Rs.67,000)
- [ ] **Peak Day** shows a date (e.g., "Jun 28") and a value higher than daily average
- [ ] **Last 7 Days Avg** displays a positive number
- [ ] All four cards render in a single row with equal widths
- [ ] No card shows `NaN`, `Infinity`, or formatting errors

### Sales Trend Chart

- [ ] Chart renders with title "Daily Sales"
- [ ] Blue line shows daily sales data
- [ ] Red line shows 7-day rolling average
- [ ] Green line shows 30-day rolling average
- [ ] Legend displays all three series
- [ ] Hovering over a data point shows date and value
- [ ] Zoom/pan interactions work
- [ ] Axes are properly labeled

### Sales by Day of Week

- [ ] Bar chart renders with title "Average Daily Sales"
- [ ] Seven bars labeled Monday through Sunday in order
- [ ] Saturday bar is visibly highest (due to 1.5× multiplier)
- [ ] Hover shows day name and average value
- [ ] Bars are distinguishable by color

### Monthly Revenue

- [ ] Bar chart renders with title "Total Monthly Sales"
- [ ] Six bars for Jan through Jun
- [ ] Later months show higher values (due to upward trend)
- [ ] Hover shows month and total value

### Raw Data Expander

- [ ] Expander collapses/expands on click
- [ ] Data table shows 50 rows with columns: date, sales, day_name, month, 7_day_avg, 30_day_avg
- [ ] "Download CSV" button is present
- [ ] Downloaded CSV opens correctly and contains all 180 rows

### General

- [ ] Page title displays "Sales Analytics Dashboard"
- [ ] Layout uses full browser width
- [ ] Page loads without errors in Streamlit console
- [ ] Responsive: layout reflows reasonably on mobile (768px width)
- [ ] No console JavaScript errors in browser dev tools

### Cross-browser (if applicable)

- [ ] Works in Chrome
- [ ] Works in Firefox
- [ ] Works in Edge

## Automated Test Recommendations

If test coverage is added, priority areas:

1. **Data generation** — Verify DataFrame shape (180×6), column types, no nulls, sales floor >= 10,000
2. **KPI calculations** — Assert `total_revenue` matches `df['sales'].sum()`, `peak_day` matches `.idxmax()`
3. **Rolling averages** — Assert `7_day_avg[6]` equals `df['sales'].iloc[:7].mean()`
4. **Data export** — Assert `df.to_csv()` produces valid CSV with correct row count
