"""Python OOP Polymorphism Practice Module"""

################################################################################
# OOP Principle: Polymorphism
################################################################################
# Polymorphism is a core concept in OOP that allows objects of different classes
# to be treated as objects of a common superclass. It enables a single interface
# to represent different underlying forms (data types). The most common use of
# polymorphism is when a parent class reference is used to refer to a child class
# object.
#
# Key Concepts of Polymorphism
# 1. Method Overriding: A child class can provide a specific implementation of a
#    method that is already defined in its parent class. This topic is covered
#    in the Inheritance section.
# 2. Duck Typing: In Python, the type or class of an object is less important
#    than the methods it defines. If an object behaves like a certain type,
#    it can be treated as that type.
################################################################################


# This functionality is similar to Protocols in Python
class Cat:
    """A simple Cat class"""

    def speak(self):
        return "Meow!"


class Dog:
    """A simple Dog class"""

    def speak(self):
        return "Woof!"


def get_animal_sound(animal):
    return animal.speak()


print(get_animal_sound(Cat()))  # Output: Meow!
print(get_animal_sound(Dog()))  # Output: Woof!

# Other examples of Polymorphism using operator overloading


class Vault:
    """A Vault in the Wizarding World"""

    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    @property
    def galleons(self):
        """Getter for galleons"""
        return self._galleons

    @galleons.setter
    def galleons(self, galleons):
        """Setter for galleons"""
        if not isinstance(galleons, int) or galleons < 0:
            raise ValueError("Galleons must be a non-negative integer.")
        self._galleons = galleons

    @property
    def sickles(self):
        """Getter for sickles"""
        return self._sickles

    @sickles.setter
    def sickles(self, sickles):
        """Setter for sickles"""
        if not isinstance(sickles, int) or sickles < 0:
            raise ValueError("Sickles must be a non-negative integer.")
        self._sickles = sickles

    @property
    def knuts(self):
        """Getter for knuts"""
        return self._knuts

    @knuts.setter
    def knuts(self, knuts):
        """Setter for knuts"""
        if not isinstance(knuts, int) or knuts < 0:
            raise ValueError("Knuts must be a non-negative integer.")
        self._knuts = knuts

    def __total_value(self):
        """Calculate the total value of the vault in knuts."""
        return self.galleons * 493 + self.sickles * 29 + self.knuts

    # Operator Overloading for adding two Vaults
    def __add__(self, other):
        if not isinstance(other, Vault):
            raise ValueError("The argument must be a Vault instance.")

        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        return Vault(galleons, sickles, knuts)

    # Operator Overloading for substracting two Vaults
    def __sub__(self, other):
        if not isinstance(other, Vault):
            raise ValueError("The argument must be a Vault instance.")

        cur_value = self.__total_value()
        oth_value = other.__total_value()

        if cur_value < oth_value:
            raise ValueError("Cannot subtract a larger vault from a smaller one.")
        new_value = cur_value - oth_value

        galleons = new_value // 493
        new_value %= 493
        sickles = new_value // 29
        knuts = new_value % 29

        return Vault(galleons, sickles, knuts)

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


if __name__ == "__main__":
    vault1 = Vault(100, 50, 25)
    print(f"Vault 1: {vault1}")
    vault2 = Vault(200, 75, 50)
    print(f"Vault 2: {vault2}")
    vault3 = vault2 - vault1
    print(f"Vault 3: {vault3}")
