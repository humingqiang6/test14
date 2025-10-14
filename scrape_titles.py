#!/usr/bin/env python3
"""
A simple web scraper to extract and print the title of a given webpage.
"""

import requests
from bs4 import BeautifulSoup

def scrape_page_title(url):
    """
    Scrapes the title from the given URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The title of the webpage, or an error message.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')

        if title_tag:
            return title_tag.get_text(strip=True)
        else:
            return "Title tag not found."

    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the URL: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    # Example URL, replace with the target URL
    target_url = "https://www.python.org"
    title = scrape_page_title(target_url)
    print(f"The title of the page '{target_url}' is: {title}")