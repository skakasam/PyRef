"""Python Built-in Functions Practice Module"""

################################################################################
# Python Built-in Functions
################################################################################
# Python has several built-in functions that can be used with lambda functions.
# These functions are often higher-order functions that take other functions as
# arguments or return them as results.
################################################################################
# The following are some common built-in functions:
#   1. abs()        :: The abs function returns the absolute value of a number.
#   2. all()        :: The all function returns True if all elements of the
#                      iterable are true.
#   3. any()        :: The any function returns True if any element of the
#                      iterable is true.
#   4. callable()   :: The callable function returns True if the object appears
#                      callable.
#   5. delattr()    :: The delattr function deletes an attribute from an object.
#   6. enumerate()  :: The enumerate function adds a counter to an iterable and
#                      returns it as an enumerate object.
#   7. eval()       :: The eval function parses the expression and executes it.
#   8. exec()       :: The exec function executes the Python code in the given
#                      string.
#   9. filter()     :: The filter function constructs an iterator from elements
#                      of an iterable for which a function returns true.
#  10. getattr()    :: The getattr function returns the value of a named attribute
#                      of an object.
#  11. globals()    :: The globals function returns a dictionary representing the
#                      current global symbol table.
#  12. hasattr()    :: The hasattr function returns True if the object has the
#                      named attribute.
#  13. id()         :: The id function returns the identity of an object.
#  14. input()      :: The input function reads a line from input, converts it
#                      to a string, and returns it.
#  15. isinstance() :: The isinstance function checks if an object is an instance
#                      of a class or a tuple of classes.
#  16. issubclass() :: The issubclass function checks if a class is a subclass of
#                      another class.
#  17. iter()       :: The iter function returns an iterator object.
#  18. len()        :: The len function returns the number of items in an object.
#  19. locals()     :: The locals function returns a dictionary representing the
#                      current local symbol table.
#  20. map()        :: The map function applies a function to all items in an input
#                      list.
#  21. max()        :: The max function returns the largest item in an iterable or
#                      the largest of two or more arguments.
#  22. min()        :: The min function returns the smallest item in an iterable or
#                      the smallest of two or more arguments.
#  23. next()       :: The next function retrieves the next item from an iterator.
#  24. pow()        :: The pow function returns the value of x to the power of y.
#  25. print()      :: The print function prints the given object to the console.
#  26. property()   :: The property function returns a property attribute for a class.
#  27. range()      :: The range function returns an immutable sequence of numbers.
#  28. repr()       :: The repr function returns a string representation of an object.
#  29. round()      :: The round function rounds a number to a specified number of
#                      decimal places.
#  30. setattr()    :: The setattr function sets the value of a named attribute of
#                      an object.
#  31. sorted()     :: The sorted function returns a new sorted list from the elements
#                      of any iterable.
#  32. sum()        :: The sum function sums the items of an iterable.
#  33. zip()        :: The zip function combines two or more iterables into tuples.
################################################################################

# abs() function example
print("abs() function example:")
print(f"  abs(-5) = {abs(-5)}")
print(f"  abs(3.14) = {abs(3.14)}")

# all() function example
print("all() function example:")
print(f"  all([True, True, False]) = {all([True, True, False])}")
print(f"  all([True, True, True]) = {all([True, True, True])}")

# any() function example
print("any() function example:")
print(f"  any([False, False, True]) = {any([False, False, True])}")
print(f"  any([False, False, False]) = {any([False, False, False])}")

# callable() function example
print("callable() function example:")
print(f"  callable(5) = {callable(5)}")
print(f"  callable(abs) = {callable(abs)}")
print(f"  callable(lambda x: x + 1) = {callable(lambda x: x + 1)}")

# delattr() function example
print("delattr() function example:")


class MyClass1:
    def __init__(self):
        self.my_attr = 42


obj = MyClass1()
print(f"  Before delattr: {obj.my_attr}")
delattr(obj, "my_attr")
print(f"  After delattr: {hasattr(obj, 'my_attr')}")

# enumerate() function example
print("enumerate() function example:")
my_list = ["a", "b", "c"]
for index, value in enumerate(my_list):
    print(f"  Index: {index}, Value: {value}")

