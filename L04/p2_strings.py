# str = "qqq"
# print(len(str))
# len_ = 333

# str1 = "abc"
# str2 = "def"
# str3 = str1 + str2
# print(str3)
#
# str1 = "abc"
# print(id(str1))
# str1 += "def"
# #str1 = str1 + "def"
# print(id(str1))
#
# str1 = "abc"
# str2 = str1 * 3
# print(str1)
# print(str2)

#str1 = "0123456789"
# print(str1[0])
# print(str1[1])
# print(str1[9])
# print(str1[len(str1) - 1])
#print(str1[1000])

#str1[0] = 'l'

# print(str1[-1])
# print(str1[-2])
# print(str1[-len(str1)])
# print(str1[-10])

#str1 = "0123456789"
# print(str1[0:3])
# print(str1[1:4])
# print(str1[:4])
# print(str1[0:4])
# print(str1[4:])
# print(str1[4:9])
#
# print(str1[4:1000])  # no error
#
# print(str1[0:2] + str1[8:])
#
# print(str1)
# str2 = str1[1:5]
# print(str2)
# print(str1)

# str2 = str1[:4] + 'Q' + str1[5:]
# print(str2)
#
# str3 = ""
# for index in range(len(str1)):
#     if index != 4:
#         str3 += str1[index]
#     else:
#         str3 += 'Q'
# print(str3)

str1 = "0123456789"
# print(str1[-3:-1])
# print(str1[-3:])
#
# print('Q' + str1[6:2] + 'Q')

# print(str1[::2])
# print(str1[1::2])
# print(str1[1:6:2])
#
# print(str1[-6:-1:2])
#
# print(str1[::-1])
# print(list(range(2, 10, -1)))
# print(list(range(10, 2, -2)))
#
# print(str1[2:9:-2])
# print(str1[9:2:-2])
#
# str2 = str1[:]
# print(id(str1))
# print(id(str2))
#
# str1 = "He'llo' wordl"
# print(str1)
#
# multi_string = """Line 1
# Line2
#
# Line4
# """
# print(multi_string)
#
# str1 = "He\"llo\" world"
# print(str1)
#
# str1 = "Line1\nLine2"
# print(str1)
#
# str1 = "Line1\tLine2                        "
# print(str1)

# "My name is John. I'm 23 years old."
name = "John"
age = 23
print("My name is ", name, ". I'm ", age, " years old.", sep='')
print("My name is " + name + ". I'm " + str(age) + " years old.")
print("My name is %s. I'm %d years old." % (name, age))
print("My name is {}. I'm {} years old.".format(name, age))
print("My name is {name_q}. I'm {age_q} years old.".format(age_q=age, name_q=name))
print(f"My name is {name}. I'm {age} years old.")
print(f"Value: {age * 2} {2 +3434}")
print(f"qwerty: {len([1,2,3,4])}")

# docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
container_name = "container_name"
cmd = f"docker inspect -f '{{{{range.NetworkSettings.Networks}}}}{{{{.IPAddress}}}}{{{{end}}}}' {container_name}"
print(cmd)


# #path = "C:\temp\file.txt"
# path = r"""C:\temp\"fil"e.txt"""
# #path = "C:\\temp\\file.txt"
# print(path)

str11 = b'Qwerty'
print(str11)
byte_string = '\x4a\x4b'
print(byte_string)

str12 = "Привет"
print(str12.encode("UTF-8"))

