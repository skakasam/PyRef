"""Python For and While Loops Practice Module"""

###############################################################################
# For Loops
###############################################################################
# Syntax:
# for variable in iterable:
#     # code block
###############################################################################
print("For Loops Examples:")

print("  Looping over string:")
name = "Novus"
for letter in name:
    print(f"    Letter: {letter}")

print("  Looping over list:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"    Index {index}: {fruit}")

print("  Looping over range:")
for i in range(5):
    print(f"    Index {i}")

print("  Looping over range with start and step:")
for i in range(1, 10, 2):
    print(f"    Index {i}")

print("  Looping over range in reverse:")
for i in range(5, 0, -1):
    print(f"    Index {i}")

print("  Looping over dictionary:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"    {key}: {value}")

print("  Looping over set:")
fruits_set = {"apple", "banana", "cherry"}
for fruit in fruits_set:
    print(f"    {fruit}")

print("  Looping over tuple:")
fruits_tuple = ("apple", "banana", "cherry")
for index, fruit in enumerate(fruits_tuple):
    print(f"    Index {index}: {fruit}")


class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        self.index = 0  # Resetting the index for a new iteration
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item


print("  Using our MyIterable class:")
my_numbers = MyIterable([10, 20, 30, 40, 50])
for number in my_numbers:
    print(f"    Number from MyIterable: {number}")


###############################################################################
# While Loops
###############################################################################
# Syntax:
# while condition:
#     # code block
###############################################################################
print("While Loops Examples:")
count = 0
while count < 5:
    print(f"    Looping through while: {count}")
    count += 1

###############################################################################
# Break and Continue statement usages in loops
###############################################################################
print("Break Statement Example:")
for i in range(10):
    if i == 5:
        print("    Breaking the loop at 5")
        break
    print(f"    Looping through: {i}")

print("Continue Statement Example:")
for i in range(5):
    if i == 2:
        print("    Skipping 2")
        continue
    print(f"    Looping through: {i}")

###############################################################################
# Else clause in Loops
###############################################################################
print("Else Clause Example:")
for i in range(5):
    if i == 6:
        print("    Found 6, exiting loop")
        break
else:
    print("    No break occurred")

###############################################################################
# Nested Loops
###############################################################################
print("Nested Loops Example:")
for i in range(3):
    for j in range(2):
        print(f"    Outer loop {i}, Inner loop {j}")
