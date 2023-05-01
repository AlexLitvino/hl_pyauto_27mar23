"""
test5544365695000@test.com

"""

import random

# print(random.random()) # [0, 1)
# print(random.random() *10)  # [0,10)
# print(3 + random.random() * (10-3))  # [3,10)

# for i in range(10):
#     print(random.randint(3, 7)) # [3, 7]

# for i in range(10):
#     print(random.randrange(5, 10, 2)) # [5, 7, 9]

# for i in range(10):
#     print(random.randbytes(3))

# lst = [3, 5, 7]
# print(random.choice(lst))

# lst = [3, 5, 7]
# print(random.shuffle(lst))
# print(lst)

# lst = [1, 2, 3]
# print(random.sample(lst, k=2, counts=[1, 10, 100]))

import sys
print(sys.maxsize)
seed = random.randint(0, sys.maxsize)
random.seed(seed)

print(random.getstate())

for i in range(5):
    print(random.randint(0, 5), end=' ')