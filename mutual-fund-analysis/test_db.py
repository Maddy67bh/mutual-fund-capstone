import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

print("HDFC NAV")
print(pd.read_sql(
    "SELECT COUNT(*) AS rows FROM hdfc_nav",
    conn
))

print("\nETF Prices")
print(pd.read_sql(
    "SELECT COUNT(*) AS rows FROM etf_prices",
    conn
))