import pandas as pd

df = pd.read_csv("synthetic_data/all_funds_nav.csv")

print(df.head())
print(df.isnull().sum())
print(df.groupby("Fund")["NAV"].describe())