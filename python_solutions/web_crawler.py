import requests
from bs4 import BeautifulSoup

def spider(mp):
    page = 1
    while page < mp:
        url = 'http://nathantrodgers.pythonanywhere.com/'
        source_code = requests.get(url)
        plain_text = source_code.text
        