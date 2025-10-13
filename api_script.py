#!/usr/bin/env python3
"""
This script demonstrates how to use the Requests library to call a REST API
and print the response. It is saved to a randomly named .py file as requested.
"""

import requests
import uuid

# Example: Fetch a random user from the API
API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_user_data():
    """Fetches data from a public API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    print("Fetching data from the API...")
    data = fetch_user_data()
    if data:
        print("Data retrieved successfully!")
        print(data[0])  # Print the first user's data

    # Generate a random filename
    random_filename = f"random_script_{uuid.uuid4().hex[:8]}.py"
    print(f"\nThis script would normally be saved to a file named: {random_filename}")
