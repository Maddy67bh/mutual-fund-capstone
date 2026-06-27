import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

queries = {
    "hdfc_count": "SELECT COUNT(*) FROM hdfc_nav",
    "etf_count": "SELECT COUNT(*) FROM etf_prices",
    "hdfc_avg": "SELECT AVG(nav) FROM hdfc_nav",
    "etf_sample": "SELECT * FROM etf_prices LIMIT 5"
}

for name, q in queries.items():
    print("\n", name)
    print(pd.read_sql(q, engine))