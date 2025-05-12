import pandas as pd

series = pd.Series([1, 2, 3, 4, 5])
my_list = series.tolist()

print(my_list)
print(type(my_list))  # Output: <class 'list'>