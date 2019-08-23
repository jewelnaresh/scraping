from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def get_links(pageUrl):
    global pages
    html = urlopen(f'http://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html.read(), 'html.parser')

    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find('p').get_text())
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print("Something is missing! Continuing")

    for link in bs.find_all('a', {'href': re.compile('^/wiki/')}):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("-"*20)
                print(newPage)
                pages.add(newPage)
                get_links(newPage)

get_links('')
