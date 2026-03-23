"""Python OOP Abstraction Practice Module"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

################################################################################
# OOP Principle: Abstraction
################################################################################
# Abstraction is a fundamental concept in OOP that focuses on hiding the
# complex implementation details and exposing only the essential features
# of an object. It allows developers to work with high-level interfaces
# without needing to understand the intricate workings of the underlying code.
#
# Key Concepts of Abstraction
# 1. Abstract Classes: A class that cannot be instantiated and is designed
#    to be subclassed. It may contain abstract methods that must be implemented
#    by its subclasses.
# 2. Interfaces: A contract that defines a set of methods that a class must
#    implement, without providing the implementation details.
################################################################################


################################################################################
# Using Python's Abstract Base Class (ABC) Module
################################################################################
class Shape(ABC):
    """Abstract Base Class for Shapes"""

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def draw(self):
        print(f"Drawing a {self}")

    def __str__(self):
        properties = {}
        for attr in dir(self):
            if not attr.startswith("_") and not callable(getattr(self, attr)):
                properties[attr] = getattr(self, attr)

        return (
            f"{self.__class__.__name__} "
            f"({', '.join(f'{key}={value}' for key, value in properties.items())})"
        )


class Circle(Shape):
    """Circle Class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius**2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    """Rectangle Class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


################################################################################
# Using Python's Protocol Module
################################################################################
@runtime_checkable
class Drawable(Protocol):
    """Protocol for Drawable Objects"""

    def draw(self) -> None:
        """This method draws a shape."""


def draw_shape(shape: Drawable) -> None:
    shape.draw()


class Square:
    """Square Class"""

    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self) -> None:
        print(f"Drawing a square with side length {self.side_length}")


if __name__ == "__main__":
    # Using ABCs
    circle = Circle(5)
    print(f"Circle Area: {circle.area():.2f}")
    print(f"Circle Perimeter: {circle.perimeter():.2f}")
    circle.draw()

    print()

    rectangle = Rectangle(4, 6)
    print(f"Rectangle Area: {rectangle.area():.2f}")
    print(f"Rectangle Perimeter: {rectangle.perimeter():.2f}")
    rectangle.draw()

    print()
    print(f"Is circle instance of Shape? {isinstance(circle, Shape)}")
    print(f"Is rectangle instance of Shape? {isinstance(rectangle, Shape)}")

    # Using Protocols
    print()
    square = Square(3)

    draw_shape(circle)
    draw_shape(square)
    draw_shape(rectangle)

    print()

    print(f"Is circle drawable? {isinstance(circle, Drawable)}")
    print(f"Is square drawable? {isinstance(square, Drawable)}")
    print(f"Is rectangle drawable? {isinstance(rectangle, Drawable)}")
