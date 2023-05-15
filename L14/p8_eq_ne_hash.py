class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User:\nname: {self.name}\nage: {self.age}"

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        else:
            return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))


john1 = User('John', 67)
john2 = User('John', 67)
anna = User('Anna', 43)

print(john1 == john2)
print(john1 == anna)

s = set()
#s.add([])  # error
s.add(john1)
print(s)
print(john1 in s)
john1.name = 'James'
print()
print(s)
print(john1 in s)
