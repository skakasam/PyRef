"""Python Lambda Function Practice Module"""

################################################################################
# Lambda Functions
################################################################################
# A lambda function is a small anonymous function defined with the lambda keyword.
# It can take any number of arguments, but can only have one expression.
# Lambda functions are often used for short, throwaway functions.
################################################################################

# Scenario1: Lambda function with no arguments
print("Scenario1: Simple lambda function")
greet = lambda: "Hello, World!"
print(f"  Greeting: {greet()}")  # Output: Greeting: Hello, World!
print(f"  greet.__name__ is {greet.__name__}")  # Output: greet.__name__ is <lambda>

# Scenario2: Lambda function with single argument
print("Scenario2: Simple lambda function")
squared = lambda x: x**2
print(f"  The square of 5 is {squared(5)}")  # Output: The square of 5 is 25

# Scenario3: Lambda function with multiple arguments
print("Scenario3: Lambda function with multiple arguments")
add = lambda x, y: x + y
print(f"  The sum of 5 and 10 is {add(5, 10)}")  # Output: The sum of 5 and 10 is 15

# Scenario4: Lambda function with default argument
print("Scenario4: Lambda function with default argument")
power = lambda x, y=2: x**y
print(f"  5 squared is {power(5)}")  # Output: 5 squared is 25
print(f"  5 cubed is {power(5, 3)}")  # Output: 5 cubed is 125

# Scenario5: Lambda function with variable number of arguments
print("Scenario5: Lambda function with variable number of arguments")
concat = lambda *args: " ".join(args)
print(
    f"  Concatenation of 'Hello', 'World' is: {concat('Hello', 'World')}"
)  # Output: Concatenation of 'Hello', 'World' is: Hello World

# Scenario6: Lambda function with conditional expression
print("Scenario6: Lambda function with conditional expression")
max_value = lambda a, b: a if a > b else b
print(f"  The maximum of 5 and 10 is {max_value(5, 10)}")  # Output: The maximum of 5 and 10 is 10

# Scenario7: Lambda function with multiple lines in the body
print("Scenario7: Lambda function with multiple lines in the body")
multi_line = lambda x: (x**2, x**3)
print(f"  The square and cube of 5 are: {multi_line(5)}")

# Scenario8: Complex lambda function
# Note:
#   This lambda function uses the walrus operator (:=) for assignment
#   expressions. The walrus operator allows us to assign values to
#   variables as part of an expression, making it easier to work with
#   intermediate results.
print("Scenario8: Complex lambda function")
complex_func = lambda x: (
    (
        y := x + 1,
        z := y * 2,
        w := z - 3,
    ),
    (
        print(f"  Intermediate values: y={y}, z={z}, w={w}"),
        w,
    ),
)[1]
print(f"  Final result is: {complex_func(5)}")

numbers = [1, 2, 3, 4, 5]

# Python map function
print("Python map function")
squared_numbers = map(lambda x: x**2, numbers)
print(f"  Squared numbers: {list(squared_numbers)}")

# Python filter function
print("Python filter function")
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"  Even numbers: {list(even_numbers)}")

# Python reduce function
print("Python reduce function")
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print(f"  Product of numbers: {product}")

# Python reduce function with initial value
print("Python reduce function with initial value")
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(f"  Sum of numbers with initial value 10: {sum_with_initial}")

# Defining higher-order functions using lambda
print("Defining higher-order functions using lambda")


def apply_function(func, value):
    return func(value)


result = apply_function(lambda x: x + 5, 10)
print(f"  Result of applying lambda function: {result}")
