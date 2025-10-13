import requests
from bs4 import BeautifulSoup
import random
import string

def scrape_page_title(url):
  """Scrapes the title from a given URL."""
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.content, 'html.parser')
    title_tag = soup.find('title')
    if title_tag:
      return title_tag.get_text(strip=True)
    else:
      return "No title found"
  except requests.exceptions.RequestException as e:
    print(f"Error fetching {url}: {e}")
    return None

if __name__ == "__main__":
  # Example URL, replace with the target URL
  target_url = "https://httpbin.org/html" 
  title = scrape_page_title(target_url)

  if title:
    print(f"Title of {target_url}: {title}")
    # Generate a random filename
    random_filename = "scraped_titles_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".py"
    print(f"Saving title to {random_filename}...")
    with open(random_filename, 'w') as f:
      f.write(f"# Scraped title from {target_url}\n")
      f.write(f"title = '''{title}'''\n")
    print(f"Title saved successfully to {random_filename}")
  else:
    print("Failed to scrape the title.")
