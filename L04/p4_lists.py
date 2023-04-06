# lst = [1,2,4, "sasasffddfs", None, [1, 3, [1, 4, {'a': 2}]]]
# print(lst)
# print(len(lst))
# print(lst[0])
# print(lst[-1])
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 3]
# print(lst[1:6:2]) # 2 4 6
#
# lst_copy = lst[:]
# print(lst)
# print(lst_copy)
# lst[2] = 12121212
#
# print(lst)
# print(lst_copy)
# #lst[232323232323] = 23

# lst = [1, 2]
# lst2 = lst * 3
# print(lst2)
#
# lst = [None] * 1000
# lst[777] = 23
# print(lst)

# lst = [[1, 2]]
# lst2 = lst * 3
# print(lst)
# print(lst2)
# #lst[0].append(555)
# print(lst2[0])
# lst2[0].append(444)
# print(lst)
# print(lst2)
#
#
# lst = [1,2,3]
# print(lst.append(343434))
# print(lst)
# print(lst[0])

lst = ['a', 'b', 'c', 'd']

# for item in lst:
#     print(item.upper())

# for index in range(len(lst)):
#     print(lst[index].upper())

# expected_values = ['a', 'b', 'c', 'd']
# actual_values = ['a', 'b', 'R', 'd']
#
# for index, item in enumerate(expected_values):
#     #print(index, item)
#     if actual_values[index] != item:
#         print(f"Error on {index} comparison")
#
#
# for index, _ in enumerate(expected_values):
#     print(index)

#lst = [1, 2, 3, 4, 5]
# lst = [1, 2, 3]
# a, b, c = lst
# print(a)
# print(b)
# print(c)

# lst = [1, 2, 3, 4, 5]
# a, b, *c = lst
# print(a)
# print(b)
# print(c)


# lst = [1, 2, 3, 4, 5]
# *a, b, c = lst
# print(a)
# print(b)
# print(c)

lst = [1, 2, 3, 4, 5]
a, *b, c, d = lst
print(a)
print(b)
print(c)
print(d)


