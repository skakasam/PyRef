"""Python Descriptor Protocol Practice Module"""

################################################################################
# Python Descriptors
################################################################################
# A descriptor is any object that defines __get__, __set__, or __delete__ methods.
#
# Optionally, a descriptor can also define __set_name__ method to know either the
# class where it was created or the name of the class variable it was assigned to.
# Note: __set_name__ method, if present, is called even if the class is not a
# descriptor.
################################################################################


def compute_age_group(self):
    match self.age:
        case x if x < 13:
            return "Child"
        case x if x < 19:
            return "Teenager"
        case x if x < 25:
            return "Youth"
        case x if x < 65:
            return "Adult"
        case _:
            return "Senior"


print("Declaring Computed Attribute Descriptor Class")


class ComputedAttribute:
    """Descriptor class for computed attributes."""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(f"  [COMPUTED ATTRIBUTE] __get__ {owner.__name__} {self.func.__name__}")
        return self.func(instance)


print("Declaring Managed Attribute Descriptor Class")


class ManagedAttribute:
    """Descriptor class for managing attribute."""

    def __set_name__(self, owner, name):
        print(f"  [MANAGED ATTRIBUTE] __set_name__ {owner.__name__} {name}")
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        print(f"  [MANAGED ATTRIBUTE] __get__ {owner.__name__} {self.public_name}")
        value = getattr(instance, self.private_name)
        return value

    def __set__(self, instance, value):
        print(f"  [MANAGED ATTRIBUTE] __set__ {instance.__class__.__name__} {self.public_name}")
        setattr(instance, self.private_name, value)

    def __delete__(self, instance):
        print(f"  [MANAGED ATTRIBUTE] __delete__ {instance.__class__.__name__} {self.public_name}")
        delattr(instance, self.private_name)


print("Declaring Person Class")


class Person:
    """Person class using the Attribute descriptor."""

    name = ManagedAttribute()  # First descriptor instance (callback to __set_name__)
    age = ManagedAttribute()  # Second descriptor instance (callback to __set_name__)
    age_group = ComputedAttribute(compute_age_group)

    def __init__(self, name, age, info):
        print("  [PERSON] __init__")
        self.name = name  # Calls the first descriptor
        self.age = age  # Calls the second descriptor
        self.info = info

    def __repr__(self):
        return (
            f"  Person(name={self.name!r}, age={self.age!r}, "
            f"category={self.age_group!r}, info={self.info!r})"
        )


print("Creating Person Instance")
person = Person("John Doe", 30, "Software Engineer")

print("Accessing Person Instance")
print(person)

################################################################################
# Person (Class Object) __dict__:
# >>> for key, val in sorted(vars(Person).items()): print(f"{key:<20s} {val}")
# ...
# __dict__             <attribute '__dict__' of 'Person' objects>
# __doc__              Person class using the Attribute descriptor.
# __firstlineno__      58
# __init__             <function Person.__init__ at 0x000001BEC55325C0>
# __module__           __main__
# __repr__             <function Person.__repr__ at 0x000001BEC5532660>
# __static_attributes__ ('age', 'info', 'name')
# __weakref__          <attribute '__weakref__' of 'Person' objects>
# age                  <__main__.ManagedAttribute object at 0x000001BEC51EDA90>
# age_group            <__main__.ComputedAttribute object at 0x000001BEC5256510>
# name                 <__main__.ManagedAttribute object at 0x000001BEC52563C0>
################################################################################

################################################################################
# person (Instance Object) __dict__:
# >>> for key, val in sorted(vars(person).items()): print(f"{key:<20s} {val}")
# ...
################################################################################
# _age                 30                      (Managed by Attribute Descriptor)
# _name                John Doe                (Managed by Attribute Descriptor)
# info                 Software Engineer       (Managed by Instance Variable)
################################################################################

################################################################################
# >>> dir(person)
################################################################################
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__static_attributes__', '__str__',
# '__subclasshook__', '__weakref__', '_age', '_name', 'age', 'age_group', 'info'
# , 'name']
################################################################################

################################################################################
# >>> vars(person)
# {'_name': 'John Doe', '_age': 30, 'info': 'Software Engineer'}
################################################################################

################################################################################
# >>> type(person.name)
# [ATTRIBUTE] __get__ Person _name
# <class 'str'>
# >>> type(person._name)
# <class 'str'>
################################################################################

################################################################################
# >>> type(person.age)
# [ATTRIBUTE] __get__ Person _age
# <class 'int'>
# >>> type(person._age)
# <class 'int'>
################################################################################

################################################################################
# >>> type(person.age_group)
#   [COMPUTED ATTRIBUTE] __get__ Person <lambda>
#   [MANAGED ATTRIBUTE] __get__ Person age
#   [MANAGED ATTRIBUTE] __get__ Person age
#   [MANAGED ATTRIBUTE] __get__ Person age
#   [MANAGED ATTRIBUTE] __get__ Person age
# <class 'str'>
################################################################################

################################################################################
# >>> type(person.info)
# <class 'str'>
################################################################################
