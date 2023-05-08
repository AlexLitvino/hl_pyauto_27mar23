class Animal:
    is_alive = True


class Human(Animal):

    health = 100

    def __init__(self, name, age):
        print("IN HUMAN CONSTRUCTOR")
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I'm {self.name} of {self.age} years")


class Employee(Human):

    def __init__(self, name, age, salary):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        #Human.__init__(self, name, age)
        self.salary = salary


    def introduce(self):
        print(f"I'm {self.name} of {self.age} years. I'm employee of a company")


#human = Human('John', 34)
employee = Employee('Anna', 54, 5454)
print(employee.health)
employee.introduce()
print(employee.__class__.__name__)
print(Employee.__bases__)
print(employee.is_alive)


class MyException(Exception):
    pass
