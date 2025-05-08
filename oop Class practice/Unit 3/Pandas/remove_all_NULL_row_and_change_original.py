import pandas as pd
df = pd.read_csv("health.csv")
new_df=df.dropna(inplace=True)
print(new_df)

df=pd.write_csv("health.")
"""This will remove and make chnages  to original ,dataframe."""