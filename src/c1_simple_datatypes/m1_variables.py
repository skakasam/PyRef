"""Python Variables Practice Module"""

from itertools import count
from typing import Dict

################################################################################
# Variables are names that allow us to store, modify, and retrieve data easily
# in memory. They are typically defined in snake_case (underscore between words)
# and can hold various data types such as strings, numbers, lists, dictionaries,
# custom types etc.
#
# In Python, assignments cause the variables to spring into existence automatically.
################################################################################
message: str = "Hello, Python!"
print(message)

################################################################################
# Constant variables are typically defined in uppercase to indicate they should
# not change. Python does not enforce immutability, but it's a convention to
# treat these as constants.
################################################################################
PI: float = 3.14159
print(PI)  # Prints 3.14159

MAX_CONNECTIONS: int = 100
print(MAX_CONNECTIONS)  # Prints 100

ORGANIZATION_INFO: Dict[str, str] = {"name": "Novus Skills", "course": "Python"}
print(ORGANIZATION_INFO)

#################################################################################
# Multiple assignment
#################################################################################
name, age, occupation = "John", 32, "Programmer"
print(name, age, occupation)  # Prints John 32 Programmer


#################################################################################
# Variable Packing and Unpacking
#   1. *args and **kwargs
#   2. Packing values
#   3. Unpacking values
#################################################################################
def fun(required, *args, **kwargs):
    print(f"  Req     : {required}")
    print(f"  Args    : {args}")
    print(f"  Kwargs  : {kwargs}")


name = "Surya Akasam"
age = 38
occupation = "Engineer"
city = "Milton"
country = "Canada"

# *args and **kwargs
print("\n")
print("Scenario 1:")
fun(name)
print("Scenario 2:")
fun(name, age, occupation)
print("Scenario 3:")
fun(name, city=city, country=country)
print("Scenario 4:")
fun(name, age, occupation, city=city, country=country)
print("Scenario 5:")
details = [age, occupation]
fun(name, *details, city=city, country=country)

# Packing values into a tuple
print("\n")
packed = (name, age, occupation, city, country)
print("Packed Tuple:", packed)
# Parentheses are optional
packed_2 = name, age, occupation, city, country
print("Packed Tuple 2:", packed_2)

# Unpacking values from a tuple
unpacked_name, unpacked_age, unpacked_occupation, unpacked_city, unpacked_country = packed
print(
    "Unpacked Tuple:",
    unpacked_name,
    unpacked_age,
    unpacked_occupation,
    unpacked_city,
    unpacked_country,
)
unpacked_name, *remainder, unpacked_country = packed_2
print("Unpacked Tuple 2:", unpacked_name, remainder, unpacked_country)
print("Remainder Type:", type(remainder))

# Packing values into a list
print("\n")
packed_list = [name, age, occupation, city, country]
print("Packed List:", packed_list)

# Unpacking values from a list
unpacked_name, unpacked_age, unpacked_occupation, unpacked_city, unpacked_country = packed_list
print(
    "Unpacked List:",
    unpacked_name,
    unpacked_age,
    unpacked_occupation,
    unpacked_city,
    unpacked_country,
)

# Packing values into a dictionary
print("\n")
packed_dict = {
    "name": name,
    "age": age,
    "occupation": occupation,
    "city": city,
    "country": country,
}
print("Packed Dictionary:", packed_dict)

# Unpacking values from a dictionary
unpacked_name = packed_dict["name"]
unpacked_age = packed_dict["age"]
unpacked_occupation = packed_dict["occupation"]
unpacked_city = packed_dict["city"]
unpacked_country = packed_dict["country"]
print(
    "Unpacked Dictionary:",
    unpacked_name,
    unpacked_age,
    unpacked_occupation,
    unpacked_city,
    unpacked_country,
)

# Packing values into a set
print("\n")
packed_set = {name, age, occupation, city, country}
print("Packed Set:", packed_set)

# Unpacking values from a set
unpacked_name, unpacked_age, unpacked_occupation, unpacked_city, unpacked_country = packed_set
print(
    "Unpacked Set:",
    unpacked_name,
    unpacked_age,
    unpacked_occupation,
    unpacked_city,
    unpacked_country,
)


#################################################################################
# More Variable Packing and Unpacking
#################################################################################
def pack_args(*args):
    print(f"args: {args}")
    print(f"type: {type(args)}")


print("\n")
pack_args(1, 2, 3)


def unpack_args(arg1, arg2, arg3):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"arg3: {arg3}")


print("\n")
user_info = ["John", 30, "Engineer"]
unpack_args(*user_info)


def pack_kwargs(**kwargs):
    print(f"kwargs: {kwargs}")
    print(f"type: {type(kwargs)}")


print("\n")
pack_kwargs(name="John", age=30, occupation="Engineer")


def unpack_kwargs(name, age, occupation):
    print(f"name: {name}")
    print(f"age: {age}")
    print(f"occupation: {occupation}")


print("\n")
packed_dict = {"name": "John", "age": 30, "occupation": "Engineer"}
unpack_kwargs(**packed_dict)

#################################################################################
# Even More Variable Packing and Unpacking
#################################################################################
print("\n")
manager, lead, *associates = "Alice", "Bob", "Charlie", "David"
print("Manager       :", manager)
print("Lead          :", lead)
print("Associates    :", associates)

team = {"manager": "Alice", "lead": "Bob", "members": ["Charlie", "David"]}
manager, lead, *members = team.items()
print("Manager       :", manager)
print("Lead          :", lead)
print("Members       :", members)
