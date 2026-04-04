"""Snake module for displaying text with a snake."""

import sys

_SNAKE_SAY = r"""   \
    \  ...
      (o o)
       \_/ \
        λ \ \
         _(__)_
       _(______)_
      (__________)=Oo⚬
"""


def _bubble(message):
    """Create a speech bubble around the given message."""
    lines = message.split("\n")
    max_length = max(len(line) for line in lines)
    top_border = "╭" + "-" * (max_length + 2) + "╮"
    bottom_border = "╰" + "-" * (max_length + 2) + "╯"
    bubble_lines = [top_border]
    for line in lines:
        bubble_lines.append(f"| {line.ljust(max_length)} |")
    bubble_lines.append(bottom_border)
    return "\n".join(bubble_lines)


def say(message="S-S-Sleep, little man cub!"):
    """Display speech bubble with a snake."""
    print(_bubble(message))
    print(_SNAKE_SAY)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        say(sys.argv[1])
    else:
        say()
