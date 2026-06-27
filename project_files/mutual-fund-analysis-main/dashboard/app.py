import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mutual Fund Dashboard", layout="wide")

st.title("📊 Mutual Fund & ETF Analysis Dashboard")

# TEMP sample data (replace later with your dataset)
df = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=100),
    "Price": range(100),
    "Fund Name": ["Fund A"] * 100,
    "Returns": [x * 0.1 for x in range(100)]
})

funds = df["Fund Name"].unique()
selected_fund = st.selectbox("Select Fund", funds)

filtered = df[df["Fund Name"] == selected_fund]

st.line_chart(filtered.set_index("Date")["Price"])

st.bar_chart(filtered["Returns"])