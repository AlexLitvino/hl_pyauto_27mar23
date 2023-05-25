# def singleton(class_):
#
#     def wrapper(*args, **kwargs):
#         if not hasattr(class_, 'instance'):
#             instance = class_(*args, **kwargs)
#             setattr(class_, 'instance', instance)
#         return getattr(class_, 'instance')
#     return wrapper
#
#
# @singleton
# class King:
#
#     def __init__(self, name):
#         self.name = name
#
# print(type(King))
#
# john = King('John')
# print(john)
# richard = King('Richard')
# print(richard)
# print(john is richard)
# print(richard.name)
#
#
# import logging
# logger_1 = logging.getLogger('cat')
# logger_2 = logging.getLogger('cat')
#
# print(logger_1 is logger_2)


class King:

    instance = None

    def __new__(cls, *args, **kwargs):
        if King.instance:
            return King.instance
        else:
            obj = super().__new__(cls)
            return obj

    def __init__(self, name):
        if King.instance:
            pass
        else:
            self.name = name
            King.instance = self


print(type(King))

john = King('John')
print(john)
richard = King('Richard')
print(richard)
print(john is richard)
print(richard.name)
