# def binary_func(func, a, b):
#     return func(a, b)
#
# def add(x, y):
#     return x + y
#
# print(binary_func(lambda x, y: x + y, 3, 7))
# print(binary_func(lambda x, y: x - y, 3, 7))
#
#
# def binary_func(name):
#     def add(x, y):
#         return x + y
#
#     def sub(x, y):
#         return x - y
#
#     if name == 'add':
#         return add
#     elif name == 'sub':
#         return sub
#     else:
#         print("Unknown function")
#
# print(binary_func('sub')(6, 3))
# func = binary_func('sub')
# print(func(6, 3))
#
#
# def add(x, y):
#     return x + y
#
# sum_ = add
# add = None
# print(sum_(3,7))


# def greetings(name):
#     return f"Hello, {name}"

# <i> </i>
#print(greetings("Anna"))

# def italic_decorator(func):
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#     return wrapper
#
# # def greetings_with_italic(name):
# #     return f"<i>{greetings(name)}</i>"
#
# # greetings_with_italic = italic_decorator(greetings)
# # print(greetings_with_italic("Anna"))
#
# @italic_decorator
# def greetings(name, cat):
#     return f"Hello, {name} and {cat}"
#
# #greetings = italic_decorator(greetings)
# print(greetings("Anna", "Murzik"))


# def italic_decorator(func):
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#     return wrapper
#
#
# def bold_decorator(func):
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"
#     return wrapper
#
#
# @italic_decorator
# @bold_decorator
# def greetings(name, cat):
#     return f"Hello, {name} and {cat}"
#
# #greetings = bold_decorator(italic_decorator(greetings))
#
# print(greetings("Anna", "Murzik"))


def italic_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def style_decorator(style):
    def param_decorator(func):



        def wrapper(*args, **kwargs):
            return f"<{style}>{func(*args, **kwargs)}</{style}>"
        return wrapper
    return param_decorator


@style_decorator('i')
@style_decorator('b')
def greetings(name, cat):
    return f"Hello, {name} and {cat}"

print(greetings("Anna", "Murzik"))

import math
import functools
import time

@functools.cache
def custom_sqrt(n):
    return math.sqrt(n)

t1 = time.perf_counter()
custom_sqrt(17)
t2 = time.perf_counter()
print(f"{t2 - t1}")

t1 = time.perf_counter()
custom_sqrt(17)
t2 = time.perf_counter()
print(f"{t2 - t1}")












