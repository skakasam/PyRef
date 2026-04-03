"""Color utility functions for terminal text formatting."""

import termcolor


def as_re(text: str):
    """Returns the text colored in red."""
    return termcolor.colored(text, "red")


def as_re_bl(text: str):
    """Returns the text colored in red and bold."""
    return termcolor.colored(text, "red", attrs=["bold"])


def as_re_ul(text: str):
    """Returns the text colored in red and underlined."""
    return termcolor.colored(text, "red", attrs=["underline"])


def as_re_bu(text: str):
    """Returns the text colored in red, bold and underlined."""
    return termcolor.colored(text, "red", attrs=["bold", "underline"])


def as_gr(text: str):
    """Returns the text colored in green."""
    return termcolor.colored(text, "green")


def as_gr_bl(text: str):
    """Returns the text colored in green and bold."""
    return termcolor.colored(text, "green", attrs=["bold"])


def as_gr_ul(text: str):
    """Returns the text colored in green and underlined."""
    return termcolor.colored(text, "green", attrs=["underline"])


def as_gr_bu(text: str):
    """Returns the text colored in green, bold and underlined."""
    return termcolor.colored(text, "green", attrs=["bold", "underline"])


def as_ye(text: str):
    """Returns the text colored in yellow."""
    return termcolor.colored(text, "yellow")


def as_ye_bl(text: str):
    """Returns the text colored in yellow and bold."""
    return termcolor.colored(text, "yellow", attrs=["bold"])


def as_ye_ul(text: str):
    """Returns the text colored in yellow and underlined."""
    return termcolor.colored(text, "yellow", attrs=["underline"])


def as_ye_bu(text: str):
    """Returns the text colored in yellow, bold and underlined."""
    return termcolor.colored(text, "yellow", attrs=["bold", "underline"])


def as_bl(text: str):
    """Returns the text colored in blue."""
    return termcolor.colored(text, "blue")


def as_bl_bl(text: str):
    """Returns the text colored in blue and bold."""
    return termcolor.colored(text, "blue", attrs=["bold"])


def as_bl_ul(text: str):
    """Returns the text colored in blue and underlined."""
    return termcolor.colored(text, "blue", attrs=["underline"])


def as_bl_bu(text: str):
    """Returns the text colored in blue, bold and underlined."""
    return termcolor.colored(text, "blue", attrs=["bold", "underline"])


def as_mg(text: str):
    """Returns the text colored in magenta."""
    return termcolor.colored(text, "magenta")


def as_mg_bl(text: str):
    """Returns the text colored in magenta and bold."""
    return termcolor.colored(text, "magenta", attrs=["bold"])


def as_mg_ul(text: str):
    """Returns the text colored in magenta and underlined."""
    return termcolor.colored(text, "magenta", attrs=["underline"])


def as_mg_bu(text: str):
    """Returns the text colored in magenta, bold and underlined."""
    return termcolor.colored(text, "magenta", attrs=["bold", "underline"])


def as_cy(text: str):
    """Returns the text colored in cyan."""
    return termcolor.colored(text, "cyan")


def as_cy_bl(text: str):
    """Returns the text colored in cyan and bold."""
    return termcolor.colored(text, "cyan", attrs=["bold"])


def as_cy_ul(text: str):
    """Returns the text colored in cyan and underlined."""
    return termcolor.colored(text, "cyan", attrs=["underline"])


def as_cy_bu(text: str):
    """Returns the text colored in cyan, bold and underlined."""
    return termcolor.colored(text, "cyan", attrs=["bold", "underline"])


def as_wh(text: str):
    """Returns the text colored in white."""
    return termcolor.colored(text, "white")


def as_wh_bl(text: str):
    """Returns the text colored in white and bold."""
    return termcolor.colored(text, "white", attrs=["bold"])


def as_wh_ul(text: str):
    """Returns the text colored in white and underlined."""
    return termcolor.colored(text, "white", attrs=["underline"])


def as_wh_bu(text: str):
    """Returns the text colored in white, bold and underlined."""
    return termcolor.colored(text, "white", attrs=["bold", "underline"])


def as_gy(text: str):
    """Returns the text colored in grey."""
    return termcolor.colored(text, "grey")


def as_gy_bl(text: str):
    """Returns the text colored in grey and bold."""
    return termcolor.colored(text, "grey", attrs=["bold"])


def as_gy_ul(text: str):
    """Returns the text colored in grey and underlined."""
    return termcolor.colored(text, "grey", attrs=["underline"])


def as_gy_bu(text: str):
    """Returns the text colored in grey, bold and underlined."""
    return termcolor.colored(text, "grey", attrs=["bold", "underline"])


def print_as_re(text: str):
    """Prints the text colored in red."""
    print(termcolor.colored(text, "red"))


def print_as_re_bl(text: str):
    """Prints the text colored in red and bold."""
    print(termcolor.colored(text, "red", attrs=["bold"]))


