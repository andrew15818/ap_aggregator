import urwid

from src.scrapers.base import BaseResponses, BaseResponse
from src.feed import Feed


class FeedListItem:
    """
    Format the item to be displayed as list of text widgets
    """

    def __init__(self, response: BaseResponse) -> None:
        self.response = response
        print(self.response)

    def as_widget(self) -> list[urwid.Text]:
        print(self.response.get_items())

        return [urwid.Text(t) for t in self.response.get_items()]


class FeedListBox(urwid.ListBox):
    """
    Queries the feed items and displays them.
    """

    def __init__(self):
        # TODO: Update to display the actual fetched items.
        self.feed_items = self._get_feed_items()
        self.listbox = urwid.ListBox(
            urwid.SimpleListWalker(
                urwid.Columns(FeedListItem(w).as_widget()) for w in self.feed_items
            )
        )
        self.main = urwid.Frame(self.listbox)

        # TODO: Get rid of this for real testing
        self.loop = urwid.MainLoop(self.main, None)
        self.loop.run()
        pass

    def _get_feed_items(self) -> BaseResponses:
        """
        Initialize the feed object and query the items
        """
        self.feed = Feed()
        ret = self.feed.init_scrapers()
        print(ret)
        return ret


class FeedPage(urwid.WidgetWrap):
    """
    Creates the feed page based on the scraper contents.
    """

    def __init__(self) -> None:
        # Create feed items
        feed_items = [
            urwid.Text("Feed Item 1"),
            urwid.Text("Feed Item 2"),
            urwid.Divider(),
            urwid.Button("Back to Menu"),
        ]
        self.main_widget = urwid.ListBox(urwid.ListBox(feed_items))
        super().__init__(urwid.Frame(urwid.ListBox(feed_items)))
        pass

    def get_data_sources(self, path: str = "default.yaml") -> None:
        """
        Get the data sources from which we are to display items.
        """
        pass

    def display(self) -> None:
        # TODO: Get the actual sources
        # Content sources
        feed = Feed()
        print(feed.init_scrapers())
        source_buttons = []
        for i in range(10):
            button = urwid.AttrMap(
                urwid.Button(str(i), on_press=None, user_data=str(i)),
                None,
                focus_map="reversed",
            )
            source_buttons.append(button)
        sources_list = urwid.ListBox(urwid.SimpleFocusListWalker(source_buttons))

        article_items = []
        for i in range(10):
            article_items.append(
                urwid.Pile(
                    [
                        urwid.AttrMap(
                            urwid.Text("I'm just happy to be here :D", "center"), "bold"
                        )
                    ]
                )
            )
        articles_list = urwid.ListBox(urwid.SimpleFocusListWalker(article_items))
        columns = urwid.Columns(
            [("weight", 20, sources_list), ("weight", 80, articles_list)]
        )
        return urwid.AttrMap(urwid.Frame(columns), "bg")


if __name__ == "__main__":
    listBox = FeedListBox()
