"""Python Sets Practice Module"""

###############################################################################
# Sets are unordered collections of unique elements. Elements cannot be accessed
# by index.
###############################################################################
# Set Creation
###############################################################################
print("Set Creation Example:")
empty_set = {}
print(f"  Empty Set                     : {empty_set}")
my_set = {1, 2, 3}
print(f"  My Set                        : {my_set}")
set_from_list = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(f"  Set from List                 : {set_from_list}")

###############################################################################
# Accessing Set Elements
###############################################################################
print("Accessing Set Elements Example:")
print(f"  My Set                        : {my_set}")
print(f"  First Element (Arbitrary)     : {next(iter(my_set))}")
print(f"  Contains 2?                   : {'Yes' if 2 in my_set else 'No'}")

###############################################################################
# Modifying Set Elements
###############################################################################
print("Modifying Set Elements Example:")
print(f"  My Set (Before)               : {my_set}")
my_set.add(4)
print(f"  My Set (After Adding 4)       : {my_set}")
my_set.remove(2)
print(f"  My Set (After Removing 2)     : {my_set}")

###############################################################################
# Set Iteration
###############################################################################
print("Set Iteration Example:")
for element in my_set:
    print(f"  Element: {element}")

###############################################################################
# Set Operations
###############################################################################
print("Set Operations Example:")
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"  Set A                         : {set_a}")
print(f"  Set B                         : {set_b}")
print(f"  Union                         : {set_a | set_b}")
print(f"  Intersection                  : {set_a & set_b}")
print(f"  Difference (A - B)            : {set_a - set_b}")
print(f"  Symmetric Difference          : {set_a ^ set_b}")

################################################################################
# Set Comprehensions
################################################################################
print("Set Comprehensions Example:")
set_c = {x * 2 for x in range(5)}
print(f"  Set C                         : {set_c}")
set_d = {x for x in range(10) if x % 2 == 0}
print(f"  Set D                         : {set_d}")
set_e = {x if x % 2 != 0 else x * 2 for x in range(10)}
print(f"  Set E                         : {set_e}")
