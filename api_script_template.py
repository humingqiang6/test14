import requests
import json

def call_api_and_save(url, output_file):
  """
  Calls a REST API, gets the JSON response, and saves it to a file.

  Args:
    url: The URL of the REST API endpoint.
    output_file: The name of the file to save the response to.
  """
  try:
    # Make the GET request
    response = requests.get(url)

    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Save the data to the specified file
    with open(output_file, 'w', encoding='utf-8') as f:
      json.dump(data, f, indent=2)

    print(f"API response successfully saved to {output_file}")

  except requests.exceptions.RequestException as e:
    print(f"An error occurred while calling the API: {e}")
  except json.JSONDecodeError:
    print("Error: The response was not valid JSON.")
  except IOError as e:
    print(f"An error occurred while writing the file: {e}")

if __name__ == "__main__":
  # Example API: JSONPlaceholder - a fake online REST API for testing
  API_URL = "https://jsonplaceholder.typicode.com/posts/1"
  OUTPUT_FILE = "api_response.json"
  call_api_and_save(API_URL, OUTPUT_FILE)
