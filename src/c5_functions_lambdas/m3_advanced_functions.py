"""Python Advanced Functions Practice Module"""

################################################################################
# Higher-Order Functions
################################################################################
# A higher-order function is a function that takes another function as an argument,
# or returns a function as a result.
# This allows for more abstract and flexible code.
# Common examples include map(), filter(), and reduce().
################################################################################
# Closures
################################################################################
# A closure is a function that retains access to its lexical scope, even when
# the function is executed outside that scope.
# This allows for more powerful and flexible function behavior.
################################################################################


# Scenario1: Function taking another function as an argument
def en_greeting(name):
    return f"Hello, {name}!"


def fr_greeting(name):
    return f"Bonjour, {name}!"


def hof_greeting(lang_func, name):
    # Call the language-specific greeting function
    greeting = lang_func(name)
    # Wrap the return value with additional formatting and return it
    return f"[ {greeting} ]"


print(hof_greeting(en_greeting, "Harry"))  # Output: [ Hello, Harry! ]
print(hof_greeting(fr_greeting, "Bob"))  # Output: [ Bonjour, Bob! ]


# Scenario2: Function returning another function
def counter(start):
    count = start

    # The increment function is a closure that captures the lexical scope
    # of the count variable. The HOF returns the increment function, which
    # can be called later to increment the count, without needing to pass
    # the count variable explicitly (or) worrying about the implementation.
    def increment():
        nonlocal count
        count += 1
        return count

    # The decrement function is a closure too, which works similar to the
    # increment function.
    def decrement():
        nonlocal count
        count -= 1
        return count

    return increment, decrement


new_message, read_message = counter(10)
print(f"New message received ({new_message()} unread)")
print(f"One message read     ({read_message()} unread)")
print(f"New message received ({new_message()} unread)")

################################################################################
# Decorators
################################################################################
# A decorator is a function that takes another function and extends its behavior
# without explicitly modifying it.
# This is useful for cross-cutting concerns like logging, authentication, etc.
################################################################################
# This concept will be explored in the decorators section.
################################################################################
