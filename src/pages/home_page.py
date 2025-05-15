from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Optional, Tuple

import urwid

from src.pages.base import BasePage


class WidgetFactory(ABC):
    """
    Provides interface for all types of widgets in our app.
    """

    @abstractmethod
    def create_widget(self, *args, **kwargs) -> urwid.Widget:
        """
        Includes logic to create each child class.
        """
        pass


class ButtonFactory(WidgetFactory):
    """
    Create a button, its label, and tie it to a cletteallback function.
    """

    def create_widget(
        self,
        label: str,
        on_press: Optional[Callable],
        align: Optional[str] = "center",
        attr: Optional[str] = "streak",
    ) -> urwid.Widget:
        """
        Create a button with given label that executes on_press when pressed.
        If the on_press is set, create a connection to the function.
        Args:
            label (str): value to display on the button
            on_press (callable): function to execute on press.
            align (str): alignment on the screen.
            attr (str): Style attribute to attach
        """
        button = urwid.Button(label=label, on_press=on_press, align=align)

        if on_press is not None:
            urwid.connect_signal(button, "click", on_press)

        return urwid.AttrMap(button, attr)


class TextFactory(WidgetFactory):
    """
    Wrapper around the creation of the Text widget.
    """

    def create_widget(
        self,
        text: Optional[str],
        style: Optional[str],
        align: Optional[str] = "center",
        attr: str = "banner",
    ) -> urwid.AttrMap:
        return urwid.AttrMap(urwid.Text((text, style), align), attr)


class SolidFillFactory:
    """
    Wrapper around the SolidFill widget.
    """

    def create_widget(
        self,
    ) -> urwid.AttrMap:
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
        self,
        label: str = "",
        on_press: Optional[Callable] = None,
        align: str = "center",
    ) -> urwid.AttrMap:
        return self.button_factory.create_widget(label, on_press, align)

    def create_text(
        self,
        style: str = "banner",
        text: str = "",
        align: str = "center",
        attr: str = "",
    ) -> urwid.AttrMap:
        return self.text_factory.create_widget(style, text, align, attr)


class HomePage(BasePage, urwid.WidgetWrap):
    """
    Defines look of main screen, starts main loop.
    """

    def __init__(self, go_to_feed: Callable):
        super().__init__(urwid.SolidFill())

    def exit(self, key: str) -> None:
        """
        Terminate the program if the specific key is pressed
        """
        if key in {"q", "Q"}:
            raise urwid.ExitMainLoop()

    def _format_palette(
        self, palette_conf: Optional[List[Dict]] = None
    ) -> List[Tuple[str, ...]]:
        """
        Format the palette yaml configs into a list of tuples to be recognized by urwid.
        Args:
            palette (list[dict]): display attribute names and colors as set in configs.
        Returns:
            List(tuple) containing the color settings.
        """
        palette: List[Tuple[str, ...]] = []
        if palette_conf is None:
            return [tuple("")]
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

    def display(self, palette: List[Dict]) -> None:
        """
        Starts main loop and displays initial splash screen.
        """
        # TODO: Rewrite the function while declaring a main widget
        pass
