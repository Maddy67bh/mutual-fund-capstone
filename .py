import pandas as pd
from pathlib import Path

folder = Path("synthetic_data/nav_files")

all_data = []

for file in folder.glob("Fund_*.csv"):
    df = pd.read_csv(file)
    df["Fund"] = file.stem
    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

final_df.to_csv("synthetic_data/all_funds_nav.csv", index=False)

print("Merged dataset created!")