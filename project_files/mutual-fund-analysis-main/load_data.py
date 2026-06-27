import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

nav = pd.read_csv("data/processed/hdfc_top100_nav_clean.csv")
etf = pd.read_csv("data/processed/etf_prices_clean.csv")

nav.to_sql(
    "hdfc_nav",
    engine,
    if_exists="replace",
    index=False
)

etf.to_sql(
    "etf_prices",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully")