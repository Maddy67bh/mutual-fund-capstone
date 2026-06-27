import pandas as pd

etf = pd.read_csv("data/raw/ETF prices.csv")

etf['price_date'] = pd.to_datetime(
    etf['price_date'],
    errors='coerce'
)

price_cols = [
    'open',
    'high',
    'low',
    'close',
    'adj_close'
]

for col in price_cols:
    etf[col] = pd.to_numeric(
        etf[col],
        errors='coerce'
    )

etf['volume'] = pd.to_numeric(
    etf['volume'],
    errors='coerce'
)

etf = etf.drop_duplicates()
etf = etf.dropna()

etf = etf[
    (etf['open'] > 0) &
    (etf['high'] > 0) &
    (etf['low'] > 0) &
    (etf['close'] > 0)
]

etf.to_csv(
    "data/processed/etf_prices_clean.csv",
    index=False
)

print(etf.shape)
print(etf.head())