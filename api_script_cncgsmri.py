import requests

# Script generated to fetch data from a REST API
API_ENDPOINT = "https://jsonplaceholder.typicode.com/posts/1"

def get_data():
    response = requests.get(API_ENDPOINT)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = get_data()
    print("Data fetched from API:")
    print(data)

