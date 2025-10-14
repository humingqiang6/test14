import os
import requests
import uuid

def generate_api_script():
    """Generates a Python script that calls a REST API."""
    script_content = '''import requests

# Example: Fetching a random user from the reqres.in API
url = "https://reqres.in/api/users"
params = {"delay": 3}  # Optional: Add a delay parameter

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()
    print("API Response:")
    print(data)

except requests.exceptions.RequestException as e:
    print(f"An error occurred while calling the API: {e}")
'''

    # Generate a random filename with .py extension
    random_filename = f"api_call_script_{uuid.uuid4().hex[:8]}.py"
    full_path = os.path.join(os.getcwd(), random_filename)

    with open(full_path, 'w') as f:
        f.write(script_content)

    print(f"Python script generated successfully: {full_path}")
    return full_path

if __name__ == "__main__":
    generate_api_script()
