# a = 3
# print(123, "123", [1, 2, 3])
# print(-a)
# # 3 + 4


# Mathematical
# print(2 + 5)
# print(2 - 5)
# print(2 * 5)
# print(2.2 * 5)
# print(5 / 2)
# print(4 / 2)

# print(5 // 2)
# print(5.2 // 2)
# print(4.0 // 2)

# print(5 % 2)
# print(15 % 4)  # 3

#a % 4
#a = 3 ** 2
# print(3 ** 2)
# print(-3 ** 2)  # -9
# print(-(3 ** 2))
#
# str1 = "Hello"
# str2 = ", worlds"
# print(str1 + str2)
# #print(str1 * 3)
# print((-3) * str1)

# Comparison
# print(4 < 6.5)
# print(4 > 6.5)
# print(4 <= 6.5)
# print(4 <= 4)
# print(4 <= 3)
# print(4 >= 6.5)
# print(3 == 3)
# print(3 == 4)
# print(3 == 3.0)
# print(3 == "asd")  # __eq__
#
# print(3 != 3)
# print(3 != 3.0)
# print(3 != 4)
#
# a = 5
# print(3 < a < 8)
# str1 = "car"
# str2 = "apple"
# str3 = "Apple"
# print(str1 < str2)
# print(str2 < str3)


# Bitwise operator
# 7654321
# | & ^ ~ >> <<
"""
|
00 - 0
01 - 1
10 - 1
11 - 1

&
00 - 0
01 - 0
10 - 0
11 - 1

^
00 - 0
01 - 1
10 - 1
11 - 0

~0 - 1
~1 - 0

"""
#print(bin(3))
# a = 3
# b = 2
# print(bin(a))
# print(bin(b))
# print(bin(a | b))

# print(bin(a))
# print(bin(b))
# print(bin(a & b))

# print(bin(a))
# print(bin(b))
# print(bin(a ^ b))

# #10 << 2 - 1000
# print(b << 2)
#
# # 10 >> 1 - 1
# print(b >> 1)

"""
 76543210
0b0000000
0b1111111
1 byte = [0, 255]

7-6 - sensor status
543 - temperature
210 - humidity
"""
# data = 173
# print(bin(data))
# humidity = data & 0b00000111
# print(humidity)
#
# temperature = (data >> 3) &0b000111
# print(temperature)
#
# a = 12
# print(bin(a))
# print(bin(~a))
# print(bin(~a & 0xFF))
# print(~a)
#
# """
# 0b00001100
# 0b11110011
# """
#
# #~a = -a - 1

# a = 3
# print(a + 3)
# print(a)
# a += 3
# # a = a + 3
# print(a)


# Logical operators
# and *,  or +,  not -
"""
False and False = False 
False and True = False
True and False = False
True and True = True

False or False = False 
False or True = True
True or False = True
True or True = True

not True = False
not False = True

"""
# a = 5
# print(3 < a < 10)
# print((3 < a) and (a < 10))
#
# # False and b - False
# # True or b - True

# Membership
# in, not in
# str = "qwertyuiokjhgfds"
# print('ty' not in str)
# lst = [1, 2, 4, 6, 8]
# print(1 in lst)
#
# d = {1: 'a', 2: 'c'}
# print('a' in d)

# is,  is not
lst1 = [1, 2]
lst2 = lst1
lst3 = [1, 2]
print(lst1 is lst2)
print(lst1 is not lst3)















