import requests  # type: ignore
from bs4 import BeautifulSoup

from src.scrapers.base import BaseScraper


class PapersWithCode(BaseScraper):
    def __init__(self, url: str):
        super(PapersWithCode, self).__init__(url)
        self.url = url
        pass

    def scrape(self):
        html = BeautifulSoup(requests.get(self.url).text, "html.parser")
        print(html)
        pass


if __name__ == "__main__":
    test = PapersWithCode(url="https://www.paperswithcode.com")
    test.scrape()
