"""Python Modules Practice"""

print(f"Importing {__name__}")

from collections import namedtuple

################################################################################
# Python Modules
################################################################################
# A module is a file containing Python code. It can define functions, classes,
# and variables. Modules allow for code reusability and organization.
#
# Definitions from a module can be imported into other modules or into the main
# module (the collection of variables that you have access to in a script executed
# at the top level)
################################################################################

# Modules can have class definitions
_Language = namedtuple("Language", ["code", "name", "greeting"])

# Modules can have constants
__LANGUAGES = (
    _Language("en", "English", "Hello"),
    _Language("zh", "Chinese", "你好"),
    _Language("hi", "Hindi", "नमस्ते"),
    _Language("es", "Spanish", "Hola"),
    _Language("ar", "Arabic", "مرحبا"),
    _Language("fr", "French", "Bonjour"),
    _Language("bn", "Bengali", "হ্যালো"),
    _Language("pt", "Portuguese", "Olá"),
    _Language("ru", "Russian", "Здравствуйте"),
    _Language("ur", "Urdu", "ہیلو"),
    _Language("id", "Indonesian", "Halo"),
    _Language("de", "German", "Hallo"),
    _Language("ja", "Japanese", "こんにちは"),
    _Language("sw", "Swahili", "Habari"),
    _Language("mr", "Marathi", "नमस्कार"),
    _Language("te", "Telugu", "హలో"),
    _Language("vi", "Vietnamese", "Xin chào"),
    _Language("tr", "Turkish", "Merhaba"),
    _Language("it", "Italian", "Ciao"),
    _Language("ta", "Tamil", "வணக்கம்"),
    _Language("fi", "Filipino", "Kamusta"),
    _Language("ko", "Korean", "안녕하세요"),
    _Language("pr", "Persian", "سلام"),
    _Language("jv", "Javanese", "Halo"),
    _Language("th", "Thai", "สวัสดี"),
    _Language("pl", "Polish", "Cześć"),
    _Language("uk", "Ukrainian", "Привіт"),
    _Language("pa", "Punjabi", "ਸਤ ਸ੍ਰੀ ਅਕਾਲ"),
)


# Modules can have custom exceptions
class UnsupportedLanguageError(Exception):
    """Custom Exception for unknown language codes"""

    def __init__(self, lang_code):
        super().__init__(f"Language `{lang_code}` not supported yet!")


# Modules can have function definitions
def supported_languages():
    """Return a list of supported languages."""
    return {lang.code: lang.name for lang in __LANGUAGES}


def greet_user(*, name, lang_code="en"):
    """Print a greeting in the specified language.

    Args:
        name (str): The name of the user.
        lang_code (str, optional): The language code for the greeting. Defaults to "en".

    Raises:
        UnsupportedLanguageError: If the language code is not supported.

    Returns:
        str: A greeting message in the specified language.
    """
    lang = next((lang for lang in __LANGUAGES if lang.code == lang_code), None)
    if lang:
        return f"{lang.name} Greeting: {lang.greeting}, {name}!"
    raise UnsupportedLanguageError(lang_code)


################################################################################
# Executing Modules
################################################################################
# To execute a module, you can use the `import` statement in another module or
# in the main module. When a module is imported, its code is executed, and any
# top-level variables, functions, and classes are made available.
#
# You can also use the `if __name__ == "__main__":` construct to allow or prevent
# parts of code from being run when the modules are imported.
################################################################################
if __name__ == "__main__":
    print("Supported Languages:")
    counter = 1
    for code, name in supported_languages().items():
        info = f"  {code}: {name}"
        print(f"{info:<18s}", end=("\n" if (counter % 7) == 0 else ""))
        counter += 1

    lang_code = input("Enter Lang Code: ")
    user_name = input("Enter Your Name: ")
    print(greet_user(name=user_name, lang_code=lang_code))
