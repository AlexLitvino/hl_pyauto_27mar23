"""
abs
divmod
round
pow
"""

# print(abs(-5))
# print(abs(3-4j))
# print(divmod(14, 3))  # //, %
# print(round(4.6666, 2))  # math floor, ceil, trunc
# print(pow(2, 3, 5))  # **

"""
all
any
callable
"""

# print(all([1, 2, 3, ""]))
# print(all([]))
# lst = [1, 3, '']
# print(bool(all(lst) and lst))
#
# print(any([0, ""]))
# print(any([]))
#
# def add(a, b):
#     return a + b
#
# print(callable(add))
# print(callable(lambda x: x + 1))
# print(callable("sssdcdaf"))


"""
len
max
min
range
reversed
sorted
sum
"""

# print(max(1, 2, 3))
# print(max([1, 2, 3]))
# print(max([], default=None))
#
# persons = [{'name': 'John', 'age': 34},
#            {'name': 'Anna', 'age': 24}]
#
# print(max(persons, key=lambda person: person['age']))
#
# lst = list(range(10))
# print(list(reversed(lst)))
# print(lst)
#
# lst = [5, 2, 7, 4]
# # print(lst.sort())
# # print(lst)
# lst_sorted = sorted(lst)
# print(lst)
# print(lst_sorted)
#
# persons = [{'name': 'John', 'age': 34},
#            {'name': 'Oksana', 'age': 24},
#            {'name': 'Anna', 'age': 24},
#            {'name': 'James', 'age': 34}]
#
# print(sorted(persons, key=lambda person: person['age']))
# print(sorted(persons, key=lambda person: (person['age'], person['name'])))
# # 24-Feb-23
#
# print(sum([1, 2, 4], start=100))

"""
enumerate
filter
map
zip
reduce*
"""

# lst = ['a', 'b', 'c']
# for index, item in enumerate(lst, start=3):
#     print(f"index ({index}), item ({item})")

# lst = list(map(int, ['1', '22', '23234']))
# print(lst)
#
# lst = ['1', '22', '23234']
# print([int(item) for item in lst])

# lst = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
# print(lst)

# lst = filter(lambda x: x >= 0, [-4, 5, -2, 7])
# print(lst)
# print(list(lst))
#
# #strings = ['t4trr', '', '', '35ttgwtwyhtt']
# strings = ['', '', '']
# filtered_strings = filter(None, strings)
# if filtered_strings:
#     print("SUCCESS, HAVE VALID STRINGS")
# else:
#     print("FAIL")
#
# print(list(filtered_strings))

# lst1 = [1, 2, 3, 4, 5]
# lst2 = "abcde"
# lst3 = [11, 22, 33, 44, 55]
# #print(list(zip(lst1, lst2, lst3)))
# #print(list(zip(lst1)))
#
# lst1 = [1, 2, 3, 4, 5, 6]
# lst2 = "abcde"
# print(list(zip(lst1, lst2)))
# print(list(zip(lst2, lst1)))
# #print(list(zip(lst1, lst2, strict=True)))
#
# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# lst2 = list(zip(*lst))
# print(lst2)

# from functools import reduce
#
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
# """
# [1, 2, 3, 4]
# [3, 3, 4]
# [6, 4]
# [10]
# """
#
# print(reduce(lambda x, y: x + y, [[1, 2, 3, [5, 5]], [4, 5, 6]]))

"""
chr
ord
"""

# print(ord('k'))
# print(chr(107))
import string
#char in strings

# print(bin(10))
# print(f"{17:b}")

"""
ascii
repr
str
format
"""

# lst = [1, 2, 3]
# print(str(lst))
#
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(str(now))  # __str__
# print(repr(now))  # __repr__
# print(ascii('Привет Hello'))
#
# print(f"{now!r}")
#
# a = 3.676543
# print(f"{a:.2}")
# print(format(a, '.2'))
#
# # now2 = eval("datetime.datetime(2023, 5, 1, 21, 26, 12, 437120)")
# # print(now2)

# byte_s = bytes("qwerty", encoding='ascii')  # \x71\x
# print(repr(byte_s))

# byte_s = bytes('Привет', encoding='UTF-8')
# print(byte_s)
#
# for i in dir(byte_s):
#     print(i)

# print(type(3))
# print(type(type(3)))
# a = 3434
# #print(type(a) == type(0))
# print(isinstance(a, int))

a = 3
def add(a, b):
    """Adding two numbers"""
    return a + b

print(globals())

import sys

a = 3
if a == 3:
    sys.exit(11)

