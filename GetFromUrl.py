from bs4 import BeautifulSoup
from requests import get
import urllib3
import Cleaners
urllib3.disable_warnings()


class GetUrlText:
    def __init__(self, url):
        self.url = url

    def action(self):
        soup = BeautifulSoup(get(self.url,
                                 verify=False).text,
                             'html.parser')
        return ' '.join([str(i.string).lower() for i in soup.find_all('p')])


class GetUrlTextsMass:
    def __init__(self, *urls):
        self.urls = urls

    def action(self):
        return map(lambda i: GetUrlText(i).action(), self.urls)


class GetCleanUrlText:
    def __init__(self, url):
        self.url = url

    def action(self):
        soup = BeautifulSoup(get(self.url,
                                 verify=False).text,
                             'html.parser')
        return ' '.join(map(lambda i: Cleaners.HTMLCleaner((str(i.text)).lower()).action(), soup.find_all('p')))
