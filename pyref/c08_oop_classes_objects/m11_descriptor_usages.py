"""Custom Validators using Descriptors"""

from abc import ABC, abstractmethod
import re


# Generic Validator
class Validator(ABC):
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f"_{name}"

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    @abstractmethod
    def validate(self, value):
        pass


class EmailAttribute(Validator):
    def validate(self, value):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if not re.match(pattern, value):
            raise ValueError("Must be a valid email address")


class Email:
    email_id = EmailAttribute()

    def __init__(self, email_id):
        self.email_id = email_id

    def __repr__(self):
        return f"Email(email_id={self.email_id})"


valid_email = Email(email_id="test@example.com")
print(valid_email)
# invalid_email = Email(email_id="invalid-email") Throws error!


# Custom Validators
class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {self.options!r}")


class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value!r} to be an int or float")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Expected {value!r} to be at least {self.minvalue!r}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Expected {value!r} to be no more than {self.maxvalue!r}")


class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r} to be a str")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f"Expected {value!r} to be no smaller than {self.minsize!r}")
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f"Expected {value!r} to be no bigger than {self.maxsize!r}")
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f"Expected {self.predicate} to be true for {value!r}")


class Component:

    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf("wood", "metal", "plastic")
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity

    def __repr__(self):
        return f"Component(name={self.name}, kind={self.kind}, quantity={self.quantity})"


valid_component = Component(name="WIDGET", kind="metal", quantity=10)
print(valid_component)
# invalid_component = Component(name="wd", kind="glass", quantity=-5) Throws error!


# Simulating Properties using Descriptors
class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("unwriteable attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("undeletable attribute")
        self.fdel(instance)


class Label:
    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def __init__(self, text):
        self.text = text

    name = Property(fget=get_text, fset=set_text)


label = Label("Python")
print(label.name)
label.name = "Java"
print(label.name)
del label.name
