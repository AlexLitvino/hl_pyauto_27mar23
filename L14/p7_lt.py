import functools

@functools.total_ordering
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User:\nname: {self.name}\nage: {self.age}"

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"

    def __lt__(self, other):
        return self.age < other.age


john = User('John', 67)
anna = User('Anna', 43)
julia = User('Julia', 55)

print(john >= anna)

users = [john, anna, julia]
print(users)
print(sorted(users))
print(sorted(users, key=lambda user: user.age))

