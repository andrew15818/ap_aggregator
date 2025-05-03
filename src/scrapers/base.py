from abc import ABC, abstractmethod
from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    Uniform format for individual item retrieved from scraped site.
    """

    title: str = "Placeholder title"
    content: str = "Placeholder content"
    link: str = "https://example.com"
    authors: list = ["Andres Ponce"]

    def __str__(self) -> str:
        return f"Title: {self.title} Link: {self.link} Authors: {self.authors} Content: {self.content}"

    def get_items(self) -> list[str | list[str]]:
        return [self.title, self.content, self.link]  # , self.authors]


class BaseResponses(BaseModel):
    """
    Collection of responses from scraper.
    """

    contents: list[BaseResponse]

    def get_contents(self) -> list[BaseResponse]:
        return self.contents


class BaseScraper(ABC):
    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def scrape(self) -> BaseResponses:
        """
        Scrape the website for relevant article links,
        return the properly formatted data for the feed parser.
        """
        return BaseResponses(contents=[BaseResponse()])
