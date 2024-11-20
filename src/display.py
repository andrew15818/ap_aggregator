from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Callable, Optional

import urwid


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
    Create a button, its label, and tie it to a callback function.
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
        Args:
            label (str): value to display on the button
            on_press (callable): function to execute on press.
            align (str): alignment on the screen.
            attr (str): Style attribute to attach
        """
        return urwid.AttrMap(
            urwid.Button(label=label, on_press=on_press, align=align), attr
        )


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


class HomePage:
    """
    Defines look of main screen, starts main loop."""

    def __init__(self):
        self.gui_creator = GUICreator()

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
        _palette = self._format_palette(palette)
        placeholder = urwid.SolidFill()

        loop = urwid.MainLoop(placeholder, _palette, unhandled_input=self.exit)
        loop.screen.set_terminal_properties(colors=256)
        loop.widget = urwid.AttrMap(placeholder, "bg")
        loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

        div = urwid.Divider()
        outside = urwid.AttrMap(div, "outside")
        inside = urwid.AttrMap(div, "inside ")
        txt = self.gui_creator.create_text(
            style="banner",
            text="Andres Ponce's everything scraper",
            align="center",
            attr="banner",
        )
        pile = loop.widget.base_widget
        button1 = self.gui_creator.create_button("Feed", align="center")
        for item in (outside, inside, txt, button1, inside, outside):
            try:
                pile.contents.append((item, pile.options()))
                print(f"Going once...{type(item)}")
            except Exception as e:
                print(type(item))
                print(f"Errorsito: {e}")
                continue

        loop.run()
