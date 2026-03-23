"""Python Numbers Practice Module"""

###############################################################################
# Numbers are immutable data types used to represent numeric values.
# They can be integers, floating-point numbers, or complex numbers.
###############################################################################
integer_value = 42
print(f"type(integer_value) = {type(integer_value)}")
print(f"integer_value = {integer_value}")  # Prints 42

float_value = 3.14
print(f"type(float_value) = {type(float_value)}")
print(f"float_value = {float_value}")  # Prints 3.14

complex_value = 1 + 2j
print(f"type(complex_value) = {type(complex_value)}")
print(f"complex_value = {complex_value}")  # Prints (1+2j)

################################################################################
# Arithmetic operations with numbers
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Floor Division (//)
# 6. Modulus (%)
# 7. Exponentiation (**)
################################################################################
a = 10
b = 3
print(a + b)  # Prints 13
print(a - b)  # Prints 7
print(a * b)  # Prints 30
print(a / b)  # Prints 3.3333333333333335 (division always returns a float)
print(a // b)  # Prints 3 (floor or integer division)
print(a % b)  # Prints 1 (remainder of division)
print(a**b)  # Prints 1000 (10 raised to the power of 3)

################################################################################
# Order of Operations - PEMDAS
#   1. Parantheses
#   2. Exponents
# 3/4. Multiplication and Division (evaluated from left to right)
# 5/6. Addition and Substraction (evaluated from left to right)
################################################################################
print(f"1 + 2 * 5 / 3 = {1 + 2 * 5 / 3}")
print(f"1 + 2 / 3 * 5 = {1 + 2 / 3 * 5}")

################################################################################
# Floating-point numbers
################################################################################
print(0.1 + 0.2)  # Prints 0.30000000000000004 due to floating-point precision issues
print(round(0.1 + 0.2, 2))  # Prints 0.3, rounding to 2 decimal places
print(f"Is 0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")

################################################################################
# Underscores in numeric literals for readability
################################################################################
universe_age = 13_800_000_000  # 13.8 billion years
print(universe_age)  # Prints 13800000000
