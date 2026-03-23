"""Python Dynamic/Duck Typing Practice"""

###############################################################################
# Python is a dynamically typed language i.e., the datatypes of variables can
# change once it's been initialized. There is no need to declare the type of a
# variable explicitly.
#
# This is often summarized as:
#   `If it walks like a duck and quacks like a duck, then it must be a duck`
#
# Types live with Objects, not Variables. See code examples below, where the
# type of the object assigned to `my_var` variable is determined at runtime.
#
# Objects have more structure than just their values. Each object also has two
# standard header fields:
#   1. `type designator` used to mark the type of the object
#   2. `reference counter` used to keep track of the number of references to
#       the object, which helps in memory management and garbage collection.
###############################################################################

my_var = None
print(f"{type(my_var)=}")

my_var = "Novus Skills"
print(f"{type(my_var)=}")

my_var = 100
print(f"{type(my_var)=}")

my_var = 3.14
print(f"{type(my_var)=}")

my_var = True
print(f"{type(my_var)=}")

###############################################################################
# Shared Reference with Immutable Objects
###############################################################################

# Example 1:
name = "Python"
# Both variables point to the same "Python" string object at this point
lang = name
# Now, `name` points to a new "Java" string object, # while `lang` still points to "Python"
name = "Java"
# Now, `lang` points to the same "Java" string object as `name`. And, no references to the
# old "Python" string object remain. Consequently, it becomes eligible for garbage collection.
lang = name

# Example 2:
a = 3
b = a
print(f"Before: a(id={id(a)})={a}, b(id={id(b)})={b}")
print(f"a == b? {a == b}")
print(f"a is b? {a is b}")
# a now points to a new integer object with value 5, int operations are immutable
a = a + 2
print(f"After: a(id={id(a)})={a}, b(id={id(b)})={b}")
print(f"a == b? {a == b}")
print(f"a is b? {a is b}")

###############################################################################
# Shared Reference with Mutable Objects (In-Place Modification)
###############################################################################
list_1 = [1, 2, 3]
list_2 = list_1
print(f"Before: list_1(id={id(list_1)})={list_1}, list_2(id={id(list_2)})={list_2}")
print(f"list_1 == list_2? {list_1 == list_2}")
print(f"list_1 is list_2? {list_1 is list_2}")
list_1.append(4)  # In-place modification: both variables reflect the change
print(f"After: list_1(id={id(list_1)})={list_1}, list_2(id={id(list_2)})={list_2}")
print(f"list_1 == list_2? {list_1 == list_2}")
print(f"list_1 is list_2? {list_1 is list_2}")

###############################################################################
# Getting Reference Counts
###############################################################################
import sys

print(f"Reference count for list_1: {sys.getrefcount(list_1)}")
print(f"Reference count for list_2: {sys.getrefcount(list_2)}")
print(f"Reference count for [1,2,3,4]: {sys.getrefcount([1,2,3,4])}")

###############################################################################
# Shared References and Equality
###############################################################################
list_1 = ["red", "blue", "green"]
list_2 = list_1
list_3 = ["red", "blue", "green"]

print(f"{id(list_1)=}")
print(f"{id(list_2)=}")
print(f"{id(list_3)=}")

print(f"list_1 == list_2? {list_1 == list_2}")  # True, same content
print(f"list_1 is list_2? {list_1 is list_2}")  # True, same object

print(f"list_1 == list_3? {list_1 == list_3}")  # True, same content
print(f"list_1 is list_3? {list_1 is list_3}")  # False, different objects

print(f"Reference count for list_1: {sys.getrefcount(list_1)}")
print(f"Reference count for list_2: {sys.getrefcount(list_2)}")
print(f"Reference count for list_3: {sys.getrefcount(list_3)}")
