import functools

def call_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@call_decorator
def add(a, b):
    """Adding two numbers"""
    return a + b

#add = call_decorator(add)

print(add(4, 7))
print(add(3, 7))
print(add.__name__)
print(add.__doc__)