import requests  # type: ignore
from bs4 import BeautifulSoup

from src.scrapers.base import BaseScraper, BaseResponse, BaseResponses


class PapersWithCodeScraper(BaseScraper):
    def __init__(self, url: str):
        super(PapersWithCodeScraper, self).__init__(url)
        self.url = url
        self.html = BeautifulSoup(
            requests.get(self.url).text,
            "html.parser",
        )

    def scrape(self) -> BaseResponses:
        """
        Scrape and format the response from PapersWithCode HTML.
        """
        try:
            papers_html = self.html.find(class_="home-page").find_all(
                class_="item-content"
            )
            for paper in papers_html:
                title_info = paper.find("h1").find("a")
                title = title_info.contents[0]
                link = (
                    self.url + title_info["href"]
                )  # Only link relative to homepage is returned
                print(f"Title: {title}, link: {link}")

                break
            return BaseResponses([BaseResponse()])
        except Exception as e:
            raise Exception(f"Could not parse PapersWithCode with error {e}")


if __name__ == "__main__":
    test = PapersWithCodeScraper(url="https://www.paperswithcode.com")
    test.scrape()
