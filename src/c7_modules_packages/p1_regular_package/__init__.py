"""Python Package for Demonstrating Modules in Python"""

print(f"Importing {__name__}")

################################################################################
# Python __init__.py File
################################################################################
# Python’s special __init__.py file marks a directory as a regular Python package
# and allows you to import its modules. This file runs automatically the first
# time you import its containing package. You can use it to initialize metadata,
# package-level variables, define functions or classes, and structure the
# package’s namespace clearly for users.
################################################################################

################################################################################
# Package Metadata
################################################################################
__version__ = "1.0.0"
__author__ = "Surya Akasam"
__email__ = "surya.akasam@outlook.com"
__description__ = "A package for demonstrating modules in Python."

################################################################################
# Controlling the Package imports using __all__
################################################################################
from .m1_modules_in_python import greet_user, supported_languages, UnsupportedLanguageError

__all__ = ["greet_user", "supported_languages", "UnsupportedLanguageError"]
