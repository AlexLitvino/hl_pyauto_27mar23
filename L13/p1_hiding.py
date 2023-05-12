class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self._salary = salary
        self.__heartbeat = 90

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value

    def change_heartbeat(self, new_value):
        self.__heartbeat = new_value

    def show_heartbeat(self):
        print(self.__heartbeat)

    def _generate_group_id(self):
        pass


class Tester(Employee):

    def increase_salary(self, increment):
        self._salary += increment

    # def show_heartbeat(self):
    #     print(self.__heartbeat)

    def drink_coffee(self):
        self.change_heartbeat(150)


employee = Employee('Anna', 43, 3444)
print(employee._salary)
employee._salary += 10000
print(employee._salary)
#print(employee.__heartbeat)
print(employee._Employee__heartbeat)
employee._Employee__heartbeat = 120
print(employee._Employee__heartbeat)



tester = Tester('Olga', 23, 3455)
print(tester._salary)
tester.increase_salary(100)
print(tester._salary)
# tester.__heartbeat = 120
# print(tester.__heartbeat)
#tester.show_heartbeat()

tester.show_heartbeat()
tester.drink_coffee()
tester.show_heartbeat()
