"""Python Intermediate Functions Practice Module"""


################################################################################
# Functions that allow positional arguments only
# All arguments before / must be specified as positional arguments
################################################################################
def positional_greet(name, greeting="Hello", /):
    print(f"{greeting}, {name}!")


positional_greet("Alice")
positional_greet("Anand", "Namaste")
# salut(name="Anand", greeting="Namaste")  # This will raise a TypeError


################################################################################
# Functions that allow keyword arguments only
# All arguments after * must be specified as keyword arguments
################################################################################
def keyword_greet(*, name, greeting="Hello"):
    print(f"{greeting}, {name}!")


keyword_greet(name="Alice")
keyword_greet(name="Anand", greeting="Namaste")
# greet("Anand", "Namaste")  # This will raise a TypeError


################################################################################
# Functions that allow a combination of both
# All arguments before / must be specified as positional arguments
# All arguments after * must be specified as keyword arguments
# All arguments after / and before * could be either positional or keyword
################################################################################
def picky_greet(name, /, title="", *, lang="en"):
    if title:
        name = f"{title} {name}"

    if lang == "fr":
        greeting = "Bonjour"
    elif lang == "es":
        greeting = "Hola"
    elif lang == "de":
        greeting = "Hallo"
    elif lang == "it":
        greeting = "Ciao"
    elif lang == "jp":
        greeting = "こんにちは"
    elif lang == "in":
        greeting = "नमस्ते"
    elif lang == "cn":
        greeting = "你好"
    elif lang == "ru":
        greeting = "Здравствуйте"
    elif lang == "ar":
        greeting = "مرحبا"
    else:
        greeting = "Hello"

    print(f"{greeting}, {name}!")


picky_greet("Alice")
picky_greet("Bob", "Mr.", lang="fr")
picky_greet("Charlie", title="Dr.", lang="es")
