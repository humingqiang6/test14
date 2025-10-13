import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def generate_random_filename(length=10):
    """Generates a random filename with a .py extension."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)) + ".py"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Generate a random filename
    filename = generate_random_filename()

    # Save the current URL to the randomly named file
    with open(filename, 'w') as f:
        f.write(f"Current URL: {driver.current_url}\n")
        f.write(f"Title: {driver.title}\n")

    print(f"Test completed. Data saved to {filename}")

finally:
    # Close the browser
    driver.quit()
