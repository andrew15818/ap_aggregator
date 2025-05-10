import urwid
from typing import Optional


# Make sure every page has a main widget to load
class BasePage:
    main_widget: Optional[urwid.Widget] = None
