# print(range(10))
# print(list(range(10)))
# print(list(range(2)))
# print(list(range(2, 10)))
# print(list(range(4, 16)))
# print(list(range(10, 2)))
# print(list(range(1, 10, 2))) #[1,3,5, 7, 9]
# print(list(range(10, 0, -1)))
# print(list(range(10, 0, -2)))

# lst = [1, 3, 5, 7, 5]
# #print(len(lst))
# for i in range(len(lst) - 1, -1, -1):
#     print(lst[i], end=' ')

# lst = [1, 3, 5, 7, 5]
# for i in lst:
#     print(i * i)

# tup = ("a", "b", "c")
# for i in tup:
#     print(i)

# s = {1, 5, 7, 2}
# for i in s:
#     print(i)

# lists = [[1, 4, 2, 3, 4], [2, 5, 3, 2, 6, 2], [1, 4, 6]]
# for lst in lists:
#     for item in lst:
#         print(item, end=' ')
#     print()

# lists = [[1, 4, "STOP", 2, 3, 4], [2, 5, 3, 2, "STOP", 6, 2], [1, 4, 6]]
# for lst in lists:
#     for item in lst:
#         if item == "STOP":
#             break
#         print(item, end=' ')
#     print()


# lists = [[1, 4, "SKIP", 2, 3, 4], [2, 5, 3, 2, "SKIP", 6, 2], [1, 4, 6], (1, 3, 4), {3, 4, 6}]
# for lst in lists:
#     for item in lst:
#         if item == "SKIP":
#             continue
#         print(item, end=' ')
#     print()

lst = [1, 3, 5]
length_of_list = len(lst)
for i in lst:
    print(i + length_of_list)
