import pandas as pd

# 1. Read the CSV file
df = pd.read_csv('assignment.csv')

# 2. Show the first 2 rows
print("\nFirst 2 rows:\n", df.head(2))

"""# 3. Check the shape (number of rows and columns)
print("\nShape:", df.shape)

# 4. Sort by 'Age'
sorted_df = df.sort_values(by='Age')
print("\nSorted by Age:\n", sorted_df)

# 5. Summary statistics (like mean, min, max)
print("\nSummary statistics:\n", df.describe())

# 6. Fill missing values (we'll set a value manually for demo)
df['Salary'][1] = None  # Introduce a missing value
df_filled = df.fillna({'Salary': 55000})  # Fill missing with 55000
print("\nAfter filling missing values:\n", df_filled)

# 7. Rename columns (change 'Name' to 'Full Name')
df_renamed = df.rename(columns={'Name': 'Full Name'})
print("\nRenamed columns:\n", df_renamed)

# 8. Concatenate (combine two DataFrames)
df2 = pd.DataFrame({
    'Full Name': ['Sara'],
    'Age': [26],
    'Salary': [53000]
})
concat_df = pd.concat([df_renamed, df2], ignore_index=True)
print("\nConcatenated DataFrame:\n", concat_df)"""
