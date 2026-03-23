"""Tracing function calls with decorators."""

################################################################################
# Using Function Decorators to Trace Function Calls
################################################################################


# Using a enclosing scope to maintain state in a closure
def call_tracer_v1(func):
    call_count = 0

    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        result = func(*args, **kwargs)
        print(
            f"Call {call_count} to {func.__name__} "
            f"with args={args} and kwargs={kwargs} "
            f"returned {result}"
        )
        return result

    return wrapper


# Using function attributes to maintain state in a closure
def call_tracer_v2(func):
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


@call_tracer_v2
def sum_v1(a, b):
    return a + b


print(f"{sum_v1(3, 5)=}")
print(f"{sum_v1(10, 20)=}")

################################################################################
# Using Class Decorators to Trace Function Calls
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


@CallTracer
def sum_v2(a, b):
    return a + b


print(f"{sum_v2(3, 5)=}")
print(f"{sum_v2(10, 20)=}")
