# def call_decorator(func):
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         print(f"{func.__name__} called {wrapper.count} times")
#         return func(*args, **kwargs)
#     wrapper.count = 0
#     return wrapper

# import functools
#
# class CallDecorator:
#
#     def __init__(self, func):
#         self.func = func
#         self.count = 0
#         functools.update_wrapper(self, func)
#
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#
#         print(f"{self.func.__name__} called {self.count} times")
#
#         results = self.func(*args, **kwargs)
#
#         return results
#
#
# #add = CallDecorator()(add)
#
# @CallDecorator
# def add(a, b):
#     """Docstrings"""
#     return a + b
#
# print(add(4, 7))
# print(add(3, 7))
# print(add.__name__)
# print(add.__doc__)

class CallDecorator:

    def __init__(self, header):
        self.header = header
        self.count = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.count += 1
            print(self.header)
            print(f"{func.__name__} called {self.count} times")

            results = func(*args, **kwargs)

            return results
        return wrapper


class User:

    def __init__(self, name):
        self.name = name

    @CallDecorator("CALLED")
    def print_name(self):
        print(f"I'm {self.name}")

john = User('John')
john.print_name()
john.print_name()