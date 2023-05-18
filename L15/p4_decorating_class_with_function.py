# func = decorator(func)
# func = Decorator()(func)
# class = decorator(class)
# class = Decorator()(class)

# def add_attribute_decorator(class_):
#
#     class_.default = 1111111
#
#     def add(self, a, b):
#         print(self.name)
#         return a + b
#
#     class_.add = add
#     return class_
#
#
# @add_attribute_decorator
# class User:
#
#     def __init__(self, name):
#         self.name = name
#
#     def print_name(self):
#         print(f"I'm {self.name}")
#
# john = User('John')
# print(User.default)
# print(john.default)
#
# print(john.add(5, 3))

def add_decorator(class_):

    class Wrapper:

        def __init__(self, *args, **kwargs):
            self.instance = class_(*args, **kwargs)

        def __getattr__(self, item):
            return getattr(self.instance, item)

        def add(self, a, b):
            print(self.instance.name)
            return a + b

    return Wrapper


@add_decorator
class User:

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"I'm {self.name}")


john = User('John')

print(john.add(5, 3))

