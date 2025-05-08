import pandas as pd
df = pd.read_csv("health.csv")
df.fillna(120,inplace=True)
print(df)