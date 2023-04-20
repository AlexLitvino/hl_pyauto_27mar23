def add(a, b=0):
    return a + b

# print(add(1))
# print(add(1))
# print(add(1))

def add_element(lst=None):
    if not lst:
        lst = []
    print(lst)
    lst.append(111)
    print(lst)
    print()


# add_element()
# add_element()
# add_element()

import copy
def func(lst):
    #lst.copy() == lst[:]
    lst_temp = copy.deepcopy(lst)
    lst_temp.append(111)
    return lst_temp

lst = [1, 2, 3, [222]]
lst2 = func(lst)
print(lst2)
print(lst)