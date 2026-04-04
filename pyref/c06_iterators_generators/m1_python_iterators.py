"""Python Iterators Practice Module"""

################################################################################
# Python Iterators and Iterables `Iterables return an iterator`
#
# Iterators:
# - Objects that allow traversal through a collection (e.g., lists, tuples)
# - Implement the iterator protocol (methods: __iter__() and __next__())
# - Example: list_iterator = iter([1, 2, 3])
#
# Iterables:
# - Objects that can return an iterator (e.g., all sequences are iterables)
# - Implement the __iter__() method
# - Example: my_list = [1, 2, 3]
#
# __iter__():
# - Returns the iterator object itself
# - Example: my_list.__iter__() returns an iterator for the list
#
# __next__():
# - Returns the next item from the iterator
# - Raises StopIteration when there are no more items
################################################################################


def for_each(my_iterable, my_function):
    print("  --START--")
    my_iterator = iter(my_iterable)
    while True:
        try:
            my_function(next(my_iterator))
        except StopIteration:
            print("  --END--")
            break


print("STRING ITERABLE:")
iterable_1 = "Hello, Python!"  # String iterable
for_each(iterable_1, lambda x: print(f"  {x}"))

print("LIST ITERABLE:")
iterable_2 = [1, 2, 3, 4, 5]  # List iterable
for_each(iterable_2, lambda x: print(f"  {x}"))


class Counter:
    def __init__(self, *, min=1, max):
        self.min = min
        self.max = max
        self.current = min

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


print("CUSTOM COUNTER ITERABLE:")
counter = Counter(max=5)
for_each(counter, lambda x: print(f"  {x}"))
