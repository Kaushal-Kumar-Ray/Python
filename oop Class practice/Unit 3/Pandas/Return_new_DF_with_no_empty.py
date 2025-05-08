import pandas as pd
df=pd.read_csv("health.csv")
new_data=df.dropna()
print(new_data)


"""HEre we will get a new DataFrame with no empty values. but the original
dataframe will remain unchanged."""