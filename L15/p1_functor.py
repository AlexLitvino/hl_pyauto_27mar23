# class Multiply:
#
#     def __init__(self, multiplicator):
#         self.multiplicator = multiplicator
#
#     def multiply(self, number):
#         return self.multiplicator * number
#
#
#
# multiply_by_5 = Multiply(5)
# print(callable(multiply_by_5))
# print(multiply_by_5.multiply(20))
#
#
# class Multiply:
#
#     def __init__(self, multiplicator):
#         self.multiplicator = multiplicator
#
#     def __call__(self, number):
#         return self.multiplicator * number
#
# multiply_by_5 = Multiply(5)
# print(callable(multiply_by_5))
# print(multiply_by_5(20))

#For callbacks

def perform_action(func, op1, op2):
    return func(op1, op2)

# def  mlp(a, b):
#     return a * b
#
# print(perform_action(mlp, 54, 2))

# class Action:
#
#     def __init__(self, action):
#         self.action = action
#
#     def __call__(self, op1, op2):
#         self.log_action(op1, op2)
#
#         if self.action == 'add':
#             return op1 + op2
#         elif self.action == 'sub':
#             return op1 - op2
#         elif self.action == 'mlp':
#             return op1 * op2
#         elif self.action == 'div':
#             return op1 / op2
#         else:
#             raise Exception("Unknown action")
#
#     def log_action(self, op1, op2):
#         print(f"Action '{self.action}' was called with operands {op1} and {op2}")
#
# add = Action('add')
# # print(add)
# print(perform_action(add, 4, 6))

# class Action:
#
#     operation_mapping = {'add': lambda x, y: x + y,
#                          'sub': lambda x, y: x - y,
#                          'mlp': lambda x, y: x * y,
#                          'div': lambda x, y: x / y}
#
#     def __init__(self, action):
#         self.action = action
#
#     def default(self, x, y):
#         raise Exception("Unknown action")
#
#     def __call__(self, op1, op2):
#         self.log_action(op1, op2)
#         return Action.operation_mapping.get(self.action, self.default)(op1, op2)
#         # if self.action == 'add':
#         #     return op1 + op2
#         # elif self.action == 'sub':
#         #     return op1 - op2
#         # elif self.action == 'mlp':
#         #     return op1 * op2
#         # elif self.action == 'div':
#         #     return op1 / op2
#         # else:
#         #     raise Exception("Unknown action")
#
#     def log_action(self, op1, op2):
#         print(f"Action '{self.action}' was called with operands {op1} and {op2}")
#
# add = Action('add')
# # print(add)
# print(perform_action(add, 4, 6))


class Action:

    operation_mapping = {'add': lambda x, y: x + y,
                         'sub': lambda x, y: x - y,
                         'mlp': lambda x, y: x * y,
                         'div': lambda x, y: x / y}

    def __init__(self, action):
        self.action = action

    def default(self, x, y):
        raise Exception("Unknown action")

    def __call__(self, op1, op2):
        self.log_action(op1, op2)
        match self.action:
            case 'add' | 'sum':
                return op1 + op2
            case 'sub':
                return op1 - op2
            case 'mlp':
                return op1 * op2
            case 'div':
                return op1 / op2
            case _:
                raise Exception("Unknown action")

    def log_action(self, op1, op2):
        print(f"Action '{self.action}' was called with operands {op1} and {op2}")

add = Action('sum')
# print(add)
print(perform_action(add, 4, 6))