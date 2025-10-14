import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup the Chrome driver with WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open Google
    driver.get("https://www.google.com")

    # Wait for a few seconds to see the page load (optional)
    driver.implicitly_wait(5)

    # Generate a random filename
    random_filename = "selenium_test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".py"

    # Save the current script to the random filename
    # In a real scenario, you might save different content. Here, we save this script itself.
    with open(random_filename, 'w') as f:
        f.write('''import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup the Chrome driver with WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open Google
    driver.get("https://www.google.com")

    # Wait for a few seconds to see the page load (optional)
    driver.implicitly_wait(5)

    # Generate a random filename
    random_filename = "selenium_test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".py"

    # Save the current script to the random filename
    # In a real scenario, you might save different content. Here, we save this script itself.
    with open(random_filename, 'w') as f:
        f.write(<content_to_save>)
    print(f"Script saved to {random_filename}")

finally:
    # Close the browser
    driver.quit()
''')
    print(f"Script saved to {random_filename}")

finally:
    # Close the browser
    driver.quit()
