import urwid


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
        super().__init__(urwid.Frame(urwid.ListBox(feed_items)))
        pass

    def get_data_sources(self, path: str = "tu_madre.yaml") -> None:
        """
        Get the data sources from which we are to display items.
        """
        pass

    def display(self) -> None:
        # TODO: Get the actual sources
        # Content sources
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
