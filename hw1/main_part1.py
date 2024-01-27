import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Set the total number of items you want to scrape
total_items = 1000

# List to store data
data = []

# Start scraping from the first page
page = 1


while len(data) < total_items:
    url = f"https://www.etsy.com/c/pet-supplies/pet-clothing-accessories-and-shoes?ordering_strategy_key=Search2_CategoryPages_TaxonomyOrdering_Gms&explicit=1&ref=pagination&page={page}"
    
    # Make an HTTP GET request to the URL
    html = session.get(url, headers=headers)

    if html.status_code == 200:

        # Parse the HTML content of the page
        soup = BeautifulSoup(html.text, 'html.parser')

        # Extract relevant content elements using BeautifulSoup
        content_product = soup.find_all('h3', class_='wt-text-caption v2-listing-card__title wt-text-truncate')
        content_review = soup.find_all('span', class_='wt-text-caption wt-text-gray wt-display-inline-block wt-nudge-l-3 wt-pr-xs-1')
        content_price = soup.find_all('span', class_='currency-value')

        for name, reviews, price in zip([name.text for name in content_product], [reviews.text for reviews in content_review], [price.text for price in content_price]):
            review_count = re.search(r'\d+', reviews).group()
            data.append([name, review_count, price])
        print(page)
        page += 1

    else:
        print(f'Error on page {page}. Response code: {html.status_code}')
        break

# Create DataFrame
df = pd.DataFrame(data, columns=['Product', 'Review', 'Price'])

# Save to csv
df.to_csv('result.csv', index=False)

print("Complete!")




