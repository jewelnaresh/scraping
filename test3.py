class Data:

    def __init__(self, job, company, jobUrl):
        self.job = job
        self.company = company
        self.jobUrl = jobUrl

    def print(self):
        print(self.job)
        print(self.company)
        print(self.jobUrl)


class Website:

    def __init__(self, name, initialUrl, jobTag, companyTag, jobUrlTag, jobUrlRegex, nextTag, nextLink):
        self.name = name
        self.initialUrl = initialUrl
        self.jobTag = jobTag
        self.companyTag = companyTag
        self.jobUrlTag = jobUrlTag
        self.jobUrlRegex = jobUrlRegex
        self.nextTag = nextTag
        self.nextLink = nextLink

import requests
from bs4 import BeautifulSoup
import re

class Crawler:

    def get_page(self, initialUrl):
        try:
            req = requests.get(initialUrl)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    
    def get_data(self, pageObject, selector):
        childObject = pageObject.select(selector)
        if childObject is not None and len(childObject) > 0:
            return childObject
        return ""

    def get_url(self, pageObject, initialUrl, selector, urlRegex):
        urls = pageObject.select(selector)
        newUrls=[]
        for url in urls:
            try:
                url = newUrls.append(initialUrl + re.search(urlRegex, url.attrs['href']).group(0))
            except AttributeError:
                url = ''
        return newUrls

    def find(self, site):
        bs = self.get_page(site.nextLink)

        jobs = self.get_data(bs, site.jobTag)
        company = self.get_data(bs, site.companyTag)
        jobUrl = self.get_url(bs, site.initialUrl, site.jobUrlTag, site.jobUrlRegex)

        for i in range(len(jobs)):
            data = Data(jobs[i].get_text(), company[i].get_text(), jobUrl[i])
            data.print()
        
        previous = "previous"
        next = "next"

        while next!=previous:
            try:
                next = self.get_data(bs, site.nextTag)[0]
            except IndexError:
                break
            site.nextLink = site.initialUrl + next.attrs['href'][5:]
            self.find(site)
            previous = next

crawler = Crawler()

siteData = [
    # ['Xpress', 'https://xpress.jobs/jobs', 'h3.job_listing-title', 'div.job_listing-company a strong', 'a.job_listing-clickbox[href*="/View/"]', '(/View/).*', 'a.next','https://xpress.jobs/Jobs/Sector/it' ],
    ['Topjobs', 'http://topjobs.lk/','td h2 a', 'td h1','td h2 a', '(employer).*(.jsp)','no-value-available','http://topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA=SDQ&jst=OPEN']
]

sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7]))

for site in sites:
    crawler.find(site)