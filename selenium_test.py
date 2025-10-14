import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Wait for a few seconds to see the page
    driver.implicitly_wait(5)

    # Generate a random filename
    random_filename = "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + ".py"

    # Save the current script as the random filename
    with open(random_filename, 'w') as f:
        f.write('''from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(5)
driver.quit()
''')

    print(f"Selenium test saved to {random_filename}")

finally:
    # Close the browser
    driver.quit()
