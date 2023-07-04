import pandas as pd
import pyarrow

df=pd.read_csv("pokemon_details.csv")
df.to_parquet("df.parquet.gzip",compression='gzip')
df_parquet=pd.read_parquet('df.parquet.gzip')

print(df_parquet)