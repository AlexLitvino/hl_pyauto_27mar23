class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User:\nname: {self.name}\nage: {self.age}"

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"


john = User('John', 34)
anna = User('Anna', 43)
julia = User('Julia', 55)

print(john)
print(str(john))
print(repr(john))
users = [john, anna, julia]
print(users)

import datetime
now = datetime.datetime.now()
print(now)
print(repr(now))
