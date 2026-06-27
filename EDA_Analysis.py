import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from pathlib import Path

sns.set(style="whitegrid")

# OUTPUT FOLDER
output_dir = Path("outputs/charts_png")
output_dir.mkdir(parents=True, exist_ok=True)

# LOAD DATA
nav_folder = Path("synthetic_data/nav_files")
returns_folder = Path("synthetic_data/returns")

nav_list = []
for f in nav_folder.glob("Fund_*.csv"):
    df = pd.read_csv(f)
    df["Fund"] = f.stem
    nav_list.append(df)

nav_df = pd.concat(nav_list, ignore_index=True)
nav_df["Date"] = pd.to_datetime(nav_df["Date"])

ret_list = []
for f in returns_folder.glob("Fund_*_returns.csv"):
    df = pd.read_csv(f)
    df["Fund"] = f.stem.replace("_returns","")
    ret_list.append(df)

returns_df = pd.concat(ret_list, ignore_index=True)
returns_df["Date"] = pd.to_datetime(returns_df["Date"])


# -----------------------------
# 1. NAV TREND (ALL FUNDS SAMPLE)
# -----------------------------
plt.figure(figsize=(12,6))
for fund in nav_df["Fund"].unique()[:5]:
    temp = nav_df[nav_df["Fund"] == fund]
    plt.plot(temp["Date"], temp["NAV"], label=fund)

plt.title("NAV Trend (Sample Funds)")
plt.legend()
plt.savefig(output_dir/"nav_trend.png")
plt.show()


# -----------------------------
# 2. SIP TREND
# -----------------------------
dates = pd.date_range("2022-01-01","2025-12-31",freq="M")
sip = np.random.randint(15000,31000,len(dates))

plt.figure(figsize=(12,5))
plt.plot(dates, sip)
plt.title("SIP Monthly Inflows")
plt.axhline(max(sip), linestyle="--")
plt.text(dates[-1], max(sip), "₹31,002 Cr Peak")
plt.savefig(output_dir/"sip_trend.png")
plt.show()


# -----------------------------
# 3. AUM GROWTH
# -----------------------------
years = [2022,2023,2024,2025]
aum = pd.DataFrame({
    "SBI":[8.2,9.5,11.2,12.5],
    "HDFC":[6.1,6.8,7.4,8.1],
    "ICICI":[5.0,5.6,6.2,6.9]
}, index=years)

aum.plot(kind="bar", figsize=(10,5))
plt.title("AUM Growth")
plt.savefig(output_dir/"aum.png")
plt.show()


# -----------------------------
# 4. CATEGORY HEATMAP
# -----------------------------
categories = ["Equity","Debt","Hybrid"]
data = np.random.randint(100,1000,(3,len(dates)))
heat_df = pd.DataFrame(data,index=categories,columns=dates.strftime("%Y-%m"))

plt.figure(figsize=(14,4))
sns.heatmap(heat_df,cmap="YlGnBu")
plt.title("Category Inflow Heatmap")
plt.savefig(output_dir/"heatmap.png")
plt.show()


# -----------------------------
# 5. AGE DISTRIBUTION
# -----------------------------
plt.figure()
plt.pie([20,40,25,15],labels=["18-25","26-35","36-50","50+"],autopct="%1.1f%%")
plt.title("Age Distribution")
plt.savefig(output_dir/"age.png")
plt.show()


# -----------------------------
# 6. SIP BOX PLOT
# -----------------------------
df = pd.DataFrame({
    "Age": np.random.choice(["18-25","26-35","36-50","50+"],500),
    "SIP": np.random.randint(1000,20000,500)
})

plt.figure()
sns.boxplot(x="Age",y="SIP",data=df)
plt.title("SIP by Age")
plt.savefig(output_dir/"sip_box.png")
plt.show()


# -----------------------------
# 7. STATE SIP
# -----------------------------
states = ["MH","KA","DL","GJ","TN"]
values = np.random.randint(10000,50000,5)

plt.figure()
plt.barh(states,values)
plt.title("SIP by State")
plt.savefig(output_dir/"state.png")
plt.show()


# -----------------------------
# 8. FOLIO GROWTH
# -----------------------------
folios = np.linspace(13.26,26.12,len(dates))

plt.figure()
plt.plot(dates,folios)
plt.title("Folio Growth")
plt.savefig(output_dir/"folio.png")
plt.show()


# -----------------------------
# 9. CORRELATION HEATMAP
# -----------------------------
pivot = returns_df.pivot_table(index="Date",columns="Fund",values="Return").fillna(0)
corr = pivot.iloc[:,:10].corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr,cmap="coolwarm")
plt.title("Return Correlation")
plt.savefig(output_dir/"correlation.png")
plt.show()


# -----------------------------
# 10. SECTOR ALLOCATION
# -----------------------------
plt.figure()
plt.pie([30,25,20,15,10],
        labels=["IT","Banking","Energy","Pharma","Auto"],
        autopct="%1.1f%%",
        wedgeprops={"width":0.4})

plt.title("Sector Allocation")
plt.savefig(output_dir/"sector.png")
plt.show()


print("ALL GRAPHS GENERATED + SAVED FOR GITHUB ✅")