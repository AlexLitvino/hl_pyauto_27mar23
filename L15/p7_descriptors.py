# class Descriptor:
#
#     def __get__(self, instance, owner):
#         print("In get")
#         print(f"{self}\n{instance}\n{owner}")
#         print()
#
#     def __set__(self, instance, value):
#         print("In set")
#         print(f"{self}\n{instance}\n{value}")
#         print()
#
#     def __delete__(self, instance):
#         print("In delete")
#         print(f"{self}\n{instance}")
#         print()
#
#
# class A:
#     attr = Descriptor()
#
# a = A()
# #a.attr
# #A.attr
# a.attr = 34


# class Descriptor:
#
#     def __get__(self, instance, owner):
#         print("In get")
#         return 0.05
#
#
#     def __set__(self, instance, value):
#         print("In set")
#         raise Exception("Set tax_rate is not allowed")
#
# class A:
#     tax_rate = Descriptor()
#
# a = A()
# print(a.tax_rate)
# try:
#     a.tax_rate = 0.01
# except:
#     pass
# print(a.tax_rate)

import datetime

class Age:

    def __get__(self, instance, owner):
        return datetime.datetime.now().year - instance.birthyear

    def __set__(self, instance, value):
        print("In set")
        instance.value = value
        #raise Exception("Set tax_rate is not allowed")


class User:

    age = Age()

    def __init__(self, name, birthyear):
        self.name = name
        self.__birthyear = birthyear
        self.value = None

    @property
    def birthyear(self):
        return self.__birthyear


john = User('John', 1983)
print(john.age)
john.age = 34 # error
#print(john.value)