# def div(a, b):
#     if b == 0:
#         status = 1
#         return None
#     return a / b
#
# #div(3, 5)
#
# import os
# os.system("gi --version")

# for i in range(10):
#     # if i > 5:
#     #     break
#     print(i)
# else:
#     print("In else")

# is_exception_occurred = False

# try:
#     print("In try")
#     b = 3 + 6
#     #a = 11 + []
#     try:
#         11 + []
#         #b = 6 / 0
#     except ArithmeticError:
#         print("ArithmeticError")
#         b = 0
# except TypeError:
#     is_exception_occurred = True
#     print("Exception caught")
# else:
#     print("No exceptions")
#     print(b)
# finally:
#     print("Always performed")
# # if not is_exception_occurred:
# #     print("No exceptions")
#
#
# print("After code with exception")

import time

# while True:
#     try:
#         print("RUN")
#         time.sleep(0.5)
#     except KeyboardInterrupt:
#         print("In except")
#         break
# print("After")

# import sys
# sys.exit(2)

# try:
#     1/0
# except Exception:
#     print("Handling exception...")

# d = {}
# try:
#     #1 + []
#     #1 /0
#     d[111]
# except (TypeError, ArithmeticError):
#     print("Exception")

# try:
#     1/0
# except ZeroDivisionError as e:
#     print(e)
#     print(e.args)
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
# except Exception:
#     print("Exception")
# print("After")
# a = 100
# if a > 10:
#     e = ValueError()
#     raise e
#     #raise ValueError
#     #raise ValueError("Parameter a  should be less than 10")

# class MyAppException(Exception):
#     pass
#
#
# class ParsingException(MyAppException):
#
#     log_file = "error.log"
#
#     def __init__(self, file_name, line_number):
#         self.file_name = file_name
#         self.line_number = line_number
#
#     def log_error(self):
#         with open(ParsingException.log_file, 'w') as f:
#             f.write(f"Error occurred in {self.file_name} on {self.line_number} line\n")
#
#
# try:
#     a = 5
#     file = "data.txt"
#     line = 34
#     raise ParsingException(file, line)
# except ParsingException as e:
#     e.log_error()
#
#
#
# #raise ParsingException("Something")

# try:
#     try:
#         1/0
#     except ArithmeticError as e:
#         print("Exception")
#         raise ValueError("b = 0") from e
# except Exception as e:
#     print(e.__class__)
#     print(e.__cause__)
#
# import sys
# sys.exc_info()

def get_data():
    try:
        data = get_data_from_db()
    except DBError:
        import random
        data = random.random()
    return data

def get_data_from_db():
    try:
        open_db()
        # get data from db
    except IOError:
        # remove temp dir
        raise DBError


def open_db():
    raise IOError("No permissions")

class DBError(Exception):
    pass

print(get_data())
