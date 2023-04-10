"""
    Tuples creation
    Operations with tuples
    Tuples methods
    Miscelanious about tuples
"""

# t = (1, 2, 4)
# print(t)
# print(type(t))
#
# t = 1, 2, 4
# print(t)
# print(type(t))
#
# t = (1,)
# print(t)
# print(type(t))
#
# t = 1,
# print(t)
# print(type(t))
#
# t = tuple([1, 3, '444', [4, 4]])
# print(t)

# t = tuple('aghsrwge')
# print(t)

# t = (1, 4, 6, 4, 6)
# print(len(t))
# print(t[-1])
# print(t[1:-1])
#
# #t[0] = 232323
#
# t1 = (1, 2)
# t2 = (3, 4)
# t2 += t1
# print(t2)
# # t3 = t1 + t2
# # print(t3)

# t = (1, 4, 6, 4, 6)
# print(t.count(4))
# print(t.index(6))


# t = (1, 2, ['internal'])
# # t[2].append(111)
# # print(t)
# lst1 = [1, 2]
# lst2 = [3, 4]
# lst1 += lst2
# print(lst1)
# #print([1, 2] + [3, 4])
#tuple
# t = (1, 2, ['internal'])
# try:
#     t[2] += [3, 4]
# except TypeError:
#     pass
# print(t)

t = (1, 2, ['internal'])
t[2].extend([3, 4])
print(t)
