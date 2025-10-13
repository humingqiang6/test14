import random
import string
from bs4 import BeautifulSoup
import requests

def scrape_page_title(url):
    """Scrapes the title from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.get_text(strip=True)
        else:
            return "No title tag found"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while parsing {url}: {e}")
        return None

def save_title_to_file(title, filename):
    """Saves the scraped title to a specified file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(title)
        print(f"Title saved to {filename}")
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")

def generate_random_filename(extension=".py"):
    """Generates a random filename with a given extension."""
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"scraped_title_{random_string}{extension}"

if __name__ == "__main__":
    url = "https://httpbin.org/html"  # Example URL that returns HTML
    title = scrape_page_title(url)
    if title:
        filename = generate_random_filename()
        save_title_to_file(title, filename)
    else:
        print("Failed to scrape the title.")
