# s1 = {1, 2, 3}
# print(s1)
# print(type(s1))
#
# s2 = set()
# print(s2)
#
# s2 = set("rrrrrytyyyefjf")
# print(s2)
#
# print(len(s2))
# print('r' in s2)
#
# # for i in s2:
# #     print(i)
#
# lst = list(s2)
# print(lst)
# lst.sort()
# print(lst)

#s1 = {[1, 2]}
# lst = []
# print(dir(lst))
# #print(lst.__hash__())
#
# t = tuple()
# print(t.__hash__())

# for i in dir([]):
#     if not i.startswith('__'):
#         print(i)

"""
    add
    clear
    copy
    pop - removes and returns "random" element
    remove - removes element, raises exception if element is missing
    discard - removes element, do nothing if element is missing
"""

# s1 = {1}
# s1.add(4)
# print(s1)
#
# #s1.clear()
# print(s1)
# #s2 = {1, (2, [])}  # error
#
# s1 = {1,4,7,3,2,6}
# value = s1.pop()
# print(value)
# print(s1)

# s1 = {1,4,7,3,2,6}
# res = s1.remove(44)
# print(res)
# print(s1)

# s1 = {1,4,7,3,2,6}
# len_before_discard = len(s1)
# res = s1.discard(4)
# len_after_discard = len(s1)
# print(res)
# print(s1)
# if len_before_discard > len_after_discard:
#     print("Element removed")

#s1[4]  # error

s1 = {1,2,4,5}
s2 = {4,5,6,7}

# s3 = s1.union(s2)
# print(s1)
# print(s2)
# print(s3)
# print()
#
# s3 = s1.update(s2)
# print(s1)
# print(s2)
# print(s3)

# s1 = {1,2,4,5}
# s2 = {4,5,6,7}
#
# s3 = s1.difference(s2)
# print(s1)
# print(s2)
# print(s3)
# print()


# s1 = {1,2,4,5}
# s2 = {4,5,6,7}
#
# s3 = s1.intersection(s2)
# print(s1)
# print(s2)
# print(s3)
# print()

# s1 = {1,2,4,5}
# s2 = {4,5,6,7}

#s3 = s1.symmetric_difference(s2)
#s3 = s1.union(s2) - s1.intersection(s2)
#s3 = s1 ^ s2
# print(s1)
# print(s2)
# print(s3)
# print()


# s1 = {1,2,4,5}
# s2 = {4,5,6,7}
#
# s3 = s1.isdisjoint(s2)
# print(s1)
# print(s2)
# print(s3)
# print()

# s1 = {1,2}
# s2 = {1, 2, 4,5,6,7}
#
# s3 = s2.issuperset(s1)
# print(s1)
# print(s2)
# print(s3)
# print()


s1 = {1,2, 10}
s2 = {1, 2, 4,5,6,7}

s3 = s1.issubset(s2)
print(s1)
print(s2)
print(s3)
print()



"""
    # methods with update, applies operation to left operand
    # methods with update, return new set
    union (s3 = s1 | s2)
    update

    difference (s3 = s1 - s2)
    difference_update

    intersection  (kind of "not intersetion") (s3 = s1 & s2)
    intersection_update

    symmetric_difference (s3 = s1 ^ s2)
    symmetric_difference_update

    isdisjoint (no common elements, "sets are independent")
    issubset  (<=)
    issuperset (>=)

"""

#results = "ID1;ID2"
