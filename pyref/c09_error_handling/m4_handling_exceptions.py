"""Python Exception Handling Practice Module"""

from m3_defining_exceptions import InvalidCalcError, InvalidCalcOperandError

################################################################################
# Python Exception Handling
################################################################################
# Exception handling in Python is done using the try-except block. This allows
# developers to catch and handle exceptions gracefully, preventing crashes and
# providing meaningful error messages.
#
# The basic syntax of a try-except block is as follows:
#
# try:
#     # Code that may raise an exception
# except SpecificException as e:
#     # Code to handle the specific exception
# except GenericException as e:
#     # Code to handle the generic exception
# except Exception as e:
#     # Code to handle any other exception
#     # re-raise the exception
#     raise UnknownException("An unknown error occurred") from e
# else:
#     # Code to run if no exception was raised
# finally:
#     # Code to run regardless of whether an exception was raised or not
#
# Multiple exceptions can be caught by using multiple except blocks or by
# specifying a tuple of exceptions.
#
# Additionally, a finally block can be used to specify cleanup code that
# should run regardless of whether an exception was raised or not.
################################################################################


def do_calc(expression: str):
    try:
        left_operand, operator, right_operand = expression.split(" ")
    except ValueError as ve:
        raise InvalidCalcError(
            "Invalid expression format. Make sure to use the format:"
            " 'left_operand operator right_operand'"
            "\nWhere 'left_operand' and 'right_operand' are numbers"
            ", and 'operator' is one of: +, -, *, /"
        ) from ve

    try:
        left_operand = int(left_operand)
    except ValueError as ve:
        raise InvalidCalcOperandError("left", left_operand) from ve

    try:
        right_operand = int(right_operand)
    except ValueError as ve:
        raise InvalidCalcOperandError("right", right_operand) from ve

    if operator == "+":
        return left_operand + right_operand
    elif operator == "-":
        return left_operand - right_operand
    elif operator == "*":
        return left_operand * right_operand
    elif operator == "/":
        return left_operand / right_operand
    else:
        raise InvalidCalcError(f"{operator} operation is not supported!")


print("Enter a space-separated expression. Ex: 2 + 3, 4 * 5 etc.")
running = True
while running:
    try:
        expression = input("Expression: ")
        result = do_calc(expression)
    except InvalidCalcOperandError as ave:
        print(ave)
    except InvalidCalcError as ce:
        print(ce)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        running = False
    else:
        print(result)
