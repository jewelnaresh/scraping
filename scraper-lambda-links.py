from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(), 'html.parser')

links = bs.find_all(lambda tag: 'href' in tag.attrs)
for link in links:
    print(link.attrs['href'])