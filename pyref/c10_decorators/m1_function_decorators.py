"""Python Function Decorators"""

from typing import Any, Callable

################################################################################
# Function Decorators are callable objects that manage or augment other functions,
# by adding additional functionality like logging, authentication, error handling,
# transaction management, caching, etc.
#
# They do name rebinding at function definition time, providing a layer of logic
# that can manage functions and methods or later calls to them with the help of
# Call Proxies (or Call Wrappers).
################################################################################
print("--> FUNCTION DECORATORS <--")


# Decorator with parameters
def styled(
    style: str = "none",
) -> Callable[[Callable[[Any], str]], Callable[[Any], str]]:
    STYLES_XREF = {
        "none": "\033[0m",
        "bold": "\033[1m",
        "faint": "\033[2m",
        "italic": "\033[3m",
        "underline": "\033[4m",
    }

    if style not in STYLES_XREF:
        raise ValueError(
            "style must be one of none, bold, faint, italic, or underline."
        )

    def decorator(func: Callable[[Any], str]) -> Callable[[Any], str]:
        """Wrap the text created by func in a box"""

        # Define the add_style wrapper function
        def add_style(*args, **kwargs):
            # Use func and args
            message = func(*args, **kwargs)

            # Add additional functionality
            lines = message.split("\n")

            styled_lines = []
            for line in lines:
                styled_lines.append(f"{STYLES_XREF[style]}{line}{STYLES_XREF['none']}")
            styled_message = "\n".join(styled_lines)

            # Return boxed message
            return styled_message

        # Return the add_style wrapper function
        return add_style

    # Return the decorator function
    return decorator


# Decorator without parameters
def boxed(func: Callable[[Any], str]) -> Callable[[Any], str]:
    """Wrap the text created by func in a box"""

    # Define the add_box wrapper function
    def add_box(*args, **kwargs):
        # Use func and args
        message = func(*args, **kwargs)

        # Add additional functionality
        lines = message.split("\n")
        max_length = max(len(line) for line in lines)

        top_border = "╭" + "-" * (max_length + 2) + "╮"
        bottom_border = "╰" + "-" * (max_length + 2) + "╯"

        bubble_lines = [top_border]
        for line in lines:
            bubble_lines.append(f"| {line.ljust(max_length)} |")
        bubble_lines.append(bottom_border)

        boxed_message = "\n".join(bubble_lines)

        # Return boxed message
        return boxed_message

    # Return the add_box wrapper function
    return add_box


@styled("faint")
@boxed
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Call the decorated greet funtion
    print(greet("Python"))
