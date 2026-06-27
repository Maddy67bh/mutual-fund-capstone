import pandas as pd

# Load data
etf = pd.read_csv("data/raw/ETF prices.csv")
nav = pd.read_csv("data/raw/hdfc_top100_nav.csv")

print("ETF Shape:", etf.shape)
print("NAV Shape:", nav.shape)

# Basic cleaning (safe start)
print("\nETF Columns:", etf.columns)
print("\nNAV Columns:", nav.columns)

print("\nETF Preview:")
print(etf.head())

print("\nNAV Preview:")
print(nav.head())