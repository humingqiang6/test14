import json
import random
import string

# Sample data to populate the JSON
first_names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Oliver"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
domains = ["example.com", "mail.com", "test.org", "demo.net"]

def generate_random_string(length=6):
    """Generates a random string of lowercase letters."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_user_data(num_users=5):
    """Generates a list of user dictionaries."""
    users = []
    for _ in range(num_users):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{name.split()[0].lower()}.{name.split()[1].lower()}@{random.choice(domains)}"
        age = random.randint(18, 80)
        active = random.choice([True, False])
        users.append({
            "id": random.randint(1000, 9999),
            "name": name,
            "email": email,
            "age": age,
            "active": active
        })
    return users

def main():
    # Generate the data
    api_response_data = {
        "status": "success",
        "data": generate_user_data(5),
        "total": 5
    }

    # Generate a random filename
    random_filename = f"api_response_{generate_random_string()}.json"
    
    # Write the data to the file
    with open(random_filename, 'w', encoding='utf-8') as f:
        json.dump(api_response_data, f, indent=2)
    
    print(f"API response data generated and saved to {random_filename}")

if __name__ == "__main__":
    main()
