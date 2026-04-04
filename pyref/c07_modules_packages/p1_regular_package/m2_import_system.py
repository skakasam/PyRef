"""Python Import System Practice"""

import sys

################################################################################
# Python Import System
################################################################################
# The import system in Python is responsible for locating and loading modules.
# It allows you to use code from other modules in your own code.
#
# The import system provides several ways to import modules, including:
# - Importing an entire module
#   (import module_name)
# - Importing specific attributes from a module
#   (from module_name import attribute_name)
# - Importing a module with an alias
#   (import module_name as alias_name)
# - Importing all attributes from a module // NOT RECOMMENDED!!
#   (from module_name import *)
#
# The import system also supports relative imports, allowing you to import modules
# based on their location within the package hierarchy.
# - from . import sibling_module
# - from .. import parent_module
# - from ... import grandparent_module
# - from .... import great_grandparent_module
################################################################################
# Module Search Path
################################################################################
# When you import a module, Python searches for a built-in modules listed in
# sys.builtin_module_names. If the module is not found, it continues searching
# in a list of directories given by the sys.path variable, in the following order:
# 1. The current directory (where the script is located)
# 2. The directories listed in the PYTHONPATH environment variable
# 3. The default installation directories for Python
################################################################################
import m1_modules_in_python

print("SYS.PATH:")
for index, path in enumerate(sys.path):
    print(f"{index:>02d}: {path}")
print()

################################################################################
# The dir() function
################################################################################
# The dir() function is a built-in Python function that returns a list of
# names in the current local scope or the attributes of an object.
# It is commonly used to inspect the contents of modules, classes, and
# instances.
################################################################################
print("DIR(m1_modules_in_python):")
for index, attribute in enumerate(dir(m1_modules_in_python)):
    print(f"{index:>02d}: {attribute:<30s} ({type(getattr(m1_modules_in_python, attribute))})")
print()

################################################################################
# Using Module Attributes
################################################################################
# You can access the attributes of a module using dot notation.
# For example, to access the 'some_function' attribute from the
# 'm1_modules_in_python' module, you would use:
# m1_modules_in_python.some_function
################################################################################
print(m1_modules_in_python.greet_user(name="Alice", lang_code="es"))
print(m1_modules_in_python.greet_user(name="Bob", lang_code="fr"))
print()
