fz = frozenset([1, 2, 4, 5, 5, 5, 7])
print(fz)
print(len(fz))
print(1 in fz)

# #s1 = {1, 2, 3, {4, 5, 6}}
# s1 = {1, 2, 3, fz}
# print(s1)
#
# for i in s1:
#     print(i)
#     if type(i) == type(frozenset()):
#         for j in i:
#             print(f'\t{j}')


fz1 = frozenset([1, 2, 4, 5, 5, 5, 7])
s2 = {1, 3, 5}
s3 = fz1.intersection(s2)
print(s3)
