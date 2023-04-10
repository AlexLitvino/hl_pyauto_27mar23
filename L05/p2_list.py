# print([5] in [3, 5, 7, [5]])

# lst1 = [1, 61, 77]
# lst2 = [1, 2, 7]
# print(lst1 > lst2)
#
# # min, max, sum, sorted
#
# a = [1, 33, 5.7]
# print(sum(a))

# b = ['q', 'a']
# print(sum(b))

# a = [1, 33, 5.7]
# print(min(a))
# print(max(a))

# # <  __lt__
# b = ['q', 'a', 'lp']
# print(min(b))
# print(max(b))

# lst = [3, 2, 7, 1, 5]
# #lst2 = sorted(lst)
# lst.sort()
# lst.append(333)
# #res = lst
# print(lst)
# #print(res)

# lst = [3, 2, 7, 1, 5]
# lst2 = sorted(lst, reverse=True)
# print(lst2)

"""
    append
    clear
    count
    extend
    index
    insert
    pop
    reverse

    remove
    copy
"""

# lst = [3, 2, 7, 1, 5]
# print(lst)
# print(lst.append(333))
# print(lst)

# lst = [3, 2, 7, 1, 5]
# lst = []
# #lst.clear()
# print(lst)


# lst = [3, 2, 7, 1, 5, 4, 5, 6]
# print(lst.count(57))

# lst = [3, 2, 7, 1, 5]
# lst2 = [1, 2, 4]
# res = lst.extend(lst2)
# print(res)
# print(lst)
# print(lst2)
#
# lst = [3, 2, 7, 1, 5]
# lst.extend('abcde')
# print(lst)

# lst = [5, 3, 2, 5, 7, 1, 5]
# print(lst.index(5, 1, 4))


"""
    insert
    pop
    reverse

    remove
    copy
"""

# lst = [5, 3, 2, 5, 7, 1, 5]
# lst.insert(-1, 'TEST')
# print(lst)


# lst = [3, 2, 5, 7, 1, 5]
# value = lst.pop(3)
# print(value)
# print(lst)

# lst = [3, 2, 5, 7, 1, 5]
# lst.reverse()
# print(lst)

#lst = [3, 2, 5, 7, 1, 5]
# reversed_lst = reversed(lst)
# print(lst)
#print(list(reversed_lst))


# lst = [3, 2, 5, 7, 1, 5]
# a = lst.remove(5)
# print(a)
# print(lst)

# lst = [3, 2, 5, 7, 1, 5]
# del lst[0]
# print(lst)
#
# a = 4
# print(a)
# del a
# print(a)

# lst = [3, 2, 5, 7, 1, 5]
# a = lst[::-1]
# print(a)
# print(lst)

# copy
#
# lst = ['internal 1',
#        ['internal 2'],
#        [1, ['super internal 3']]]

# for i in lst:
#     print(i)

# for index, item in enumerate(lst):
#     print(f"{index}: {item}")

# #[1, '3333', 555, [], {}]
# print(lst)
# lst2 = lst.copy()
# lst3 = lst[:]
# import copy
# lst4 = copy.deepcopy(lst)
#
# lst[0] = 'UPDATED 1'
# lst[1].append('UPDATED 2')
# lst[2][1][0] = 'UPDATED SUPER INTERNAL'
#
# print(lst)
# print(lst2)
# print(lst3)
# print(lst4)

# lst = [1, 2]
# a = list({1: 1, 4: 4, 7: 5})
# print(a)

# lst = []
# for i in range(10):
#        if i % 2 == 0:
#               lst.append(i)
# print(lst)

# [expression for i in iterable if condition]

# a = 3
# lst = [i * i for i in range(10)]
# b = 4
# print(lst)
# lst.append(54)
# print(lst)

# str1 = "f5fvafg555tsvsffs"
# lst = [int(symbol) for symbol in "f5fvafg5655tsv7sffs" if symbol.isdigit()]
# print(lst)
#
# lst = [[i, i * i] for i in range(10)]
# print(lst)
#
# lst = [[x, y] for x in range(5) for y in "abcdgffsf"]
# print(lst)
# print()
# lst = []
# for x in range(5):
#    for y in "abcdgffsf":
#        lst.append([x, y])
#
# print(lst)

# lst = list(range(10))
# print(lst)
# for i in lst:
#    print(i)
#    if i % 2 == 0:
#        lst.append(i)
#
# print(lst)

#lst = [4, 5, 3, 6, 6, 6, 7, 3]
# print(lst)
# for index, item in enumerate(lst):
#        if item == 6:
#               del lst[index]
#
# print(lst)

"""
[4, 5, 3, 6, 6, 6, 7, 3]
[4, 5, 3, 6, 6, 7, 3]
[4, 5, 3, 6, 7, 3]
"""

# lst = [4, 5, 3, 6, 6, 6, 7, 3]
# lst2 = [i for i in lst if i != 6]
# print(lst)
# print(lst2)

# lst = [4, 5, 3, 6, 6, 6, 7, 3]
# print(lst)
# for item in lst:
#     if item == 6:
#         lst.remove(6)
# print(lst)

lst = [4, 5, 3, 6, 6, 6, 7, 3]
print(list(lst))
print(list(range(len(lst) - 1, -1, -1)))  # [7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(lst) - 1, 0, -1):
       print(lst)
       if lst[i] == 6:
           del lst[i]

print(lst)






