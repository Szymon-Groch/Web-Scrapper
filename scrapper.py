import requests
from bs4 import BeautifulSoup

# url
url = 'https://books.toscrape.com/'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# target - prices
product_price_divs = soup.find_all('div', class_='product_price')

# Extract and print the content of each div
for div in product_price_divs:
    print(div.text.strip())

