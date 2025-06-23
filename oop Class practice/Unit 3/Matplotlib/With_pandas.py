import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 120, 90, 140, 160]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot using matplotlib
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
