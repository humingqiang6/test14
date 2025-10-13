import requests
import random
import string

# Configuration
API_URL = "https://jsonplaceholder.typicode.com/posts/1"  # Example API endpoint
OUTPUT_DIR = "/workspace"

def generate_random_filename(length=8, prefix="api_script_", suffix=".py"):
    """Generates a random filename with a prefix and suffix."""
    random_chars = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return f"{prefix}{random_chars}{suffix}"

def fetch_and_save_api_data(url, output_directory):
    """Fetches data from a REST API and saves a script that fetched it to a random .py file."""
    try:
        print(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # The script content to save
        script_content = f'''import requests

# Script generated to fetch data from a REST API
API_ENDPOINT = "{url}"

def get_data():
    response = requests.get(API_ENDPOINT)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = get_data()
    print("Data fetched from API:")
    print(data)

'''
        # Generate a random filename
        random_filename = generate_random_filename()
        full_path = f"{output_directory}/{random_filename}"

        # Write the script content to the randomly named file
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(script_content)

        print(f"API data fetched successfully.")
        print(f"Python script saved to: {full_path}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the API: {e}")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")

if __name__ == "__main__":
    fetch_and_save_api_data(API_URL, OUTPUT_DIR)
