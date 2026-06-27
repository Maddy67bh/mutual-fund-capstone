📌 1. hdfc\_nav (NAV Time Series)

Column	Type	Description

date	TEXT	NAV record date (YYYY-MM-DD)

nav	FLOAT	Net Asset Value of fund



Business Meaning:



Tracks daily NAV movement of mutual funds

Used for return calculation and CAGR analysis

📌 2. etf\_prices (ETF Market Data)

Column	Type	Description

fund\_symbol	TEXT	ETF ticker symbol

price\_date	TEXT	Trading date

open	FLOAT	Opening price

high	FLOAT	Highest price of day

low	FLOAT	Lowest price of day

close	FLOAT	Closing price

adj\_close	FLOAT	Adjusted closing price

volume	INTEGER	Trading volume



Business Meaning:



Used for price trend analysis

Helps measure liquidity and volatility

📌 3. Derived Tables (Future Schema)

dim\_fund

fund\_id → Unique fund identifier

amfi\_code → AMFI scheme code

fund\_name → Name of mutual fund

category → Equity/Debt/Hybrid

fund\_house → AMC name

dim\_date

date\_id → Surrogate key

full\_date → Calendar date

year → Year

month → Month

day → Day

quarter → Quarter

fact\_nav

nav\_id → Unique row ID

amfi\_code → Fund reference

date → NAV date

nav → NAV value

fact\_transactions

txn\_id → Transaction ID

investor\_id → Investor reference

transaction\_type → SIP / Lumpsum / Redemption

amount → Transaction amount

units → Units purchased/sold

fact\_performance

return\_1y → 1 Year return %

return\_3y → 3 Year return %

expense\_ratio → Fund expense %

fact\_aum

aum → Assets Under Management

Tracks fund size over time

📌 Data Source

Internal cleaned dataset (CSV processed from raw NAV \& ETF files)

Stored in SQLite: bluestock\_mf.db

🎯 Notes

Missing values handled via forward-fill (NAV)

Duplicates removed during cleaning

All numeric fields validated (>0 where applicable)

🚀 END OF DOCUMENT

