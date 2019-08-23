from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def get_data(url):
    html = urlopen('https://xpress.jobs/'+url)
    bs = BeautifulSoup(html.read(), 'html.parser')

    links = bs.find_all('a', href=re.compile('^(../Jobs)/View/[0-9]*$'))
    next = bs.find('a', {'class': 'next'})
    for link in links:
       print(link.parent.find('h3').get_text())
       print(link.parent.find('div', {'class': 'job_listing-company'}).a.get_text())
       print('https://xpress.jobs/' + link.attrs['href'])
       print('-'*30)

    get_data(next.attrs['href'])

get_data('jobs') 