from src.scrapers.base import BaseScraper


class XScraper(BaseScraper):
    """
    Since this site requires user login, we have to authenticate to retrieve posts.
    Scrape contents from X for a given user.
    """

    def __init__(self):
        pass

    def authenticate(self):
        pass
