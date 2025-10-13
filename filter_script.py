import pandas as pd
import random
import string

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 22],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']
}
df = pd.DataFrame(data)

# Filter the DataFrame (e.g., Age > 25)
filtered_df = df[df['Age'] > 25]

# Generate a random filename
random_filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.py'

# Save the filtered DataFrame to the randomly named file
# This saves the DataFrame object itself, which is unusual. A more common task would be to save it as CSV.
# Saving the script that creates the filtered data.
script_content = f'''import pandas as pd

# This script recreates the filtered DataFrame.
data = {data}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 25]
print(filtered_df)
'''
with open(random_filename, 'w') as f:
    f.write(script_content)

print(f"Filtered DataFrame saved to {random_filename}")
print(filtered_df)
