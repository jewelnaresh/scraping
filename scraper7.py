from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def get_links(articleUrl):
    html = urlopen(f"http://en.wikipedia.org{articleUrl}")
    bs = BeautifulSoup(html.read(), 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

    
    # return bs.find_all(lambda tag: 'href' in tag.attrs and re.compile('^(/wiki/)((?!:).)*$').search(tag.attrs['href']))

links = get_links('/wiki/Kevin_Bacon')
while len(links) > 0 :
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = get_links(newArticle)