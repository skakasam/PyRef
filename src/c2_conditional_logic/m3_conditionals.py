"""Python Conditional Statements Practice Module"""

###############################################################################
# If-Else Examples
###############################################################################
x = 10
y = 20
if x > y:
    print("X is greater than Y")
elif x < y:
    print("X is less than Y")
else:
    print("X is equal to Y")

###############################################################################
# Ternary Conditional Operator
###############################################################################
result = "X > Y" if x > y else "X < Y" if x < y else "X = Y"
print(f"Ternary Result: {result}")


###############################################################################
# Match Case (Python 3.10+)
###############################################################################
def match_case_example_1(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Unknown"


print(f"Match Case Result: {match_case_example_1(1)}")


###############################################################################
# Pattern Matching with Structures
###############################################################################
def match_case_example_2(value):
    match value:
        case (1, 2):
            return "Tuple (1, 2)"
        case [1, 2]:
            return "List [1, 2]"
        case _:
            return "Unknown"


print(f"Match Case Result: {match_case_example_2((1, 2))}")