# eval() function example
print("eval() function example:")
x = 10
print(f"  eval('x + 1') = {eval('x + 1')}")

# exec() function example
print("exec() function example:")
code = "for i in range(3): print(f'  exec: {i}')"
exec(code)

# getattr() function example
print("getattr() function example:")


class MyClass2:
    def __init__(self):
        self.my_attr = 42


obj = MyClass2()
print(f"  getattr(obj, 'my_attr') = {getattr(obj, 'my_attr')}")
print(f"  getattr(obj, 'unknown_attr', 'default') = {getattr(obj, 'unknown_attr', 'default')}")


# globals() function example
print("globals() function example:")
print(f"  globals()['x'] = {globals().get('x', 'not found')}")
print(f"  globals()['y'] = {globals().get('y', 'not found')}")

# hasattr() function example
print("hasattr() function example:")
print(f"  hasattr(obj, 'my_attr') = {hasattr(obj, 'my_attr')}")
print(f"  hasattr(obj, 'unknown_attr') = {hasattr(obj, 'unknown_attr')}")

# id() function example
print("id() function example:")
print(f"  id(obj) = {id(obj)}")

# isinstance() function example
print("isinstance() function example:")
print(f"  isinstance(obj, MyClass) = {isinstance(obj, MyClass1)}")
print(f"  isinstance(obj, dict) = {isinstance(obj, dict)}")

# issubclass() function example
print("issubclass() function example:")
print(f"  issubclass(MyClass, object) = {issubclass(MyClass1, object)}")
print(f"  issubclass(MyClass, dict) = {issubclass(MyClass1, dict)}")

# iter() and next() function example
print("iter() and next() function example:")
my_list = [1, 2, 3]
my_iter = iter(my_list)
print(f"  next(my_iter) = {next(my_iter)}")
print(f"  next(my_iter) = {next(my_iter)}")
print(f"  next(my_iter) = {next(my_iter)}")
try:
    print(f"  next(my_iter) = {next(my_iter)}")
except StopIteration:
    print("  next(my_iter) = No more items. StopIteration raised!")

# locals() function example
print("locals() function example:")
print(f"  locals()['x'] = {locals().get('x', 'not found')}")
print(f"  locals()['y'] = {locals().get('y', 'not found')}")

# max() function example
print("max() function example:")
print(f"  max([1, 2, 3]) = {max([1, 2, 3])}")
print(f"  max('abc') = {max('abc')}")

# min() function example
print("min() function example:")
print(f"  min([1, 2, 3]) = {min([1, 2, 3])}")
print(f"  min('abc') = {min('abc')}")

# property() function example
print("property() function example:")


class MyClass3:
    def __init__(self, attr):
        self._attr = attr

    attr = property(
        fget=lambda self: self._attr,
        fset=lambda self, value: setattr(self, "_attr", value),
    )

    def __repr__(self):
        return f"MyClass(attr={self._attr})"


obj = MyClass3(42)
print(f"  [Before] obj.attr = {obj.attr}")
obj.attr = 84
print(f"  [After] obj.attr = {obj.attr}")

# repr() function example
print("repr() function example:")
print(f"  repr(obj) = {repr(obj)}")

# round() function example
print("round() function example:")
print(f"  round(4.29) = {round(4.29)}")
print(f"  round(4.73) = {round(4.73, 1)}")

# setattr() function example
print("setattr() function example:")
print(f"  [Before] obj.attr = {obj.attr}")
setattr(obj, "attr", 168)
print(f"  [After] obj.attr = {obj.attr}")

# sorted() function example - returns a new sorted iterable
print("sorted() function example:")
print(f"  sorted([3, 1, 2]) = {sorted([3, 1, 2])}")
print(f"  sorted('cba') = {sorted('cba')}")

# sum() function example
print("sum() function example:")
print(f"  sum([1, 2, 3]) = {sum([1, 2, 3])}")

# zip() function example
print("zip() function example:")
print(f"  zip([1, 2, 3], ['a', 'b', 'c']) = {list(zip([1, 2, 3], ['a', 'b', 'c']))}")
