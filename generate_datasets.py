import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

# Create output folders
output = Path("synthetic_data")
output.mkdir(exist_ok=True)

nav_folder = output / "nav_files"
nav_folder.mkdir(exist_ok=True)

# =====================================================
# 40 Mutual Fund NAV Files
# =====================================================

funds = [
    "SBI_Bluechip","HDFC_Top100","ICICI_Bluechip","Axis_Bluechip",
    "Kotak_Bluechip","Mirae_LargeCap","DSP_FlexiCap","UTI_FlexiCap",
    "Nippon_LargeCap","Canara_Bluechip",
    "Fund11","Fund12","Fund13","Fund14","Fund15",
    "Fund16","Fund17","Fund18","Fund19","Fund20",
    "Fund21","Fund22","Fund23","Fund24","Fund25",
    "Fund26","Fund27","Fund28","Fund29","Fund30",
    "Fund31","Fund32","Fund33","Fund34","Fund35",
    "Fund36","Fund37","Fund38","Fund39","Fund40"
]

dates = pd.date_range("2022-01-01", "2026-12-31", freq="B")

for fund in funds:
    nav = 100 + np.cumsum(np.random.normal(0.08, 1.0, len(dates)))

    df = pd.DataFrame({
        "Date": dates,
        "NAV": nav.round(2)
    })

    df.to_csv(nav_folder / f"{fund}.csv", index=False)

print("✓ 40 NAV files created")