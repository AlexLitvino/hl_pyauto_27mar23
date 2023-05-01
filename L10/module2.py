# import module1
# print(module1.add(2, 4))
# print(module1.sub(4, 6))

# import module1 as m
# print(m.add(2, 4))
# print(m.sub(4, 6))

# from module1 import add
# print(add(2, 4))
#print(sub(4, 6))  # error

# from module1 import add as sum_
# print(sum_(2, 4))

# from module1 import *
# print(add(2, 4))
# print(sub(4, 6))
#
# def mlp():
#     add(3, 6)

import sys
print(sys.path)
sys.path.append('/home/olytvynov/Projects/HL/hl_pyauto_27mar23')

import L10.module1 as m
print(m.add(2, 4))
print(m.sub(4, 6))

print(f"In module2: {__name__}")