import requests

# Example: Fetching data from a public API
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data retrieved successfully!")
    print(data)
else:
    print(f"Error: {response.status_code}")
