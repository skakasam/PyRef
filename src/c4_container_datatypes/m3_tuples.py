"""Python Tuples Practice Module"""

###############################################################################
# Tuple Creation
###############################################################################
from operator import le

print("Tuple Creation Examples:")
empty_tuple = ()
print(f"  Empty Tuple: {empty_tuple}")
fruits = ("apple", "banana", "cherry")
print(f"  Fruits Tuple: {fruits}")
mixed_tuple = (1, 2.0, "three", [4])
print(f"  Mixed Tuple: {mixed_tuple}")
# Can also instatiate using tuple() by passing a valid iterable
# family = tuple(("John", "Emma", ["Adam", "Bella"]))
# print(f"  Family Tuple: {family}")
# team = tuple(["Alice", "Bob", ["Charlie", "David"]])
# print(f"  Team Tuple: {team}")

###############################################################################
# Accessing Tuple Elements
###############################################################################
print("Accessing Tuple Elements Examples:")
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"  First Day: {days[0]}")
print(f"  Second Day: {days[1]}")

###############################################################################
# Modifying Tuples
###############################################################################
print("Modifying Tuples Examples:")
# Tuples are immutable, so we cannot modify them directly
# fruits[1] = "blueberry"  Results in TypeError
# Instead, we can create a new tuple
fruits = fruits[:1] + ("blueberry",) + fruits[2:]
print(f"  After Modification: {fruits}")

###############################################################################
# Tuple Iteration
###############################################################################
print("Tuple Iteration Examples:")
for fruit in fruits:
    print(f"  {fruit}")

###############################################################################
# Tuple Methods
###############################################################################
print("Tuple Methods Examples:")
dell_laptop = "Dell Precision 5550 Laptop"
dell_monitor = "Dell Ultrasharp U2722D QHD Monitor"
lenovo_laptop = "Lenovo ThinkPad X1 Carbon Laptop"
lenovo_monitor = "Lenovo L27q-30 27-Inch QHD Monitor"
desk_setup = (
    dell_laptop,
    dell_monitor,
    dell_monitor,  # Can have duplicate items
    "Dell Thunderbolt WD19TBS Dock",
    "Vaydeer Dual Aluminum Monitor Stand Riser",
    "Nolansend 4K Webcam",
    "Insignia 7-Port USB 2.0 Hub",
    "Lenovo Wireless VoIP Headset",
    "Keychron B6 Pro Wireless Keyboard",
    "Keychron M6 Wireless Optical Mouse",
    "SHW 55-Inch Commercial-Grade Office Computer Desk",
    "Cykov Ergonomic Mesh Desk Chair",
)
print(f"  No of items in Desk Setup: {len(desk_setup)}")
print(f"  Desk Setup Contains '{dell_laptop}'? {dell_laptop in desk_setup}")
print(f"  Desk Setup Contains '{lenovo_laptop}'? {lenovo_laptop in desk_setup}")
print(f"  Count of '{dell_monitor}': {desk_setup.count(dell_monitor)}")
print(
    f"  Index of '{dell_monitor}'",
    f": {desk_setup.index(dell_monitor) if dell_monitor in desk_setup else -1}",
)
print(
    f"  Index of '{lenovo_monitor}'",
    f": {desk_setup.index(lenovo_monitor) if lenovo_monitor in desk_setup else -1}",
)

###############################################################################
# Tuple Unpacking
###############################################################################
laptop, monitor, *other_items = desk_setup
print("Tuple Unpacking Examples:")
print(f"  Laptop (type: {type(laptop)}): {laptop}")
print(f"  Monitor (type: {type(monitor)}): {monitor}")
print(f"  Other Items (type: {type(other_items)}): {other_items}")

###############################################################################
# Tuple Comprehension
###############################################################################
# Tuple comprehension is not directly supported in Python, but we can use
# generator expressions and the tuple() constructor to achieve similar results.
print("Tuple Comprehension Examples:")
squared = tuple(x**2 for x in range(10))
print(f"  Squared Tuple: {squared}")
