# try:
#     file = open('error.log', 'r')
#     file.read()
# finally:
#     file.close()
#
# with open('error.log', 'r') as file:
#     file.read()

# class MockFile:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print("In enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("In exit")
#         pass
#
#     def read(self):
#         return "TEST DATA"
# print(open)
# builtin_open = open
#
# def open(file_name, mode='r'):
#     if file_name == "mock_file.txt":
#         return MockFile("mock_file.txt")
#     else:
#         return builtin_open(file_name, mode)
# print(open)
#
# # with open("error.log") as f:
# #     print(f.read())
#
# with open("mock_file.txt") as f:
#     print(f.read())

import contextlib

@contextlib.contextmanager
def file(file_name, mode='r'):
    try:
        file = open(file_name, mode)
        yield file
    finally:
        print("Finally")
        file.close()

with file('error.log') as f:
    1/0
    print(f.read())