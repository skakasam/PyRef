"""Python Class Objects Practice Module"""

from m1_class_definitions import Transformer

################################################################################
# Working with Class Objects
################################################################################
# Class objects support:
#   -> Attribute Reference
#      1. Class Variables
#      2. Class Methods
#   -> Object Instantiation
################################################################################
optimus = Transformer("Optimus Prime", "Freightliner Truck", "Autobot")

print("OPERATIONS USING CLASS OBJECTS:")
print("    Referencing data attributes:")
print(f"        {Transformer.planet = }")
print("    Referencing method attributes:")
print(f"        {Transformer.say_slogan = }")
print(f"        {Transformer.from_dict = }")
print(f"        {Transformer.transform = }")
print("    Instantiating Objects:")
print(f"        {optimus = }")
