print(__debug__)

def add(a, b):
    #assert 0 < a < 100, "Invalid a"
    return a + b

assert add(3, 5) == 8
a = add(3, 5)
assert a == 9, f"Expected 9 but {a}  received"
print("After assertion")

# assert condition, message
#
# if not condition:
#     raise AssertionError(message)
