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

    def __init__(self, name, initialUrl, jobTag, companyTag, jobUrlTag):
        self.name = name
        self.initialUrl = initialUrl
        self.jobTag = jobTag
        self.companyTag = companyTag
        self.jobUrlTag = jobUrlTag

import requests
from bs4 import BeautifulSoup

class Crawler:

    def get_page(self, initialUrl):
        try:
            req = requests.get(initialUrl)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    
    def get_data(self,pageObject, selector):
        childObject = pageObject.select(selector)
        # print(childObject)
        if childObject is not None and len(childObject) > 0:
            if 'a' in selector:
                return 'https://xpress.jobs/jobs/' + childObject[0].attrs['href']
            return childObject[0].get_text()
        return ""

    def find(self, site):
        bs = self.get_page(site.initialUrl)

        job = self.get_data(bs, site.jobTag)
        company = self.get_data(bs, site.companyTag)
        jobUrl = self.get_data(bs, site.jobUrlTag)

        data = Data(job, company, jobUrl)
        data.print()

crawler = Crawler()

siteData = [
    ['Xpress', 'https://xpress.jobs/jobs', 'h3.job_listing-title', 'strong', 'a.job_listing-clickbox'],
    ['Topjobs', 'http://topjobs.lk/','span.job-link a', 'div.h5', 'a']
]

sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4]))

for site in sites:
    crawler.find(site)