import os


def sum_(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_(lst[1:])

# lst = [1, 2, 3]   #(1 + (2 + (3 (+ 0))))
# print(sum_(lst))

config = {
    'data': {
        'url': "",
        'timeout': 5
    }
}

"""
n! = 1 * 2 ...* n
f(0) = 1
f(1) = 1
f(n) = n * f(n-1)
"""
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

# for i in range(6):
#     print(factorial(i))

# lst = [1, 2, 3, [3, 4, 5]]
# print(isinstance(1, int))
# print(isinstance([], int))
# print(isinstance([], list))

import os
dirpath, dirnames, filenames = os.walk('recursion_dir')
print(dirpath, dirnames, filenames)

for dirpath, dirnames, filenames in os.walk('recursion_dir'):
    for file in filenames:
        print(dirpath)
        if file.endswith('.py'):
            print(file)
        print()


