-- Monthly average NAV
SELECT strftime('%Y-%m', date) month,
AVG(nav)
FROM hdfc_nav
GROUP BY month;

-- Top 5 ETFs by average price
SELECT fund_symbol,
AVG(close) avg_price
FROM etf_prices
GROUP BY fund_symbol
ORDER BY avg_price DESC
LIMIT 5;

-- ETF count
SELECT COUNT(DISTINCT fund_symbol)
FROM etf_prices;

-- NAV volatility
SELECT AVG(nav), MIN(nav), MAX(nav)
FROM hdfc_nav;