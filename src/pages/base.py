import urwid
from typing import Optional


# Make sure every page has a main widget to load
class BasePage:
    main_widget: Optional[urwid.Widget] = None

    def get_main_widget(self) -> Optional[urwid.Widget]:
        return self.main_widget
