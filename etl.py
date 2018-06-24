import bonobo
import requests
from bs4 import BeautifulSoup

# scrape coolblue to know the price of a particular headphone
def scrape_coolblue():
    price = ''
    status = ''
    url = 'https://www.coolblue.be/nl/product/788941/bose-quietcomfort-35-ii-wireless-zwart.html'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text.strip()
        soup = BeautifulSoup(html, 'lxml')
        price_status_section = soup.select('.sales-price--current')
        if len(price_status_section) > 1:
            price = price_status_section[1].text.strip()
    return price

# scrape bol to know the price of a particular headphone
def scrape_bol():
    price = ''
    status = ''
    url = 'https://www.bol.com/nl/p/bose-quietcomfort-35-serie-ii-draadloze-koptelefoon-zwart/9200000081129317/?country=BE'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text.strip()
        soup = BeautifulSoup(html, 'lxml')
        price_section = soup.find('span', {'class': 'promo-price'})
        if price_section:
            price = price_section.text.strip()
    return price

# call the scrape functions
def extract():
    yield scrape_coolblue()
    yield scrape_bol()

# transform the data into the right format 
def transform(price: str):
    t_price = price.replace(',', '').replace('-', '')
    print(t_price)
    return float(t_price)

# store the data in txt file
def load(price: float):
    with open('pricing.txt', 'a+', encoding='utf8') as f:
        f.write((str(price) + '\n'))

if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'referrer': 'https://google.com'
    }

    graph = bonobo.Graph(
        extract,
        transform,
        load,
    )
    bonobo.run(graph)