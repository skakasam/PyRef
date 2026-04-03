"""Python Lists Practice Module"""

###############################################################################
# List Creation
###############################################################################
print("List Creation Examples:")
empty_list = []
print(f"  Empty List: {empty_list}")
fruits = ["apple", "banana", "cherry"]
print(f"  Fruits List: {fruits}")
mixed_list = [1, "two", 3.0, [4, 5]]
print(f"  Mixed List: {mixed_list}")
numbers = list(range(1, 10))  # list(iterable)
print(f"  Numbers List: {numbers}")

###############################################################################
# Accessing List Elements
###############################################################################
print("Accessing List Elements Examples:")
print(f"  First Fruit: {fruits[0]}")
print(f"  Last Fruit: {fruits[-1]}")
print(f"  Slicing Fruits: {fruits[1:3]}")

###############################################################################
# Modifying Lists
###############################################################################
print("Modifying Lists Examples:")
fruits.append("orange")
print(f"  After Append: {fruits}")
fruits.remove("banana")
print(f"  After Remove: {fruits}")
fruits[0] = "kiwi"
print(f"  After Replace: {fruits}")
fruits.extend(["grape", "melon"])
print(f"  After Extend: {fruits}")
fruits.insert(1, "mango")
print(f"  After Insert: {fruits}")
fruit = fruits.pop()
print(f"  After Pop: {fruits}, Popped: {fruit}")

###############################################################################
# List Iteration
###############################################################################
print("List Iteration Examples:")
for fruit in fruits:
    print(f"  Fruit: {fruit}")

for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

###############################################################################
# List Methods
###############################################################################
print("List Methods Examples:")
print(f"  Length: {len(fruits)}")
print(f"  Count of 'apple': {fruits.count('apple')}")
fruits.sort()
print(f"  After Sort: {fruits}")
fruits.reverse()
print(f"  After Reverse: {fruits}")
print(f"  Comma separated fruits: {", ".join(fruits)}")
basket = fruits.copy()
print(f"  Basket Copy: {basket}")
print(f"  Is Basket Equal to Fruits? {basket is fruits}")
basket.remove("kiwi")
print(f"  Basket after Removing Kiwi: {basket}")
basket.clear()
print(f"  Basket after Clear: {basket}")

###############################################################################
# Nested Lists
###############################################################################
print("Nested Lists Example:")
nested_list = [fruits, [1, 2, 3]]
print(f"  Nested List: {nested_list}")

###############################################################################
# List Comprehensions
###############################################################################
print("List Comprehensions Examples:")
squared = [x**2 for x in range(5)]
print(f"  Squared Numbers: {squared}")
even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"  Even Numbers: {even_numbers}")
even_odd_numbers = [f"{x}-EVEN" if x % 2 == 0 else f"{x}-ODD" for x in range(10)]
print(f"  Even/Odd Numbers: {even_odd_numbers}")
