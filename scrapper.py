import requests
from bs4 import BeautifulSoup

# URL
url = 'https://books.toscrape.com/'
response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    #prices
    product_price_divs = soup.find_all('div', class_='product_price')

    #book titles
    h3_tags = soup.find_all('h3')


    combined_content = []

    #Extracting found element together for printing
    for h3 in h3_tags:
        combined_content.append(f"Heading: {h3.text.strip()}")


    for div in product_price_divs:
        combined_content.append(f"Product Price: {div.text.strip()}")

    #Print 
    for content in combined_content:
        print(content)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
