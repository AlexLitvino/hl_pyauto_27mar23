# a = 3
# a += 5
# users = [
#     {'name': 'Anna', 'age': 23, 'salary':5343},
#     {'name': 'John', 'age': 34, 'salary':5343},
#     {'name': 'Oksana', 'age': 33, 'salary':5343}
#
# ]
#
# def get_total_salary(users):
#     total = 0
#     for user in users:
#         total += user['salary']
#     return total
#
# print(get_total_salary(users))


# class Human:
#     pass
#
# print(Human)
# print(type(Human))
#
# human1 = Human()
# print(human1)
# print(type(human1))
# print(isinstance(human1, Human))
# print(isinstance(human1, list))
# human2 = Human()
# print(human2)
# print(type(human2))

# class Human:
#
#     name = 'John'
#
# john1 = Human()
# print(john1.name)
# john1.name = 'James'
# print(john1.name)
#
# john2 = Human()
# print(john2.name)


# class Human:
#
#     height = 179
#
#     def __init__(self, name, age=56):
#         self.name = name
#         self.age = age
#         Human.height = 23
#
#     def print_name(self):
#         print(self)
#         print(f"My name is  {self.name}")
#
# print(Human.__dict__)
#
# john = Human('John', 12)
# print(john)
# anna = Human('Anna', 35)
#
# john.print_name()
#
# print(Human.height)
# print(john.height)
# print(john.__dict__)
# print(anna.height)
#
# print(john.name, john.age)
# print(anna.name, anna.age)
#
# john.name = "James"
#
# Human.height = 543
# print(john.name, john.age, john.height)
# print(anna.name, anna.age, anna.height)
#
# andrew = Human('Andrew')
# print(andrew.name, andrew.age)
#
# #maksim = Human()

# class Human:
#
#     mutable = []
#     immutable = 111
#
#     def __init__(self, name, age=56):
#         self.name = name
#         self.age = age
#
#
#
# john = Human('John', 12)
# anna = Human('Anna', 35)

# print(john.immutable)
# print(john.__dict__)
# print(anna.immutable)
# print(john.__dict__)
#
# Human.immutable = 2222
#
# print(john.immutable)
# print(john.__dict__)
# print(anna.immutable)
# print(john.__dict__)

# john.immutable = 33333
#
# print(Human.immutable)
# print(Human.__dict__)
# print(john.immutable)
# print(john.__dict__)
# print(anna.immutable)
# print(anna.__dict__)

# print(Human.mutable)
# print(Human.__dict__)
# print(john.mutable)
# print(john.__dict__)
# print(anna.mutable)
# print(anna.__dict__)

# Human.mutable.append(1111)
#
# print()
# print(Human.mutable)
# print(Human.__dict__)
# print(john.mutable)
# print(john.__dict__)
# print(anna.mutable)
# print(anna.__dict__)

# john.mutable.append(2222)
#
# print()
# print(Human.mutable)
# print(Human.__dict__)
# print(john.mutable)
# print(john.__dict__)
# print(anna.mutable)
# print(anna.__dict__)
#
# john.mutable.append(33333)
#
# print()
# print(Human.mutable)
# print(Human.__dict__)
# print(john.mutable)
# print(john.__dict__)
# print(anna.mutable)
# print(anna.__dict__)
#
# anna.mutable = []
#
# print()
# print(Human.mutable)
# print(Human.__dict__)
# print(john.mutable)
# print(john.__dict__)
# print(anna.mutable)
# print(anna.__dict__)

# class Human:
#
#     height = 178
#
#     def __init__(self, name, age=56):
#         self.name = name
#         self.age = age
#
#     def change_name(self, new_name):
#         print(Human.get_random_user_id())
#         self.name = new_name
#
#     def format_name(this):
#         return f"<i>{this.name}</i>"
#
#     def print_formatted_name(self):
#         print(self.format_name())
#
#     def get_user_email(self):
#         return f"{self.name}{Human.get_random_user_id()}@test.com"
#
#
#     # def hello():
#     #     print("Hello")
#
#     @staticmethod
#     def get_random_user_id():
#         print(Human.height)
#         import random
#         return random.random()
#
#     @classmethod
#     def create_human_with_salary(cls, name, age, salary):
#         obj = cls(name, age)
#         obj.salary = salary
#         #print(cls)
#         return obj
#
#     @classmethod
#     def change_class_height(cls, new_height):
#         cls.height = new_height
#
#
# def get_random_user_id():
#     print(Human.height)
#     import random
#     return random.random()


#Human.get_random_user_id = staticmethod(get_random_user_id)

# john = Human('John', 34)
# print(Human)
# anna = Human.create_human_with_salary('Anna', 35, 4535)
# print(anna.name, anna.age, anna.salary)
# print(type(anna))
#
#
# print(john.get_user_email())
# john.print_formatted_name()
# print(john.get_random_user_id())
# print(Human.get_random_user_id())
#Human.hello()
#
# # print(john.name)
# Human.change_name(john, 'James')
# # john.change_name('James')
# # print(john.name)
#
# #if __name__ == '__main__':


class Human:

    # def __new__(cls, *args, **kwargs):
    #     print("In __new__")
    #     return super().__new__(cls)

    def __init__(self, name, age=56):
        #print("In __init__")
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name



def say_hello(self):
    print(f"Hello {self.name}")

#Human.say_hello = say_hello
john = Human('John', 46)
#john.say_hello = say_hello
#john.say_hello(john)

from types import MethodType
john.say_hello = MethodType(say_hello, john)
john.say_hello()

# obj = object.__new__(Human)
# print(obj)
# print(obj.__dict__)
# obj.__init__('Anna', 34)
# print(obj)
# print(obj.__dict__)