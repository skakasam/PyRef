"""Python Dictionaries Practice Module"""

###############################################################################
# Dictionary Creation
###############################################################################
print("Dictionary Creation Examples:")
empty_dict = {}
print(f"  Empty Dictionary: {empty_dict}")
fruits = {"apple": 1, "banana": 2, "cherry": 3}
print(f"  Fruits Dictionary: {fruits}")
mixed_dict = {"one": 1, "two": 2.0, "three": [3]}
print(f"  Mixed Dictionary: {mixed_dict}")
# Can also instatiate using dict() by passing a valid iterable of key value pairs
# family = dict([("father", "John"), ("mother", "Emma"), ("children", ["Adam", "Bella"])])
# print(f"  Family Dictionary: {family}")
# Can also instatiate using dict() by passing a keyword arguments
# team = dict(manager="Alice", lead="Bob", members=["Charlie", "David"])
# print(f"  Team Dictionary: {team}")
checklist = {}.fromkeys(["apple", "grapes", "tomato", "onion"], 0)
print(f"  Checklist: {checklist}")

###############################################################################
# Accessing Dictionary Elements
###############################################################################
print("Accessing Dictionary Elements Examples:")
print(f"  Apple Count: {fruits['apple']}")
# print(f"  Mango Count: {fruits['mango']}") Results in KeyError
print(f"  Apple Count: {fruits.get('apple')}")
print(f"  Mango Count: {fruits.get('mango')}")
print(f"  Mango Count (default 0): {fruits.get('mango', 0)}")
print(f"  All Fruits: {fruits.keys()}")
print(f"  All Counts: {fruits.values()}")
print(f"  All Items: {fruits.items()}")

###############################################################################
# Modifying Dictionaries
###############################################################################
print("Modifying Dictionaries Examples:")
fruits["orange"] = 4
print(f"  After Add: {fruits}")
fruits["banana"] = 5
print(f"  After Update: {fruits}")
del fruits["cherry"]
print(f"  After Delete: {fruits}")

###############################################################################
# Dictionary Iteration
###############################################################################
print("Dictionary Iteration Examples:")
for fruit, count in fruits.items():
    print(f"  {fruit}: {count}")

###############################################################################
# Dictionary Methods
###############################################################################
print("Dictionary Methods Examples:")
print(f"  Length: {len(fruits)}")
print(f"  Contains 'apple'? {'apple' in fruits}")
print(f"  Contains 'grape'? {'grape' in fruits}")
popped_fruit_count = fruits.pop("orange", 0)
print(f"  Popped Fruit Count: {popped_fruit_count}")
print(f"  After Pop: {fruits}")
# cherry_count = fruits.pop("cherry") Results in KeyError
# print(f"  Popped Cherry Count: {cherry_count}")
# print(f"  After Pop: {fruits}")
fruits.clear()
print(f"  After Clear: {fruits}")
instore_orders = {"coffee": 2, "tea": 1, "juice": 3}
online_orders = {"coffee": 10, "sandwich": 5, "salad": 3}
total_orders = {}
total_orders.update(instore_orders)
total_orders.update(online_orders)
print(f"  Total Orders: {total_orders}")

################################################################################
# Dictionary Comprehension
################################################################################
# Dictionary comprehension is a concise way to create dictionaries in Python.
# It consists of an expression pair (key: value) followed by a for clause,
# and can include optional if clauses.
print("Dictionary Comprehension Examples:")
squared_fruits = {fruit: count**2 for fruit, count in fruits.items()}
print(f"  Squared Fruits: {squared_fruits}")
