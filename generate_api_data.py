import json
import random
import string
from datetime import datetime

def generate_mock_data():
    """Generates a mock JSON API response."""
    data = {
        "status": "success",
        "data": {
            "id": random.randint(1, 10000),
            "name": "".join(random.choices(string.ascii_letters, k=10)),
            "email": f"{''.join(random.choices(string.ascii_lowercase, k=5))}@example.com",
            "timestamp": datetime.now().isoformat()
        },
        "message": "Data fetched successfully."
    }
    return data

def save_to_random_file(data):
    """Saves the data to a randomly named JSON file."""
    random_filename = f"api_response_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}.json"
    full_path = f"/workspace/{random_filename}"
    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {full_path}")
    return full_path

if __name__ == "__main__":
    mock_data = generate_mock_data()
    file_path = save_to_random_file(mock_data)