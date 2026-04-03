"""Class Pitfalls with Decorators"""


################################################################################
# Don't use Class Decorators to decorate Class Methods
################################################################################
class CallTracer:
    def __init__(self, func):  # on @ decoration, save original function
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):  # on later calls, do extra work
        self.call_count += 1
        result = self.func(*args, **kwargs)
        print(
            f"Call {self.call_count} to {self.func.__name__} "
            f"with args={args} and kwargs={kwargs} "
            f"returned {result}"
        )
        return result


class OrderProcessor:
    @CallTracer
    def process_order(self, order_id):
        print(f"Processing order {order_id}")


# OrderProcessor().process_order(123) This will not work becasue the self argument
# in the CallTracer is of the CallTracer instance, not the OrderProcessor instance.


################################################################################
# Use Function Decorators to decorate Class Methods
################################################################################
def call_tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1  # type: ignore
        result = func(*args, **kwargs)
        print(
            f"Call {wrapper.call_count} to {func.__name__} "  # type: ignore
            f"with args={args} and kwargs={kwargs} "
            f"returned {result}"
        )
        return result

    wrapper.call_count = 0  # type: ignore
    return wrapper


class User:
    def __init__(self, username):
        self.username = username

    @call_tracer
    def login(self, otp):
        print(f"User {self.username} logged in using {otp} OTP")


User("alice").login("123456")  # This will work because the decorator propagates the
# self argument as the first item of the *args tuple, so the decorated method has access
# to the instance of the class.
