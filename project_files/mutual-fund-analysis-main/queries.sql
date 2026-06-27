-- 1. Top 5 funds by NAV growth
SELECT amfi_code,
       MAX(nav) - MIN(nav) AS nav_growth
FROM hdfc_nav
GROUP BY amfi_code
ORDER BY nav_growth DESC
LIMIT 5;

-- 2. CAGR (approx yearly return)
SELECT amfi_code,
       (POWER(MAX(nav) * 1.0 / MIN(nav),
        1.0 / ((julianday(MAX(date)) - julianday(MIN(date))) / 365.25)) - 1) * 100
       AS cagr_pct
FROM hdfc_nav
GROUP BY amfi_code;

-- 3. Average NAV per month
SELECT substr(date,1,7) AS month,
       AVG(nav) AS avg_nav
FROM hdfc_nav
GROUP BY month;

-- 4. ETF average closing price per fund
SELECT fund_symbol,
       AVG(close) AS avg_close
FROM etf_prices
GROUP BY fund_symbol;

-- 5. Highest ETF trading volume
SELECT fund_symbol,
       SUM(volume) AS total_volume
FROM etf_prices
GROUP BY fund_symbol
ORDER BY total_volume DESC
LIMIT 5;

-- 6. Total NAV records
SELECT COUNT(*) AS total_nav FROM hdfc_nav;

-- 7. Date range coverage
SELECT MIN(date) AS start_date,
       MAX(date) AS end_date
FROM hdfc_nav;

-- 8. Best performing funds (simple return %)
SELECT amfi_code,
       (MAX(nav)/MIN(nav)-1)*100 AS return_pct
FROM hdfc_nav
GROUP BY amfi_code
ORDER BY return_pct DESC
LIMIT 5;

-- 9. Monthly ETF average close
SELECT substr(price_date,1,7) AS month,
       AVG(close) AS avg_close
FROM etf_prices
GROUP BY month;

-- 10. Funds with stable NAV (low volatility proxy)
SELECT amfi_code,
       MAX(nav) - MIN(nav) AS volatility
FROM hdfc_nav
GROUP BY amfi_code
ORDER BY volatility ASC
LIMIT 5;