"""Python Datatypes Conversions Practice Module"""

###############################################################################
# Types can be explicitly coverted into another types (if possible) using the
# builtin type as a function.
###############################################################################
price = 24.99
int_price = int(price)
print(f"price = {price}, floor_price = {int_price}")

marks = 75
str_marks = str(marks)
print(f"grade = {marks!r}, str_marks = {str_marks!r}")
