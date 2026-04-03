"""Common utilities for the PyRef project."""

__version__ = "0.1.0"
__all__ = ["red", "green", "yellow", "blue", "cyan", "magenta", "grey", "white"]

from enum import Enum

import termcolor


class _TextColor(Enum):
    BLUE = "blue"
    CYAN = "cyan"
    GREEN = "green"
    GREY = "grey"
    MAGENTA = "magenta"
    RED = "red"
    WHITE = "white"
    YELLOW = "yellow"


class _TextFormatter:
    """A class containing methods for formatting text with colors and styles."""

    def __init__(self, color: _TextColor):
        """Initializes the TextFormatter class."""
        self._color = color

    def __call__(self, text: str, bold: bool = False, underline: bool = False) -> str:
        """Formats the text with the specified color and styles."""
        attrs = []
        if bold:
            attrs.append("bold")
        if underline:
            attrs.append("underline")
        return termcolor.colored(text, self._color.value, attrs=attrs)

    def bold(self, text: str) -> str:
        """Formats the text with the specified color and bold style."""
        return self(text, bold=True)

    def head(self, text: str) -> str:
        """Formats the text with the specified color, bold and underline styles."""
        return self(text, bold=True, underline=True)

    @property
    def color(self):
        """Returns the color of the text."""
        return self._color


red = _TextFormatter(_TextColor.RED)
green = _TextFormatter(_TextColor.GREEN)
yellow = _TextFormatter(_TextColor.YELLOW)
blue = _TextFormatter(_TextColor.BLUE)
cyan = _TextFormatter(_TextColor.CYAN)
magenta = _TextFormatter(_TextColor.MAGENTA)
grey = _TextFormatter(_TextColor.GREY)
white = _TextFormatter(_TextColor.WHITE)
