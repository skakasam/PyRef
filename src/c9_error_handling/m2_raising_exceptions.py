"""Python Exception Raising Practice Module"""

################################################################################
# Python Exception Raising
################################################################################
# Exceptions can be raised intentionally using the raise statement. This is
# useful for signaling that an error or exceptional condition has occurred.
#
# The basic syntax of the raise statement is as follows:
#
# raise SomeException("Error message")
#
# This will raise an instance of SomeException with the specified error message.
#
# Custom exceptions can also be defined by creating a new class that
# subclasses the built-in Exception class.
#
# Syntax:
# raise [exception] from [active_exception]
#
# Note:
#   1. If no [exception] is specified, raise re-raises the exception that
#      is currently being handled, which is also known as the [active_exception]
#   2. If there isn't currently an [active_exception], a RuntimeError is raised.
#   3. Otherwise, raise evaluates the [exception] and raises it. It must be either
#      a subclass of BaseException or an instance of BaseException. If it is a class,
#      the exception instance will be obtained when needed by instantiating it with
#      no arguments.
#   4. The type of the exception is the exception instance's class, the value is
#      the instance itself.
#   5. A traceback is a report containing the function calls made in your code
#      at a specific point. It is normally created automatically when an exception
#      is raised and attached to it as the __traceback__ attribute. We can create
#      custom tracebacks by raising exceptions with a specific traceback using the
#      with_traceback() method.
#      ex: raise Exception("Foo error occurred").with_traceback(foo_error_traceback)
#   6. The from clause is used for exception chaining, allowing you to raise a new
#      exception while preserving the context of the original exception. If given,
#      the original exception is stored in the new exception's __cause__ attribute.
#      ex: raise RuntimeError("New error occurred") from e
################################################################################


def bar():
    root_error = RuntimeError("Root Error Message")
    resulting_error = RuntimeError("Resulting Error Message")
    raise resulting_error from root_error


def foo():
    bar()


if __name__ == "__main__":
    try:
        foo()
    except Exception as e:
        raise RuntimeError("Something bad happened!") from e
