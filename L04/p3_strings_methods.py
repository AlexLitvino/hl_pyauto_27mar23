# print(1, 3)
# print(2, 4)

# str1 = "asasasasddsddasasas"
# str1.encode()

"""
# Position in string
    endswith
    find
    index
    rfind
    rindex
    startswith
    count
"""

#str1 = "123451167811934324234242311"
# # print(str1.endswith('8d9'))
# # print(str1.startswith('1e23'))
# #print(str1.count('11'))
# # print(str1.index('11', 8))
# # print(str1.find('11'))
# print(str1.rfind('11'))

"""
# Letter case
    capitalize
    casefold
    lower
    upper
    swapcase
    title
"""
# str1 = "Ab Cdddd tttttt"
# print(str1.capitalize())
# print(str1.title())
# print(str1.lower())
# print(str1.upper())
# print(str1.swapcase())
# print("heiß".casefold())

"""
# Justification
    center
    ljust
    rjust
    zfill
"""
# str1 = "12345"
# print(str1.center(15, '+'))
# print(str1.rjust(15))
# a = 'a3'
# print(a.zfill(3))

"""
# Combination/separation
    join
    split
    rsplit
    splitlines
    partition
    rpartition
"""
# str1 = "qwdfqewdfwer twer fggf deedfed"
# print(str1.split('wd', maxsplit=3))
# print('_'.join(['qqq', 'aaa', 'ttt']))
# print(str1.rsplit('w'))
multi_string = """
Line1
Line2

"""
# print(multi_string.splitlines())
# for i in multi_string.splitlines():
#     print(i)
#print(str1.partition('twer'))

"""
# Removing whitespaces
    strip
    lstrip
    rstrip
"""
# print("   fdfsf ".strip())


"""
# Modification
    removeprefix
    removesuffix
    replace
    expandtabs
"""
#print("PREFIXasdasffgsfhhshfg".removeprefix("PREFIX"))
#print("aaa bbb ccc aaa".replace('aaa', 'qqq', 1))


"""
# Checking
    isalnum
    isalpha
    isascii
    isdecimal
    isdigit
    isidentifier
    islower
    isnumeric
    isprintable
    isspace
    istitle
    isupper
"""
print("dssdf3$$$$44344d".isalnum())


import string
print(string.digits)
print(string.ascii_letters)

