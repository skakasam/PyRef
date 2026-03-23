"""Python OOP Inheritance Practice Module"""

import random

################################################################################
# OOP Principle: Inheritance
################################################################################
# Inheritance is a mechanism in OOP that allows a new class (child class)
# to inherit attributes and methods from an existing class (parent class).
# This promotes code reusability and establishes a relationship between
# the parent and child classes.
#
# In Python, inheritance is achieved by defining a new class that
# derives from an existing class. The child class can override or extend
# the functionality of the parent class.
#
# Key Concepts of Inheritance
# 1. Single Inheritance: A child class inherits from one parent class.
# 2. Multiple Inheritance: A child class can inherit from multiple parent classes.
# 3. Method Overriding: A child class can provide a specific implementation of a method
#    that is already defined in its parent class.
# 4. Super(): A built-in function that allows you to call methods from the parent class.
################################################################################

HOUSE_GRIFFINDOR = "Gryffindor"
HOUSE_HUFFLEPUFF = "Hufflepuff"
HOUSE_RAVENCLAW = "Ravenclaw"
HOUSE_SLYTHERIN = "Slytherin"
HOUSES = [HOUSE_GRIFFINDOR, HOUSE_HUFFLEPUFF, HOUSE_RAVENCLAW, HOUSE_SLYTHERIN]
SPELL_EXPECTO_PATRONUM = "Expecto Patronum"


class Wizard:
    """A Wizard in the Wizarding World"""

    def __init__(self, name, house):
        self._name = name
        self._house = self.sort_house() if not house else house

    @staticmethod
    def sort_house():
        return random.choice(HOUSES)

    @property
    def name(self):
        """Getter for name"""
        return self._name

    @property
    def house(self):
        """Getter for house"""
        return self._house

    def cast_spell(self, spell):
        """Cast a spell"""
        return f"{self.name} casts {spell}!"

    def __str__(self) -> str:
        return f"Wizard(name={self.name}, house={self.house})"


class Student(Wizard):
    """A Student in the Wizarding World"""

    def __init__(self, name, house, spirit_guardian):
        super().__init__(name, house)  # Call the parent class constructor
        self._spirit_guardian = spirit_guardian  # Add additional data attributes

    @property
    def spirit_guardian(self):
        """Getter for spirit guardian"""
        return self._spirit_guardian

    def cast_spell(self, spell):  # Override the cast_spell method
        if spell == SPELL_EXPECTO_PATRONUM:
            return (
                f"{self.name} casts {spell} and summons their spirit "
                f"guardian: {self.spirit_guardian}!"
            )
        return super().cast_spell(spell=spell)

    def __str__(self) -> str:
        return (
            f"Student(name={self.name}, house={self.house}, "
            f"spirit_guardian={self.spirit_guardian})"
        )


if __name__ == "__main__":
    professor = Wizard("Albus Dumbledore", HOUSE_GRIFFINDOR)
    print(professor)
    print(professor.cast_spell(SPELL_EXPECTO_PATRONUM))
    print(f"{isinstance(professor, Wizard) = }")
    print(f"{isinstance(professor, Student) = }")

    print()

    student = Student("Harry Potter", HOUSE_GRIFFINDOR, "Stag")
    print(student)
    print(student.cast_spell(SPELL_EXPECTO_PATRONUM))
    print(f"{isinstance(student, Wizard) = }")
    print(f"{isinstance(student, Student) = }")
