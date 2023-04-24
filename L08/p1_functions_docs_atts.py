# """This module is for docstrings explanation
#
#
#
# """
#
#
# class A:
#     """This class about ..."""
#     pass
#
#
# def add(a, b):
#     """
#     Function ...
#     :param a: int first add
#     :param b: int
#     :return: int sum
#     """
#     return a + b  # dddd


def add(a, b):
    """Docstring"""
    add.my_attribute = 10000
    return a + b
add(2, 4)
print(add.my_attribute)
print(hasattr(add, 'my_attribute'))
#print(add.my_attribute) # error
add.my_attribute = 4
print(add.my_attribute)
print(hasattr(add, 'my_attribute'))

print(add)
print(add.__name__)
print(add.__doc__)
print(add.__code__.co_argcount)
print(add.__code__.co_filename)