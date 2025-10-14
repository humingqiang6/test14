import random
import string
import requests

def generate_random_filename():
    """Generates a random filename with a .py extension."""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}.py"

def create_api_script():
    """Creates a Python script that calls a REST API using Requests."""
    script_content = '''import requests

# Example: Fetching data from a public API
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data retrieved successfully!")
    print(data)
else:
    print(f"Error: {response.status_code}")
'''

    filename = generate_random_filename()
    with open(filename, 'w') as f:
        f.write(script_content)

    print(f"Python script created: {filename}")
    return filename

if __name__ == "__main__":
    create_api_script()