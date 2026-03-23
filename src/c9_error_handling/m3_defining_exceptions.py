"""Python Defining Custom Exceptions"""

################################################################################
# Defining Custom Exceptions
################################################################################
# Custom exceptions can be defined by creating a new class that subclasses
# the built-in Exception class. This allows for more specific exception types
# that can carry additional information or behavior.
#
# Example-1 (Basic Usage)
#   class CustomException(Exception):
#       pass
#
#   try:
#       raise CustomException("This is a custom exception")
#   except CustomException as e:
#       print(f"Caught a custom exception: {e}")
#
# Example-2 (With Additional Attributes):
#   class CustomExceptionWithAttributes(Exception):
#       def __init__(self, message, error_code):
#           self.message = message
#           self.error_code = error_code
#
#   try:
#       raise CustomExceptionWithAttributes("This is a custom exception", 404)
#   except CustomExceptionWithAttributes as e:
#       print(f"Caught a custom exception: {e.message} (Error code: {e.error_code})")
################################################################################


class InvalidCalcError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidCalcOperandError(InvalidCalcError):
    def __init__(self, operand_type, operand_value):
        self.message = (
            f"{operand_type.capitalize()} operand value ({operand_value}) "
            f"can't be converted to a number."
        )
