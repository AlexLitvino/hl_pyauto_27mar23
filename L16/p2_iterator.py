# lst = [3, 5, 6]
# #iter()
# #next()
#
# for i in lst:
#     print(i)


class SquareIterator:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        # self.current = self.start
        return self

    def __next__(self):
        if self.current < self.stop:
            square = self.current * self.current
            self.current += 1
            return square
        else:
            raise StopIteration


sq_iter = SquareIterator(2, 8)
for i in sq_iter:
    print(i)

# print("QQQ")
# #print(sq_iter.current)
#
#
# for i in sq_iter:
#     print(i)

# lst = [4, 4]
# print(lst is iter(lst))

# class SquareIterator:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.current = start
#
#     def __iter__(self):
#         return SquareIterator(self.start, self.stop)
#
#     def __next__(self):
#         if self.current < self.stop:
#             square = self.current * self.current
#             self.current += 1
#             return square
#         else:
#             raise StopIteration
#
#
# sq_iter = SquareIterator(2, 8)
# for i in sq_iter:
#     print(i)
#
# print("QQQ")
# print(sq_iter.current)
#
# for i in sq_iter:
#     print(i)

# class SquareIteratorLogic:
#
#     def __init__(self, start, stop):
#         self.stop = stop
#         self.current = start
#
#     def __next__(self):
#         if self.current < self.stop:
#             square = self.current * self.current
#             self.current += 1
#             return square
#         else:
#             raise StopIteration
#
#
# class SquareIterator:
#
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return SquareIteratorLogic(self.start, self.stop)
#
#
# sq_iter = SquareIterator(2, 8)
# for i in sq_iter:
#     print(i)
#
# print("QQQ")
#
# for i in sq_iter:
#     print(i)