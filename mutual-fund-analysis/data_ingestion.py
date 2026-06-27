import pandas as pd

# Load CSVs (example structure)
files = [
    "data/raw/file1.csv",
    "data/raw/file2.csv"
]

for f in files:
    try:
        df = pd.read_csv(f)
        print("\nFILE:", f)
        print("Shape:", df.shape)
        print(df.dtypes)
        print(df.head())
    except Exception as e:
        print("Error:", f, e)