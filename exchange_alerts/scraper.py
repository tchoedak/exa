from bs4 import BeautifulSoup
import requests


def find_exchange_rate(page):
    soup = BeautifulSoup(page.content)
    results = soup.find_all('span', {'class': 'ccOutputRslt'})
    if results:
        return results[0].text


def extract_value(scraped_result):
    return float(scraped_result.split()[0])


def extract_currency(scraped_result):
    return scraped_result.split()[1]


class Result(object):

    def __init__(self, url):
        self.page = requests.get(url.url)
        self.result = find_exchange_rate(self.page)
        self.value = extract_value(self.result)
        self.url = url


    def __repr__(self):
        return f'1 \033[32m{self.url.from_} : \033[33m{self.value} {self.url.to}'


    def __str__(self):
        return f'1 {self.url.from_} : {self.value} {self.url.to}'
