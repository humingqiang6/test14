import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 'Age': [25, 30, 35, 40, 22], 'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']}
df = pd.DataFrame(data)

# Filtered DataFrame (Age > 28)
filtered_df = df[df['Age'] > 28]

# Display the result
print("Filtered DataFrame:")
print(filtered_df)

# Optionally, save to CSV
# filtered_df.to_csv('output.csv', index=False)
