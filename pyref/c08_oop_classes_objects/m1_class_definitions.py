"""Python Class Definition Practice Module"""


################################################################################
# Class Definition
################################################################################
# Data Attributes:
#   1. Class variables are shared among all instances of the class. They can be
#      accessed using the class name or an instance.
#   2. Instance variables (data attributes) are defined within the __init__ method
#      and are unique to each instance of the class.
#
# Method Attributes:
#   1. Class methods are defined using the @classmethod decorator and take cls
#      as the first parameter.
#      USES:
#         - Accessing class variables
#         - Factory methods
#   2. Instance methods are defined using the self parameter. They require an
#      instance of the class to be called.
#      USES:
#         - Accessing instance variables
#         - Modifying instance state
#   3. Static methods are defined using the @staticmethod decorator and do not
#      require an instance or class reference.
#      USES:
#         - Utility functions
#         - Functions that operate on parameters rather than instance or class data
################################################################################
class Transformer:
    """A simple Transformer class"""

    planet = "Cybertron"

    def __init__(self, name, form, faction):
        self._name = name
        self._form = form
        self._faction = faction
        self._alt_mode = False

    @classmethod
    def from_dict(cls, data):
        """Create a Transformer instance from a dictionary."""
        return cls(**data)

    def transform(self):
        """Transform into alt or robot mode"""
        if self._alt_mode:
            self._alt_mode = False
            return f"{self._form} transforms back into {self._name}"

        self._alt_mode = True
        return f"{self._name} transforms into {self._form}"

    @property
    def name(self):
        return self._name

    @property
    def form(self):
        return self._form

    @property
    def faction(self):
        return self._faction

    @staticmethod
    def say_slogan(message, lpad=0):
        """Create a speech bubble around the given message."""
        lines = message.split("\n")
        max_length = max(len(line) for line in lines)
        top_border = " " * lpad + "╭" + "-" * (max_length + 2) + "╮"
        bottom_border = " " * lpad + "╰" + "-" * (max_length + 2) + "╯"
        bubble_lines = [top_border]
        for line in lines:
            bubble_lines.append(" " * lpad + f"| {line.ljust(max_length)} |")
        bubble_lines.append(bottom_border)
        return "\n".join(bubble_lines)

    def __repr__(self) -> str:
        """String representation of the Transformer instance"""
        return f"Transformer(name={self._name!r}, form={self._form!r}, faction={self._faction!r})"
