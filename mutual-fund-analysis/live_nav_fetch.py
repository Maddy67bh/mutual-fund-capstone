import requests
import pandas as pd

schemes = {
    "HDFC": 125497,
    "SBI": 119551,
    "ICICI": 120503,
    "Nippon": 118632,
    "Axis": 119092,
    "Kotak": 120841
}

all_data = []

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    res = requests.get(url).json()

    if "data" in res:
        df = pd.DataFrame(res["data"])
        df["scheme"] = name
        df["scheme_code"] = code
        all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

final_df.to_csv("data/raw/multi_scheme_nav.csv", index=False)

print("DONE: Data saved successfully")
print(final_df.head())
