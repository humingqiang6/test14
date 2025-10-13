import pandas as pd
import random
import string

def generate_random_filename(length=8, prefix="filtered_data_", suffix=".py"):
    """Generates a random filename."""
    random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return f"{prefix}{random_string}{suffix}"

def create_and_filter_data():
    """Creates a sample DataFrame, filters it, and saves the script to a random .py file."""
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 22],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']
    }
    df = pd.DataFrame(data)

    # Filter the DataFrame (e.g., Age > 28)
    filtered_df = df[df['Age'] > 28]

    # Generate a random filename
    random_filename = generate_random_filename()

    # Create the script content as a string
    script_content = f'''import pandas as pd

# Sample DataFrame
data = {data}
df = pd.DataFrame(data)

# Filtered DataFrame (Age > 28)
filtered_df = df[df['Age'] > 28]

# Display the result
print("Filtered DataFrame:")
print(filtered_df)

# Optionally, save to CSV
# filtered_df.to_csv('output.csv', index=False)
'''

    # Write the script content to the randomly named file
    with open(random_filename, 'w') as f:
        f.write(script_content)

    print(f"Script saved to {random_filename}")

if __name__ == "__main__":
    create_and_filter_data()
