txn = pd.read_csv("data/raw/investor_transactions.csv")

txn.columns = txn.columns.str.lower()

txn['transaction_date'] = pd.to_datetime(
    txn['transaction_date'],
    errors='coerce'
)

mapping = {
    'sip': 'SIP',
    'systematic investment plan': 'SIP',
    'lumpsum': 'Lumpsum',
    'lump sum': 'Lumpsum',
    'redemption': 'Redemption',
    'redeem': 'Redemption'
}

txn['transaction_type'] = (
    txn['transaction_type']
    .str.lower()
    .map(mapping)
)

txn = txn[txn['amount'] > 0]

valid_kyc = ['Verified', 'Pending', 'Rejected']

txn.loc[
    ~txn['kyc_status'].isin(valid_kyc),
    'kyc_status'
] = 'Pending'

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print(txn['transaction_type'].value_counts())
print(txn['kyc_status'].value_counts())