# a = [i for i in range(10)]

"""
Iterator
^
Generator      List
^
Generator functions, Generator expressions
"""

# sq_li = [i * i for i in range(10)]
# sq_gen = (i * i for i in range(10))
# print(sq_li[3])
#print(sq_gen[3]) # error

# for i in sq_gen:
#     print(i)
# for i in sq_gen:
#     print(i)

# import sys
# print(sys.getsizeof(sq_li))
# print(sys.getsizeof(sq_gen))


# print(sq_li)
# #print(list(sq_gen))
#
# # for i in sq_gen:
# #     print(i)
#
# print(next(sq_gen))
# print(next(sq_gen))
# print(next(sq_gen))
# #print(next(sq_gen))

# def sq_generator(n):
#     for i in range(n):
#         yield i * i
#         print("After yield")
#
#
#
# sq_gen = sq_generator(10)
#
#
# for i in sq_gen:
#     print(i)
# sq_gen2 = sq_generator(10)
# for i in sq_gen2:
#     print(i)

# def gen():
#     yield 1
#     yield 2
#     yield 100
#
# for i in gen():
#     print(i)


# def gen(n):
#     for i in range(n):
#         yield i
#         if i > 2:
#             return "Stopped"

# for i in gen(10):
#     print(i)

# try:
#     g = gen(10)
#     for i in range(10):
#         print(next(g))
# except StopIteration as e:
#     print(e.value)

# def g1():
#     for i in range(4):
#         yield i
#
# def g2():
#     for i in "abcd":
#         yield i

# def g():
#     q1 = g1()
#     q2 = g2()
#     for i in q1:
#         yield i
#     for i in q2:
#         yield i

# def g():
#     q1 = g1()
#     q2 = g2()
#     yield from q1
#     yield from q2
#
# # for i in g():
# #     print(i)
#
# import itertools
# for i in itertools.chain(g1(), g2()):
#     print(i)


def g():
    for i in range(10):
        a = yield i
        print(a)

q = g()
print(next(q))
print(next(q))
print(q.send(1000))

# @pytest.fixture
# def db():
#     # setup db
#     yield db
#     db.close()


