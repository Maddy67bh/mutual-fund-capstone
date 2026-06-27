-- 1. Total NAV records
SELECT COUNT(*) FROM hdfc_nav;

-- 2. ETF records
SELECT COUNT(*) FROM etf_prices;

-- 3. Date range NAV
SELECT MIN(date), MAX(date) FROM hdfc_nav;

-- 4. HDFC total return %
SELECT 
  (MAX(nav) - MIN(nav)) * 100.0 / MIN(nav) AS return_pct
FROM hdfc_nav;

-- 5. Top ETF by price movement
SELECT fund_symbol,
       (MAX(close) - MIN(close)) * 100.0 / MIN(close) AS return_pct
FROM etf_prices
GROUP BY fund_symbol
ORDER BY return_pct DESC
LIMIT 5;

-- 6. Avg NAV
SELECT AVG(nav) FROM hdfc_nav;

-- 7. Max NAV
SELECT MAX(nav) FROM hdfc_nav;

-- 8. Min NAV
SELECT MIN(nav) FROM hdfc_nav;