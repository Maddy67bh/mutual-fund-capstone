import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mutual Fund Dashboard", layout="wide")

st.title("📊 Mutual Fund Analysis Dashboard")

# ---------------------------
# LOAD DATA
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/hdfc_top100_nav.csv")
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    return df

df = load_data()

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start Date", df["date"].min())
end_date = st.sidebar.date_input("End Date", df["date"].max())

filtered_df = df[(df["date"] >= pd.to_datetime(start_date)) &
                 (df["date"] <= pd.to_datetime(end_date))]

# ---------------------------
# KPI METRICS
# ---------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Latest NAV", round(filtered_df["nav"].iloc[-1], 2))
col2.metric("Max NAV", round(filtered_df["nav"].max(), 2))
col3.metric("Min NAV", round(filtered_df["nav"].min(), 2))

# ---------------------------
# NAV TREND
# ---------------------------
fig = px.line(filtered_df, x="date", y="nav",
              title="NAV Trend Over Time")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# DATA TABLE
# ---------------------------
st.subheader("📄 Raw Data")
st.dataframe(filtered_df)