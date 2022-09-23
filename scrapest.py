from csv import writer
from email import header
import encodings
from bs4 import BeautifulSoup
import requests
from csv import writer


url = 'https://www.pararius.com/apartments/'
pages = requests.get(url)

soup = BeautifulSoup(pages.content, 'html.parser')
lists = soup.find_all('section', class_ = 'listing-search-item')

with open('housing.csv', 'w', encoding = 'UTF-8', newline = '' ) as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)


    for list in lists:
        title = list.find('a', class_ = 'listing-search-item__link listing-search-item__link--title').text.replace('\n', '')
        location = list.find('div', class_ = 'listing-search-item__sub-title').text.replace('\n', '')
        price = list.find('div',class_ = 'listing-search-item__price').text.replace('\n', '')
        area = list.find('li', class_ = 'illustrated-features__item illustrated-features__item--surface-area').text.replace('\n', '')
        info = [title, location, price, area]
        thewriter.writerow(info)

 
