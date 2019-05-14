import requests
from bs4 import BeautifulSoup

def spider(mp):
    page = 1
    while page < mp:
        url = 'http://nathantrodgers.pythonanywhere.com/'
        source_code = requests.get(url)
        source_text = source_code.text
        extracted_txt = BeautifulSoup(source_text)
            for link in extracted_txt.findAll('a', {'class': 'item_name'}):
                href = link.get('hred')
                print(href)

spider(1)
            