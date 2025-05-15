import urwid

from src.scrapers.base import BaseResponse
from src.feed import Feed
from src.pages.base import BasePage


class FeedListItem:
    """
    Format the item to be displayed as list of text widgets
    """

    def __init__(self, response: BaseResponse) -> None:
        self.response = response

    def as_widget(self) -> urwid.Pile:
        """
        Display each item as some text columns and separators
        """

        columns = urwid.Columns(
            [
                urwid.Text(self.response.title),
                urwid.Text(self.response.link),
                urwid.Text(", ".join(self.response.authors)),
            ]
        )
        return urwid.Pile([columns, urwid.AttrMap(urwid.Divider("-"), "bold")])


class FeedPage(urwid.WidgetWrap, BasePage):
    """
    Queries the feed items and displays them.
    """

    def __init__(self):
        """
        Create the listbox item for each of the fetched articles
        """
        self.feed_items = self._get_feed_items()
        self.banner = urwid.Columns(
            [urwid.Text("Title"), urwid.Text("Link"), urwid.Text("Authors")]
        )
        self.listbox = urwid.ListBox(
            urwid.SimpleFocusListWalker(
                FeedListItem(w).as_widget() for w in self.feed_items
            )
        )
        self.header = self.create_column_header()
        self.main_widget = urwid.Pile(
            [
                ("pack", self.header),
                ("pack", urwid.Divider("+")),
                ("weight", 1, self.listbox),
            ]
        )

        super().__init__(urwid.AttrMap(self.main_widget, "foreground"))

        self.loop = urwid.MainLoop(
            self.main_widget, None, unhandled_input=self.keypress
        )
        self.loop.run()

    def get_widget(self) -> urwid.Widget:
        """
        Get the main widget for changing screen.
        """
        return self.main_widget

    def keypress(self, key: str) -> None:
        if key in {"q", "Q"}:
            raise urwid.ExitMainLoop()

    def create_column_header(self) -> urwid.Columns:
        columns = [
            urwid.AttrMap(urwid.Text("Title"), "header_label"),
            urwid.AttrMap(urwid.Text("Link"), "header_label"),
            urwid.AttrMap(urwid.Text("Authors"), "header"),
        ]

        return urwid.Columns(columns)

    def _get_feed_items(self) -> list[BaseResponse]:
        """
        Initialize the feed object and query the items
        """
        self.feed = Feed()
        ret = self.feed.init_scrapers()
        return ret


if __name__ == "__main__":
    listBox = FeedPage()
