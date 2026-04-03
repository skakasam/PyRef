"""Python Managed Attributes Practice Module"""


################################################################################
# Unmanaged Attributes Example
#
# Pros:
#   1. Simple to implement.
#   2. No boilerplate code.
#
# Cons:
#   1. Lack of control over attribute access and Potential for invalid states.
#   2. Problems with future changes. Refactoring to add validation later can be
#      cumbersome. The clients become dependent on the current implementation
#      details.
################################################################################
class BasicPerson:
    def __init__(self, name):
        self.name = name


basic_person = BasicPerson("John Doe")
print(basic_person.name)  # Output: John Doe
basic_person.name = "Jane Doe"
print(basic_person.name)  # Output: Jane Doe


################################################################################
# Controlled Attributes Example
#
# Pros:
#   1. Better control over attribute access.
#   2. Validation logic can be added easily.
#
# Cons:
#   1. More boilerplate code.
#   2. Still potential for invalid states if not careful.
################################################################################
class ControlledPerson:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        elif not name:
            raise ValueError("Name cannot be empty")
        elif not name.strip():
            raise ValueError("Name cannot be whitespace")
        else:
            self._name = name


controlled_person = ControlledPerson("Emma Watson")
print(controlled_person.get_name())  # Output: Emma Watson
controlled_person.set_name("Emily Watson")
print(controlled_person.get_name())  # Output: Emily Watson


################################################################################
# Managed Attributes Example
#
# Pros:
#   1. Better control over attribute access.
#   2. Validation logic can be added easily.
#   3. Allows for computed properties (attribute accessors).
#      ** The property built-in, for specifying methods to handle access to
#      ** attributes.
#
#      ** The __get__ and __set__ descriptor methods, for handling access to
#      ** attributes and the basis for other tools such as properties and slots.
#
#      ** The __getattr__ and __setattr__ methods, for handling undefined attribute
#      ** fetches and all attribute assignments.
#
#      ** The __getattribute__ method, for handling all attribute access.
#
# Cons:
#   1. More boilerplate code.
################################################################################
class ManagedPerson:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        elif not value:
            raise ValueError("Name cannot be empty")
        elif not value.strip():
            raise ValueError("Name cannot be whitespace")
        else:
            self._name = value


managed_person = ManagedPerson("Johnny Walker")
print(managed_person.name)  # Output: Johnny Walker
managed_person.name = "Joanna Walker"
print(managed_person.name)  # Output: Joanna Walker
