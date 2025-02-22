from abc import ABC
from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    Uniform format for individual item retrieved from scraped site.
    """

    title: str = "Placeholder title"
    content: str = "Placeholder content"
    link: str = "https://example.com"
    authors: list = ["Andres Ponce"]


class BaseResponses(BaseModel):
    """
    Collection of responses from scraper.
    """

    contents: list[BaseResponse]


class BaseScraper(ABC):
    def __init__(self, url: str):
        self.url = url

    def scrape(self):
        """
        Scrape the website for relevant article links,
        return the properly formatted data for the feed parser.
        """
        pass
