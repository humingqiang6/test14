import pandas as pd

# This script recreates the filtered DataFrame.
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'], 'Age': [25, 30, 35, 40, 22], 'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 25]
print(filtered_df)
