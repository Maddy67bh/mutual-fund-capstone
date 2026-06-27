import pandas as pd

df = pd.read_csv("data/raw/ETF prices.csv")

print("\nDataset Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nUnique Funds")
print(df["fund_symbol"].nunique())