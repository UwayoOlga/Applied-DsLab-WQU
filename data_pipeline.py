import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('real_estate_data.csv')
print("Raw data preview")
print(df.head())

df.dropna(inplace=True)

df.columns = df.columns.str.lower().str.replace(' ', '_')
df = df[df['price_usd'] < 400000]

print("\nCleaned and filtered data preview:")
print(df.head())

engine = create_engine('mysql+pymysql://root:@localhost/real_estate_pipeline')

df.to_sql('properties', con=engine,if_exists='append',index=False)