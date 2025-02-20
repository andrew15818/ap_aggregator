from abc import ABC


class BaseScraper(ABC):
    def __init__(self, url: str):
        self.url = url

    def scrape(self):
        """
        Scrape the website for relevant article links
        """
        pass
