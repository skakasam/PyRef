"""Python Conditional Expressions Practice Module"""

###############################################################################
# Comparison Operators
# 1. Equal                    (==)
# 2. Not Equal                (!=)
# 3. Greater Than             ( >)
# 4. Less Than                ( <)
# 5. Greater Than or Equal To (>=)
# 6. Less Than or Equal To    (<=)
###############################################################################
from ast import Pass


print("Comparison Operators:")
print(f"    Is 5 == 2 ? {5 == 2}")
print(f"    Is 2 != 5 ? {2 != 5}")
print(f"    Is 5  > 2 ? {5  > 2}")
print(f"    Is 5  < 2 ? {5  < 2}")
print(f"    Is 5 >= 4 ? {5 >= 4}")
print(f"    Is 5 <= 4 ? {5 <= 4}")

###############################################################################
# Membership Operators (x in y / x not in y)
# 1. In                       (in)
# 2. Not In                   (not in)
#
# Note:
# 1. For strings and byte types, x in y is True if x is a substring of y.
# 2. For sequences (e.g., lists, tuples), x in y is True if x is an element of y.
# 3. For dictionaries, x in y is True if x is a key in y.
# 4. For sets, x in y is True if x is an element of y.
# 5. For user-defined classes, x in y is True if y implements the __contains__,
#    and it returns true for x.
# 6. For iterators that define __getitem__, then x in y is True if y can be indexed
#    and it returns a non-negative integer index i such that x == y[i] or x is y[i].
###############################################################################
print("Membership Operators:")
print(f"    Is 'a' in 'apple'? {'a' in 'apple'}")
print(f"    Is 'b' not in 'apple'? {'b' not in 'apple'}")
print(f"    Is 1 in [1, 2, 3]? {1 in [1, 2, 3]}")
print(f"    Is 4 not in [1, 2, 3]? {4 not in [1, 2, 3]}")


###############################################################################
# Identity Operators (x is y / x is not y)
# This operator tests for object identity
# 1. Is                        (is)
# 2. Is Not                    (is not)
# Note: An object's identity is determined using the id() function
###############################################################################
class Person:
    pass


class Animal:
    pass


class Dragon(Animal):
    pass


dragon, person = Dragon(), Person()
animal = dragon

print("Identity Operators:")
print(f"    Is dragon a person? {dragon is person}")
print(f"    Is dragon an animal? {dragon is animal}")
print(f"    Is dragon not a person? {dragon is not person}")
print(f"    id(person) = {id(person)}, id(animal) = {id(animal)}, id(dragon) = {id(dragon)}")


###############################################################################
# Boolean Operators (and, or, not)
# 1. And                      (and)
# 2. Or                       (or)
# 3. Not                      (not)
###############################################################################
is_active = True
print("Boolean Operators:")
print(f"    Is (5 > 2) and (2 < 3)? {(5 > 2) and (2 < 3)}")
print(f"    Is (5 > 2) or (2 > 3)? {(5 > 2) or (2 > 3)}")
print(f"    Is not active? {not is_active}")
