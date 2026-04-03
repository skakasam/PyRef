"""Python Functions Odds and Ends"""


# Functions can be passed around as arguments to other functions.
def singler(x):
    """Return the single of x."""
    return 1 * x


def doubler(x):
    """Return the double of x."""
    return 2 * x


def triple(x):
    """Return the triple of x."""
    return 3 * x


multipliers = [(singler, 5), (doubler, 10), (triple, 6)]

for func, value in multipliers:
    print(f"{func.__name__}({value})={func(value)}")


# Functions can created as closures to retain state from enclosing scope
def make_multiplier(factor):
    def multiplier(x):
        return factor * x

    return multiplier


doubler = make_multiplier(2)
tripler = make_multiplier(3)

print(doubler(5))
print(tripler(5))


# Function introspection
greeting_by_language = {
    "arabic": "مرحبا",
    "bengali": "হ্যালো",
    "chinese": "你好",
    "dutch": "Hallo",
    "english": "Hello",
    "french": "Bonjour",
    "german": "Hallo",
    "hindi": "नमस्ते",
    "italian": "Ciao",
    "japanese": "こんにちは",
    "korean": "안녕하세요",
    "lativian": "Labas",
    "malayalam": "ഹലോ",
    "norwegian": "Hallo",
    "oromo": "Akkam",
    "polish": "Cześć",
    "portuguese": "Olá",
    "quechua": "¡Hola!",
    "russian": "Здравствуйте",
    "romanian": "Bună ziua",
    "spanish": "¡Hola!",
    "swedish": "Hej!",
    "tamil": "வணக்கம்",
    "telugu": "నమస్కారం",
    "ukrainian": "Привіт",
    "vietnamese": "Xin chào",
    "welsh": "Helo",
    "xhosa": "Molo",
    "yiddish": "העלא",
    "zulu": "Sawubona",
}


def greet(name: str, lang: str = "english") -> str:
    """Return a greeting message."""
    greeting = greeting_by_language.get(lang, "Hello")
    return f"{greeting}, {name}!"


print("--> FUNCTION INTROSPECTION <--")
print(f"{greet('Alice') = }")  # Call the function
print(f"{greet.__name__ = }")  # Function name
print(f"{greet.__doc__ = }")  # Function docstring
print(f"{greet.__code__.co_varnames = }")  # Function argument names
print(f"{greet.__code__.co_argcount = }")  # Function argument count

# Function annotations
print("--> FUNCTION ANNOTATIONS <--")
for arg, annotation in greet.__annotations__.items():
    print(f"{arg}: {annotation}")
