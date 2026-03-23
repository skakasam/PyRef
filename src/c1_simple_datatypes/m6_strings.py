"""Python Strings Practice Module"""

###############################################################################
# Strings are immutable sequences of unicode characters used to represent
# textual data. They can be defined using single quotes, double quotes,
# or triple quotes. However, be consistent in the quotes usages.
###############################################################################
greeting_1 = "Welcome to Python!"
print(greeting_1)

greeting_2 = """Welcome to Python with triple quotes!
This allows for multi-line strings."""
print(greeting_2)

###############################################################################
# Adding escape sequences (tabs or newlines) in strings
###############################################################################
print("Novus,\\Skills!")  # Prints "Novus," followed by a backslash, and finally "Skills!"
print("Novus,\vSkills!")  # Prints "Novus," followed by a vertical tab and "Skills!"
print("Novus,\nSkills!")  # Prints "Novus," followed by "Skills!" on a new line
print("Novus,\tSkills!")  # Prints "Novus," followed by a tab and "Skills!"

###############################################################################
# String Concatenation & Formatting
# 1. Concatenation Operator (+)
# 2. f-strings (formatted string literals)
# 3. str.format() method
# 4. Old-style formatting with % operator
###############################################################################
first_name = "Novus"
last_name = "Skills"
full_name_1 = first_name + " " + last_name
print(full_name_1)  # Prints "Novus Skills"
full_name_2 = f"{first_name} {last_name}"
print(full_name_2)  # Prints "Novus Skills"
full_name_3 = "{0} {1}".format(first_name, last_name)
print(full_name_3)  # Prints "Novus Skills"
full_name_4 = "%s %s" % (first_name, last_name)
print(full_name_4)  # Prints "Novus Skills"

###############################################################################
# Changing case of strings
# 1. title() - Capitalizes the first letter of each word
# 2. upper() - Converts all characters to uppercase
# 3. lower() - Converts all characters to lowercase
###############################################################################
label = "novus skills"
print(f"type(label) = {type(label)}")
print(label.title())  # Prints "Novus Skills"
print(label.upper())  # Prints "NOVUS SKILLS"
print(label.lower())  # Prints "novus skills"

###############################################################################
# Stripping whitespaces from strings wuth strip(), lstrip(), and rstrip()
###############################################################################
label = "   Novus Skills   "
print(f"`{label.strip()}`")  # Removes leading and trailing spaces
print(f"`{label.lstrip()}`")  # Removes leading spaces
print(f"`{label.rstrip()}`")  # Removes trailing spaces

###############################################################################
# Removing prefizes and suffixes from strings with remprefix() and remsuffix()
###############################################################################
url = "https://novusskills.com"
print(url.removesuffix(".com"))  # Removes ".com" suffix
print(url.removeprefix("https://"))  # Removes "https://" prefix
print(url.removeprefix("http://").removesuffix(".org"))  # No change
print(url.removeprefix("https://").removesuffix(".com"))  # Prints "novusskills"

###############################################################################
# Strings and Indexes
###############################################################################
message = "Python is awesome!"
print(f"message           = {message}")
print(f"message[0:6]      = {message[0:6]}")
print(f"message[10:17]    = {message[10:17]}")

###############################################################################
# Raw Strings
###############################################################################
project_path = r"C:\Users\NovusSkills\Projects\Python\\"
print(project_path[:-1])  # Prints the raw string with backslashes

###############################################################################
# F-Strings for String Interpolation
# Syntax:
# f"...literal...{expression [=] [!s, !r, or !a] [:formatspec]}...literal..."
#
# Where:
# - `expression` is any valid Python expression
# - `=` allows you to assign a name to the expression
# - `!s`, `!r`, and `!a` are conversion flags for string, repr, and ascii
# - `:formatspec` allows you to specify a format for the output
#   - [[fill]align][sign][z][#][0][width][grouping][.precision][typecode]
#   - fill can be any fill character other than `{` or `}`
#   - align can be `<` (left), `>` (right), `=` (padding after the sign) or `^` (center)
#   - sign can be `+`, `-`, or a space (to use a space for positive numbers)
#   - z is for zero-padding
#   - # is for alternate formatting
#   - 0 is for leading zeros
#   - width is the minimum width
#   - grouping is for thousands separators
#   - .precision is for decimal places
#   - typecode is for the type of formatting (e.g., d for integers, f for floats)
###############################################################################
name = "Novus Skills"
print(f"Hello, {name}!")  # Prints "Hello, Novus Skills!"
price = 29.99
print(f"{price=:<5.2f}")  # Prints "price=29.99"
