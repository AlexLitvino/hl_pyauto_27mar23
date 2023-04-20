a = 3
b = 4
c = 5

def max_of_3(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    #max_ = None
    if a > b and a > c:
        max_ = a
        return a
    elif b > a and b > c:
        max_ = b
        return b
    elif c > a and c > b:
        max_ = c
        return c
    else:
        max_ = "All equals"
    return max_

    # def max_a():
    #     pass
    #
    # return

# print(max_of_3(1, 2, 5))
# print(max_of_3(b=1, c=2, a=5))
# print(max_of_3(1, c=2, b=5))
#print(max_of_3(c=1, 2, b=5))

# print(max_of_3)
#
# print(max_of_3(1, b, 6))

# def greetings(name):
#     print(f"Hello, {name}")
#
# print(greetings("Alex"))
#
#
# def perform_login(username, password):
#     pass
#
# print(perform_login('1', '2'))
#
# class A:
#     ...
#
# a = 33
# if a > 5:
#     pass
# else:
#     print("a < 5")
#
# def less_more(n):
#     return [n - 1, n + 1, "Success"]
#
# print(type(less_more(6)))
# a, b, s = less_more(6)
# print(a, b, s)

# c = input()
# CONST = 4
# def func(a, b=CONST):
#     print(f"a={a}, b={b}")
#
# func(1, 3)
# func(3)
# func(c, c)

#print(1, 3, "fdf", 53)

# def func(a1, *args, key):
#     print(a1)
#     print(args)
#     print(key)
#     s = 0
#     for i in args:
#         s += i
#     return s
#
# import logging
# a = func("a", key=333)
# print(a)
# a = func(1, 3, 4, 5, key=4344)
# print(a)

def func(pos, *args, key, **kwargs):
    print(pos)
    print(args)
    print(key)
    print(kwargs)
    # for i in kwargs:
    #     print(f"{i}: {kwargs[i]}")

func(1, 2, 3, key=232323, url=1, timeout=54, ht=7)
lst = [1, 2, 4]
print(*lst)
print()