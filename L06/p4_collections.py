import random
lst = [random.randint(0, 10) for i in range(100)]
print(lst)

import collections
counter = collections.Counter(lst)
print(counter)
print(counter[2])
