from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple

import urwid
from urwid import Align


class WidgetFactory(ABC):
    """
    Provides interface for all types of widgets in our app.
    """

    @abstractmethod
    def create_widget(self):
        """
        Includes logic to create each child class.
        """
        pass


class ButtonFactory(WidgetFactory):
    """
    Create a button, its label, and tie it to a callback function.
    """

    def create_widget(
        self, label: str, on_press: Optional[callable], align: str = "center"
    ):
        """
        Create a button with given label that executes on_press when pressed.
        Args:
            label (str): value to display on the button
            on_press (callable): function to execute on press.
            align (str): alignment on the screen.
        """
        return urwid.Button(label=label, on_press=on_press, align=align)


class TextFactory(WidgetFactory):
    def create_widget(style: str, text: str, align: str = "center"):
        return urwid.Text(style, text, align)


class SolidFillFactory:
    def create_widget(
        self,
    ):
        pass


class GUICreator:
    """
    Class that actually creates the widget objects.
    """

    def __init__(self):
        self.button_factory = ButtonFactory()
        self.text_factory = TextFactory()
        self.solidfill_factory = SolidFillFactory()

    def create_button(
        self, label: str = "", on_press: callable = None, align: str = "center"
    ):
        return self.button_factory.create_widget(label, on_press, align)


class DisplayManager:
    """
    Defines look of different windows, starts main loop.
    """

    def __init__(self):
        self.gui_creator = GUICreator()

    def exit(self, key: str) -> None:
        """
        Terminate the program if the specific key is pressed
        """
        if key in {"q", "Q"}:
            raise urwid.ExitMainLoop()

    def _format_palette(self, palette_conf: List[Dict] = None) -> List[Tuple]:
        """
        Format the palette yaml configs into a list of tuples to be recognized by urwid.
        Args:
            palette (list[dict]): display attribute names and colors as set in configs.
        Returns:
            List(tuple) containing the color settings.
        """
        palette = []
        if palette_conf is None:
            palette_conf = []
        for item in palette_conf:
            palette.append(
                (
                    item.get("name", "tmp"),
                    item.get("foreground", ""),
                    item.get("background", ""),
                    item.get("mono", ""),
                    item.get("foreground_high", ""),
                    item.get("background_high", ""),
                )
            )
        return palette

    def start(self, palette: list[dict]) -> None:
        """
        Starts main loop and displays initial splash screen.
        """
        palette = self._format_palette(palette)
        placeholder = urwid.SolidFill()

        loop = urwid.MainLoop(placeholder, palette, unhandled_input=self.exit)
        loop.screen.set_terminal_properties(colors=256)
        loop.widget = urwid.AttrMap(placeholder, "bg")
        loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

        div = urwid.Divider()
        outside = urwid.AttrMap(div, "outside")
        inside = urwid.AttrMap(div, "inside ")
        txt = urwid.Text(
            ("banner", "Andres Ponce's everything scraper"), align="center"
        )
        streak = urwid.AttrMap(txt, "banner")
        pile = loop.widget.base_widget
        button1 = self.gui_creator.create_button("Feed", align=Align.CENTER)
        streak2 = urwid.AttrMap(button1, "streak")

        for item in (outside, inside, streak, streak2):
            pile.contents.append((item, pile.options()))

        loop.run()
