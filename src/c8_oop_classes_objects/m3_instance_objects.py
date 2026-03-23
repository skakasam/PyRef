"""Python Instance Objects Practice Module"""

from m1_class_definitions import Transformer

################################################################################
# Working with Instance Objects
################################################################################
# Instance objects support:
#   -> Attribute Reference
#      1. Instance Variables (data attributes)
#      2. Methods (functions defined within the class)
################################################################################


print("OPERATIONS USING INSTANCE OBJECTS:")
print("    Referencing class attributes:")
megatron = Transformer.from_dict(
    {
        "name": "Megatron",
        "form": "Cybertronian Jet",
        "faction": "Decepticon",
    }
)
print(f"        {megatron.planet = }")
print("    Referencing static attributes:")
print(megatron.say_slogan("Peace through tyranny!", 8))
print("    Referencing instance attributes:")
print(f"        {megatron.name = }")
print(f"        {megatron.transform() = }")
