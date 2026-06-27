import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

nav = pd.read_sql("SELECT * FROM hdfc_nav", engine)

print(nav.head())
print(nav.shape)