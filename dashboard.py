"""
Interactive Sales Dashboard (Streamlit)
Run with: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title='Sales Analytics Dashboard', layout='wide')

# Generate synthetic data
np.random.seed(42)
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(180)]
base_sales = 50000
trend = np.linspace(0, 20000, 180)
weekly = 1 + 0.3 * np.sin(np.pi * np.arange(180) / 3.5)
dow_map = np.array([1.0, 1.0, 1.0, 1.1, 1.2, 1.5, 1.3])
day_factors = [dow_map[d.weekday()] for d in dates]
noise = np.random.normal(0, 5000, 180)
sales = np.maximum((base_sales + trend) * weekly * np.array(day_factors) + noise, 10000).round(2)

df = pd.DataFrame({
    'date': dates,
    'sales': sales,
    'day_name': [d.strftime('%A') for d in dates],
    'month': [d.strftime('%b') for d in dates],
})

df['7_day_avg'] = df['sales'].rolling(7).mean()
df['30_day_avg'] = df['sales'].rolling(30).mean()

# KPI row
st.title('Business Performance Dashboard')
st.markdown('Daily sales monitoring across 180 days.')

col1, col2, col3, col4 = st.columns(4)
total_revenue = df['sales'].sum()
avg_daily = df['sales'].mean()
peak_day = df.loc[df['sales'].idxmax(), 'date'].strftime('%b %d')
peak_value = df['sales'].max()
recent_7 = df['sales'].tail(7).mean()

col1.metric('Total Revenue', f'Rs.{total_revenue:,.0f}')
col2.metric('Daily Average', f'Rs.{avg_daily:,.0f}')
col3.metric('Peak Day', f'Rs.{peak_value:,.0f}', f'On {peak_day}')
col4.metric('Last 7 Days Avg', f'Rs.{recent_7:,.0f}')

# Sales trend chart
st.subheader('Sales Trend')
fig = px.line(df, x='date', y='sales', title='Daily Sales')
fig.add_scatter(x=df['date'], y=df['7_day_avg'], mode='lines', name='7-Day Avg', line=dict(color='red'))
fig.add_scatter(x=df['date'], y=df['30_day_avg'], mode='lines', name='30-Day Avg', line=dict(color='green'))
st.plotly_chart(fig, use_container_width=True)

# Two columns: day of week + monthly
col_left, col_right = st.columns(2)

with col_left:
    st.subheader('Sales by Day of Week')
    dow_df = df.groupby('day_name')['sales'].mean().reset_index()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dow_df['day_name'] = pd.Categorical(dow_df['day_name'], categories=day_order, ordered=True)
    dow_df = dow_df.sort_values('day_name')
    fig2 = px.bar(dow_df, x='day_name', y='sales', title='Average Daily Sales')
    st.plotly_chart(fig2, use_container_width=True)

with col_right:
    st.subheader('Monthly Revenue')
    monthly_df = df.groupby('month')['sales'].sum().reset_index()
    fig3 = px.bar(monthly_df, x='month', y='sales', title='Total Monthly Sales')
    st.plotly_chart(fig3, use_container_width=True)

# Raw data expander
with st.expander('View Raw Data'):
    st.dataframe(df.head(50), use_container_width=True)
    csv = df.to_csv(index=False)
    st.download_button('Download CSV', csv, 'sales_data.csv', 'text/csv')
