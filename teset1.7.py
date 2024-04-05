'''
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup
'''
'''
from bs4 import BeautifulSoup
import requests
 
url = "http://www.w3schools.com/php/demo_intro.php"
 
istek = requests.get(url)
html = istek.content
 
print(html)
'''
'''
def get_soup(TARGET_URL):
    page = requests.get(TARGET_URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

URL = 'https://bilative.github.io/sisterslab/web_scraping'

soup = get_soup(URL)
'''