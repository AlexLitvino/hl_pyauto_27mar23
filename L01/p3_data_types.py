# Data types
"""
Numbers
- int
- float
- Decimal
- Complex

String
Boolean
None

Sequence type:
list
tuple

dict
set
frozenset

file
Custom classes
"""
#print(4)

number = 123456
print(id(number))
number = number + 1
print(id(number))

float_number = 3.5
print(float_number)
float_number2 = 2.4E-2 #3e5  # 3 * 10 ^ 5
print(float_number2)

print(0.1 + 0.1 + 0.1)  #

import decimal
print(decimal.Decimal("0.1") + decimal.Decimal("0.1") + decimal.Decimal("0.1"))

complex_number = 3 + 4j
print(complex_number.conjugate())

"""
str1 = "Qwerty"
print(str1)
str2 = 'Qwerty'
print(str2)
str3 = '//div[@id="unique"]'
print(str3)
"""

# multiline_string = """Line1
# Line2
#
# Line_n
# """
# print(multiline_string)
#
# true = True
# false = False
# print(True + False)
#
# str = "" # "sdfsdsdsd"
# print(bool(str))
#
# # if None:
# #    print("This string is not empty")
#
# print("This string is not empty")
#
#
# # if (str == ""){
# #   s.o.p("")
# # }


lst1 = [1, 2, "sd", True, None]
print(lst1)
print(id(lst1))
lst1.append("END")
print(lst1)
print(id(lst1))
print(lst1[1])

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1
#print(id(l1) == id(l2))
#print(l1 is l2)
#print(l1 == l2)

print(l1 is l2)  # False
print(l2 is l3)  # False
print(l1 is l3)  # False

l3[0] = 2121212
print(l1)



t1 = (1, 2, 3)
print(t1)
t2 = (1,)
print(t2)
#t2[0] = 232323
t3 = ([], 3)
print(t3)
t3[0].append(2)
print(t3)
#     [1, 2, 3, 4, 4, 4]
s1 = {1, 2, 3, 4, 4, 4}
print(s1)
#s1[0]

s1 = {1, 2, 5, 7}
s2 = {3, 5, 7}
print(s1.intersection(s2))


user_lst = ["user1", "user2", "user1"]
print(set(user_lst))

fz = frozenset(user_lst)
print(fz)


users = {1: "user1",
      2: "user2",
         }  # [1,2]: "user3"

print(users)
print(users[1])
users[1] = "user3"
print(users)

"""
BASE_URL=http://google.com

"""


# set222 = {1, 2, "string", {1,2}}
# print(set222)
#__hash__

l1 = [1, 3, 4, [3]]
l3 = l1.copy()
l3[3].append(1111)
print(l1)
print(l3)
