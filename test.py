from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def open_site(url):
    html = urlopen(url)
    return BeautifulSoup(html.read(), 'html.parser')

def get_title(linkurl):
    bs = open_site(linkurl)
    links = bs.find_all('a', href=re.compile('^(../Jobs)/View/[0-9]*$'))
    next = bs.find('a', {'class': 'next'})

    for link in links:
        new = open_site('https://xpress.jobs'+link.attrs['href'][2:])
        print(new.find('h1', {'class': 'page-title'}).get_text())
        print('-'*30)

    get_title('https://xpress.jobs'+next.attrs['href'])

get_title('https://xpress.jobs/jobs')

html = urlopen('http://topjobs.lk/')
bs = BeautifulSoup(html.read(), 'html.parser')

modules = bs.findAll('div', {'class': 'module'})

for module in modules:
    titles = module.findAll('div')
    for title in titles:
        print(title.h5.get_text())
        print(title.span.a.get_text())
        print('-'*30)