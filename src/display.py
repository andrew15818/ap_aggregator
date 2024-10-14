import urwid
from urwid import Align
from typing import List, Tuple, Dict


class DisplayManager:
    """
    Defines look of different windows, starts main loop.
    """

    def __init__(self):
        pass

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
        button1 = urwid.Button("Feed", align=Align.CENTER)
        streak2 = urwid.AttrMap(button1, "streak")

        for item in (outside, inside, streak, streak2):
            pile.contents.append((item, pile.options()))

        loop.run()
