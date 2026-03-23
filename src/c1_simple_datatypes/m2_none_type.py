"""Python NoneType Practice Module"""

###############################################################################
# In Python, None is a special constant that represents the absence of a value.
# It's an object of the NoneType class.
# 1. Singleton Object:
#       There is only one None object in Python.  This means all variables
#       assigned the value None actually point to the exact same object in
#       memory. You can confirm this using the is operator, for example, x
#       is None will evaluate to True if x is None.
# 2. Not the same as 0, an empty string, or False:
#       While these also represent "nothing" in certain contexts, None is
#       distinct from them. For instance, the boolean value of an empty string
#       "" is False, while the boolean value of None is also False. However,
#       they are not the same object or type.
# 3. Used as a placeholder:
#       None is often used to initialize variables that may be assigned a
#       meaningful value later. It's also the default return value for
#       functions that don't explicitly have a return statement.
# 4. The NoneType Class:
#       None is the sole instance of the NoneType class. You can check the
#       type of a variable with type(variable) is NoneType or simply variable
#       is None.
###############################################################################

from types import NoneType


name, age = None, None
print(f"type(name) = {type(name)}")
print(f"type(age) = {type(age)}")

name = "John"
print(f"name is None? {name is None}")
print(f"isinstance(age, NoneType)? {isinstance(age, NoneType)}")
