"""Snake module for displaying a singing snake."""

_SNAKE_SING = r"""
  ♫♪♫♪♫♪♫
      \  __
        {00}
        \__/
        /^/
       ( (
       \_\______
       (________)
      (__________)=Oo⚬
"""


def sing():
    """Display a singing snake."""
    print(_SNAKE_SING)


if __name__ == "__main__":
    sing()
