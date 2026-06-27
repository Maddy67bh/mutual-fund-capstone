import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mutual Fund Dashboard", layout="wide")

st.title("📊 Mutual Fund & ETF Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("../data/processed/cleaned_data.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

funds = df["Fund Name"].unique()
selected_fund = st.sidebar.selectbox("Select Fund", funds)

filtered_df = df[df["Fund Name"] == selected_fund]

# KPI section
col1, col2, col3 = st.columns(3)

col1.metric("Records", len(filtered_df))
col2.metric("Avg Price", round(filtered_df["Price"].mean(), 2))
col3.metric("Max Price", round(filtered_df["Price"].max(), 2))

# Price Trend
st.subheader("Price Trend")

fig = px.line(
    filtered_df,
    x="Date",
    y="Price",
    title=f"{selected_fund} Price Trend"
)

st.plotly_chart(fig, use_container_width=True)

# Returns distribution
st.subheader("Returns Distribution")

fig2 = px.histogram(filtered_df, x="Returns", nbins=30)
st.plotly_chart(fig2, use_container_width=True)

# Correlation (if multiple funds)
if "Returns" in df.columns:
    st.subheader("Correlation Heatmap")

    pivot = df.pivot_table(values="Returns", index="Date", columns="Fund Name")
    fig3 = px.imshow(pivot.corr(), text_auto=True)
    st.plotly_chart(fig3, use_container_width=True)