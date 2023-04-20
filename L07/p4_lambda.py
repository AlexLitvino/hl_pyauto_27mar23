def inc(n):
    return n + 1

print(inc(4))

inc = lambda x: x + 1

print(inc(4))

# def add(x, y):
#     return x + y

add = lambda x, y: x + y
print(add(3, 60))

lst = list(map(int, ['1', '2', '3']))
print(lst)

lst = list(map(lambda x: x * x, range(10)))
print(lst)