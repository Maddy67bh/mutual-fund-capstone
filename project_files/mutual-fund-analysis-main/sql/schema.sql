CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT
);

CREATE TABLE fact_nav (
    id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date TEXT,
    nav REAL
);

CREATE TABLE fact_etf_prices (
    id INTEGER PRIMARY KEY,
    fund_symbol TEXT,
    price_date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL
);