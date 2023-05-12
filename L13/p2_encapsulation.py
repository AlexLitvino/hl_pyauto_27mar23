import datetime


class Employee:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        self.__health = 90

    def get_name(self):
        return self.name

    @property
    def full_name(self):
        return f"{self.name} Unknown Surname"

    @property
    def age(self):
        return datetime.datetime.now().year - self.birthyear

    # def get_health(self):
    #     print("Get health")
    #     return self.health
    #
    # def set_health(self, value):
    #     if 50 <= value <= 190:
    #         self.health = value
    #     else:
    #         raise ValueError("Invalid health value")
    #
    # def delete_health(self):
    #     print("Removing health attr")
    #     del self.health
    #
    # super_health = property(fget=get_health, fset=set_health, fdel=delete_health, doc="Documentation on health attr")

    @property
    def super_health(self):
        """Documentation on health attr"""
        print("Get health")
        return self.__health

    @super_health.setter
    def super_health(self, value):
        if 50 <= value <= 190:
            self.__health = value
        else:
            raise ValueError("Invalid health value")

    @super_health.deleter
    def super_health(self):
        print("Removing health attr")
        del self.__health



employee = Employee('Anna', 1990)
print(employee.name)
#print(employee.get_name())
print(employee.full_name)
#employee.full_name = 'Olga'
print(employee.age)

print(employee.super_health)
employee.super_health = 120
print(employee.super_health)
print(Employee.super_health.__doc__)
del employee.super_health
print(employee.super_health)
