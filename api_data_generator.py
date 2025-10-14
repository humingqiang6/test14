import json
import random
import string
from datetime import datetime

def generate_sample_data():
    """Generates a sample JSON object simulating an API response."""
    data = {
        "timestamp": datetime.now().isoformat(),
        "users": [
            {
                "id": i,
                "name": f"User {random.choice(string.ascii_uppercase)}{i}",
                "email": f"user{i}@example.com",
                "active": random.choice([True, False]),
                "signup_date": datetime.now().isoformat()
            }
            for i in range(1, random.randint(3, 6))
        ],
        "total_count": random.randint(10, 100)
    }
    return data

def save_to_random_file(data, directory="/workspace"):
    """Saves the data to a randomly named JSON file."""
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".json"
    filepath = f"{directory}/{random_name}"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return filepath

if __name__ == "__main__":
    sample_data = generate_sample_data()
    saved_file_path = save_to_random_file(sample_data)
    print(f"Data saved to: {saved_file_path}")