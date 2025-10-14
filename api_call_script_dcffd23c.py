import requests

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
