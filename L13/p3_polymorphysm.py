# #len()
# # print(abs(-5.7))
# # print(abs(3+4j))
#
# def add(a, b):
#     return a + b
# print(add(4, 6))
# print(add("as", "fg"))
#
# # def add(a, b, c):
# #     return a + b
#
# print(add(4, 6))
# print(add("as", "fg"))


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * percent


class Manager(Employee):

    def increase_salary(self, percent, bonus=0):
        # self.salary += self.salary * percent + bonus
        super().increase_salary(percent)
        self.salary += bonus



employee = Employee('Anna', 1000)
manager = Manager('Olga', 1000)

employee.increase_salary(0.1)
print(employee.salary)
manager.increase_salary(0.1,  500)
print(manager.salary)

for emp in [employee, manager]:
    if isinstance(emp, Manager):
        emp.increase_salary(0.2, 100)
    else:
        emp.increase_salary(0.25, 0)

print(employee.salary)
print(manager.salary)
