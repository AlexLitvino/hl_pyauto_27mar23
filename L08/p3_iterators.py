# lst = [1, 2, 3]
# for i in lst:
#     print(i)

# lst = [1, 2, 3]
# lst_iter = iter(lst)
# #print(type(lst_iter))
# print(next(lst_iter))
# print(next(lst_iter))
# print(next(lst_iter))
# #print(next(lst_iter))
#
# print(lst is lst_iter)

with open('file.txt') as f:
    # for i in f:
    #     print(i)
    # for i in f:
    #     print(i)
    # for i in range(5):
    #     print(f"Q{f.readline()}Q")
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    file_iter = iter(f)
    print(file_iter is f)
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))

# for i in lst:
#     print(i)