def print_as_re_ul(text: str):
    """Prints the text colored in red and underlined."""
    print(termcolor.colored(text, "red", attrs=["underline"]))


def print_as_re_bu(text: str):
    """Prints the text colored in red, bold and underlined."""
    print(termcolor.colored(text, "red", attrs=["bold", "underline"]))


def print_as_gr(text: str):
    """Prints the text colored in green."""
    print(termcolor.colored(text, "green"))


def print_as_gr_bl(text: str):
    """Prints the text colored in green and bold."""
    print(termcolor.colored(text, "green", attrs=["bold"]))


def print_as_gr_ul(text: str):
    """Prints the text colored in green and underlined."""
    print(termcolor.colored(text, "green", attrs=["underline"]))


def print_as_gr_bu(text: str):
    """Prints the text colored in green, bold and underlined."""
    print(termcolor.colored(text, "green", attrs=["bold", "underline"]))


def print_as_ye(text: str):
    """Prints the text colored in yellow."""
    print(termcolor.colored(text, "yellow"))


def print_as_ye_bl(text: str):
    """Prints the text colored in yellow and bold."""
    print(termcolor.colored(text, "yellow", attrs=["bold"]))


def print_as_ye_ul(text: str):
    """Prints the text colored in yellow and underlined."""
    print(termcolor.colored(text, "yellow", attrs=["underline"]))


def print_as_ye_bu(text: str):
    """Prints the text colored in yellow, bold and underlined."""
    print(termcolor.colored(text, "yellow", attrs=["bold", "underline"]))


def print_as_bl(text: str):
    """Prints the text colored in blue."""
    print(termcolor.colored(text, "blue"))


def print_as_bl_bl(text: str):
    """Prints the text colored in blue and bold."""
    print(termcolor.colored(text, "blue", attrs=["bold"]))


def print_as_bl_ul(text: str):
    """Prints the text colored in blue and underlined."""
    print(termcolor.colored(text, "blue", attrs=["underline"]))


def print_as_bl_bu(text: str):
    """Prints the text colored in blue, bold and underlined."""
    print(termcolor.colored(text, "blue", attrs=["bold", "underline"]))


def print_as_mg(text: str):
    """Prints the text colored in magenta."""
    print(termcolor.colored(text, "magenta"))


def print_as_mg_bl(text: str):
    """Prints the text colored in magenta and bold."""
    print(termcolor.colored(text, "magenta", attrs=["bold"]))


def print_as_mg_ul(text: str):
    """Prints the text colored in magenta and underlined."""
    print(termcolor.colored(text, "magenta", attrs=["underline"]))


def print_as_mg_bu(text: str):
    """Prints the text colored in magenta, bold and underlined."""
    print(termcolor.colored(text, "magenta", attrs=["bold", "underline"]))


def print_as_cy(text: str):
    """Prints the text colored in cyan."""
    print(termcolor.colored(text, "cyan"))


def print_as_cy_bl(text: str):
    """Prints the text colored in cyan and bold."""
    print(termcolor.colored(text, "cyan", attrs=["bold"]))


def print_as_cy_ul(text: str):
    """Prints the text colored in cyan and underlined."""
    print(termcolor.colored(text, "cyan", attrs=["underline"]))


def print_as_cy_bu(text: str):
    """Prints the text colored in cyan, bold and underlined."""
    print(termcolor.colored(text, "cyan", attrs=["bold", "underline"]))


def print_as_wh(text: str):
    """Prints the text colored in white."""
    print(termcolor.colored(text, "white"))


def print_as_wh_bl(text: str):
    """Prints the text colored in white and bold."""
    print(termcolor.colored(text, "white", attrs=["bold"]))


def print_as_wh_ul(text: str):
    """Prints the text colored in white and underlined."""
    print(termcolor.colored(text, "white", attrs=["underline"]))


def print_as_wh_bu(text: str):
    """Prints the text colored in white, bold and underlined."""
    print(termcolor.colored(text, "white", attrs=["bold", "underline"]))


def print_as_gy(text: str):
    """Prints the text colored in grey."""
    print(termcolor.colored(text, "grey"))


def print_as_gy_bl(text: str):
    """Prints the text colored in grey and bold."""
    print(termcolor.colored(text, "grey", attrs=["bold"]))


def print_as_gy_ul(text: str):
    """Prints the text colored in grey and underlined."""
    print(termcolor.colored(text, "grey", attrs=["underline"]))


def print_as_gy_bu(text: str):
    """Prints the text colored in grey, bold and underlined."""
    print(termcolor.colored(text, "grey", attrs=["bold", "underline"]))


def print_divider() -> None:
    """Prints a divider line."""
    print(termcolor.colored("\n" + ("-=-" * 40) + "\n", "grey", attrs=["bold"]))
