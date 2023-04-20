# def func(a, b, c):
#     print(f"a={a}, b={b}, c={c}")
#
# func(1, 2, 3)
# func(1, c=3, b=2)
# func(c=3, a=1, b=2)


# def func(a, /, b, c):
#     print(f"a={a}, b={b}, c={c}")

#func(1, 2, 3)
#func(1, c=3, b=2)
#func(c=3, a=1, b=2)  # error


# def func(a, b, *, c):
#     print(f"a={a}, b={b}, c={c}")

#func(1, 2, 3)  # error
# func(1, c=3, b=2)
# func(c=3, a=1, b=2)

# def func(a, /, b, *, c):
#     print(f"a={a}, b={b}, c={c}")

#func(1, 2, 3)  # error
#func(1, c=3, b=2)
#func(c=3, a=1, b=2)  # error