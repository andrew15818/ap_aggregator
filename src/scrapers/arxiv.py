import requests  # type: ignore
from src.scrapers.base import BaseResponse, BaseResponses, BaseScraper
import urllib.request as libreq  # type: ignore
import feedparser  # type: ignore


class ArxivScraper(BaseScraper):
    def __init__(self, url: str = "http://export.arxiv.org/api/query?"):
        super(ArxivScraper, self).__init__(url)
        self.url = url
        self.query = "search_query=cat:cs.CV+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.AI+OR+cat:cs.NE+OR+cat:cs.RO"  # Query for these categories
        self.query += "&start=0&max=10"
        self.final_url = f"{self.url}{self.query}"
        self.feed = None

        print(f"Querying: {self.final_url}")
        response = requests.get(
            self.final_url,
        )
        with libreq.urlopen(self.final_url) as url:
            response = url.read()  # type: ignore

        if url.status == 200:  # type: ignore
            self.feed = feedparser.parse(response)  # type: ignore
        else:
            print(f"Error querying {self.final_url}")

    def scrape(self) -> BaseResponses:
        if not self.feed:
            raise Exception(f"Could not parse url {self.final_url}")

        responses = []
        for item in self.feed.entries:
            response = BaseResponse(
                title=item["title"].replace("\n", ""),
                content=item.title_detail["value"],
                link=item["link"],
                authors=[n["name"] for n in item.authors],
            )
            # print(response.title)
            responses.append(response)

        return BaseResponses(contents=responses)


if __name__ == "__main__":
    url = "http://export.arxiv.org/api/query?"
    scraper = ArxivScraper(url=url)
    scraper.scrape()
