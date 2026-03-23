"""Python OOP Encapsulation Practice Module"""

################################################################################
# OOP Principle: Encapsulation
################################################################################
# Encapsulation is the bundling of data (attributes) and methods (functions)
# that operate on the data into a single unit, or class. It restricts direct
# access to some of the object's components, which is a means of preventing
# accidental interference and misuse of the methods and attributes.
#
# In Python, we achieve encapsulation through:
#   1. Private Attributes: Prefixing an attribute with an underscore (_) makes it
#      "private" by convention, indicating it should not be accessed directly
#      outside the class.
#   2. Property Decorators: These are built-in decorators (@property,
#      @<attribute>.setter, @<attribute>.deleter) that allow us to define methods
#      that can be accessed like attributes.
#   3. Name Mangling: Prefixing an attribute with double underscores (__)
#      triggers name mangling, which changes the name of the attribute in a way
#      that makes it harder to create subclasses that accidentally override
#      private attributes.
#   4. Composition: Instead of inheriting from a class, we can include instances
#      of other classes as attributes, thereby encapsulating their behavior and
#      state.
#   5. Aggregation: This is a special form of composition where the contained
#      objects can exist independently of the container.
################################################################################


class Galleon:
    """A class representing a Galleon in the Wizarding World"""

    def __init__(self, value=0):
        self.value = value

    @property
    def value(self):
        """Getter for the value"""
        return self._value

    def to_galleons(self):
        """Convert Galleons to Galleons."""
        return self.value

    def to_sickles(self):
        """Convert Galleons to Sickles."""
        return self.value * 17

    def to_knuts(self):
        """Convert Galleons to Knuts."""
        return self.value * 493

    @value.setter
    def value(self, value):
        """Setter for the value"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Galleon value must be a non-negative integer.")
        self._value = value

    def __str__(self):
        return f"{self.value} Galleons"


class Sickles:
    """A class representing a Sickle in the Wizarding World"""

    def __init__(self, value=0):
        self.value = value

    @property
    def value(self):
        """Getter for the value"""
        return self._value

    @value.setter
    def value(self, value):
        """Setter for the value"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Sickle value must be a non-negative integer.")
        self._value = value

    def to_galleons(self):
        """Convert Sickles to Galleons."""
        return self.value / 17

    def to_sickles(self):
        """Convert Sickles to Sickles."""
        return self.value

    def to_knuts(self):
        """Convert Sickles to Knuts."""
        return self.value * 29

    def __str__(self):
        return f"{self.value} Sickles"


class Knuts:
    """A class representing a Knut in the Wizarding World"""

    def __init__(self, value=0):
        self.value = value

    @property
    def value(self):
        """Getter for the value"""
        return self._value

    @value.setter
    def value(self, value):
        """Setter for the value"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Knut value must be a non-negative integer.")
        self._value = value

    def to_galleons(self):
        """Convert Knuts to Galleons."""
        return self.value / 493

    def to_sickles(self):
        """Convert Knuts to Sickles."""
        return self.value / 29

    def to_knuts(self):
        """Convert Knuts to Knuts."""
        return self.value

    def __str__(self):
        return f"{self.value} Knuts"


class Vault:
    """A Vault in the Wizarding World"""

    def __init__(self, galleons=0, sickles=0, knuts=0):
        # Composition
        self.galleons = Galleon(galleons)
        self.sickles = Sickles(sickles)
        self.knuts = Knuts(knuts)

    def total_value(self):
        """Calculate the total value of the vault in Knuts."""
        return self.galleons.to_knuts() + self.sickles.to_knuts() + self.knuts.to_knuts()

    def __str__(self):
        return f"{self.galleons}, {self.sickles}, {self.knuts}"


if __name__ == "__main__":
    vault = Vault(3, 58, 493)
    print(f"Vault: {vault}")
    print(f"Total value in Knuts: {vault.total_value()}")
