from src.scrapers.base import BaseResponses, BaseResponse
from src.scrapers.paperswithcode import PapersWithCodeScraper
from src.scrapers.arxiv import ArxivScraper


class Feed:
    """
    Initialize and trigger the scrapers.
    """

    def __init__(self):
        # TODO: More flexible init system, read from configs
        self.scrapers = [ArxivScraper, PapersWithCodeScraper]

    def init_scrapers(self) -> list[BaseResponse]:
        scraper_responses = []
        for scraper in self.scrapers:
            for response in scraper().scrape().get_contents():
                scraper_responses.append(response)
        return BaseResponses(contents=scraper_responses).contents


if __name__ == "__main__":
    feed = Feed()
    feed.init_scrapers()
