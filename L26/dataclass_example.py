from dataclasses import dataclass, asdict, astuple

@dataclass(frozen=True)
class User:
    name: str
    age: int
    salary: int

    def custom_methoid(self):
        print(f"Hello, {self.name}")



user1 = User('John', 23, 46233)
print(user1)
#print(user1.name)

print(asdict(user1))
print(astuple(user1))

user2 = User('John', 23, 46233)
print(user2)

print(user1 == user2)

user2.custom_methoid()
#user1.name = 'James'