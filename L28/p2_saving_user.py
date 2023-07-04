import sqlite3


# # Using __conform__ for converting Python object to db
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __conform__(self, protocol):
#         if protocol is sqlite3.PrepareProtocol:
#             return f"{self.name}|{self.salary}"
#
#
# connection = sqlite3.connect('emplyees4.db')
# cursor = connection.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS Employees (employee TEXT);')
# employee1 = Employee('John Smith', 34000)
# cursor.execute('INSERT INTO Employees VALUES (?);', (employee1,))
# connection.commit()
# cursor.execute('SELECT * FROM Employees;')
# data = cursor.fetchall()
# print(data)


# ######################################################################################################################
# # Using sqlite3.PARSE_COLNAMES
#
# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"User(name={self.name}, age={self.age})"
#
#
# def user_adapter(user):
#     return f"{user.name}|{user.age}"
#
#
# def user_converter(value):
#     value = str(value, 'utf-8')
#     name, age = value.split('|')
#     return User(name, int(age))
#
#
# sqlite3.register_adapter(User, user_adapter)
# sqlite3.register_converter('my_user', user_converter)
#
# connection = sqlite3.connect('users2.db', detect_types=sqlite3.PARSE_COLNAMES)
#
# cursor = connection.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS Users (user my_user);')
# user1 = User('John Smith', 34)
# cursor.execute('INSERT INTO Users (user) VALUES (?);', (user1,))
# connection.commit()
#
# cursor.execute('select user as "user [my_user]" from Users;')
#
# data = cursor.fetchall()
# print(data)
# user = data[0][0]
# print(user.name)

# ######################################################################################################################

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name={self.name}, age={self.age})"


def user_adapter(user):
    return f"{user.name}|{user.age}"


def user_converter(value):
    value = str(value, 'utf-8')
    name, age = value.split('|')
    return User(name, int(age))


sqlite3.register_adapter(User, user_adapter)
sqlite3.register_converter('my_user', user_converter)

connection = sqlite3.connect('users3.db', detect_types=sqlite3.PARSE_DECLTYPES)

cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Users (user my_user);')
user1 = User('John Smith', 34)
cursor.execute('INSERT INTO Users(user) VALUES (?);', (user1,))
connection.commit()

cursor.execute('select user from Users;')

data = cursor.fetchall()
print(data)
user = data[0][0]
print(user.name)
