"""Python Generators Practice Module"""

################################################################################
# Python Generators are a simpler way to create iterators using the `yield`
# keyword. They allow you to define an iterative algorithm by writing a function
# that can be paused and resumed, maintaining its state between calls.
#
#    ============================      ====================================
#    FUNCTION                      vs  GENERATOR
#    ============================      ====================================
# 1. Uses return statement             Uses yield statement
# 2. Returns a single value            Can return multiple values over time
# 3. Cannot maintain state             Maintains state between calls
# 4. Consumes more memory              More memory efficient (lazy evaluation)
#
# Generator functions are like normal functions in most respects, and in fact are
# coded with normal def statements. However, when created, they are compiled into
# generator objects, which support the iterator protocol.
################################################################################


def count_up_to(max):
    current = 1
    while current <= max:
        yield current  # Yield pauses the function, returning current
        current += 1  # Resume from here on the next call


five_counter = count_up_to(5)  # Generator object that supports the iterator protocol

print("Functions vs Generators:")
print(f"  {type(count_up_to)=}")
print(f"  {type(five_counter)=}")
print(f"  {dir(five_counter)=}")

print("Counting up to 5:")
first_value = next(five_counter)
print(f"  1st value from generator: {first_value}")
second_value = next(five_counter)
print(f"  2nd value from generator: {second_value}")
for value in five_counter:
    print(f"  Next value from generator: {value}")
