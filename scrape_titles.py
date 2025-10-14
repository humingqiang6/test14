import requests
from bs4 import BeautifulSoup
import random
import string

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
            return "No title found"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    """Main function to demonstrate scraping."""
    # Example URL
    url = 'https://httpbin.org/html'  # A test page that usually has a title

    title = scrape_page_title(url)
    if title:
        print(f"Title of {url} is: {title}")
    else:
        print(f"Could not scrape the title from {url}")

if __name__ == "__main__":
    main()