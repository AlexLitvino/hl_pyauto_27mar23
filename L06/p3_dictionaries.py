"""
Dictionaries
    Dictionaries creation
    Operations with dictionaries
    Iterating over dictionary
    Dictionaries methods
    Dictionaries unpacking
"""

# contacts = {
#     #"Andrew": 1111111111111,
#     "John": ["+45454151", "244343242"],
#     "Anna": ["434544", "455545"],
#     "Andrew": 343434,
#     5: "Andrew",
#     1.545: "Andre2"
# }
# print(contacts)
# print(contacts["Anna"])
# #print(contacts["Alex"])
# print(len(contacts))
# print("Anna" in contacts)
# print(343434 in contacts)

# contacts["Andrew"] = 5678489789
# print(contacts)

# contacts['Kate'] = [322332, 555]
# print(contacts)

# d2 = dict(((1, "a"), [2, "b"]))
# print(d2)

# d3 = {i: i * i for i in range(10) if i % 2 == 0}
# print(d3)


# contacts = {
#     #"Andrew": 1111111111111,
#     "John": {"phones": ["+45454151", "244343242"],
#              "weigth": 54},
#     "Anna": ["434544", "455545"],
#     "Andrew": 343434,
#     5: "Andrew",
#     1.545: "Andre2"
# }
# print(contacts)

# del contacts['John']
# print(contacts)

# for key in contacts:
#     print(key)

# for key in contacts:
#     print(contacts[key])

# for key, value in contacts.items():
#     print(f"{key} - {value}")

"""
    clear
    copy
    fromkeys
    get
    
    items
    keys
    values
    
    pop
    popitem
    setdefault
    update
    
"""

# d = {1: 'a',
#      2: 'b',
#      3: 'c'}
# d.clear()
# print(d)

# d2 = dict().fromkeys([1, 2, 3, 4], 555)
# print(d2)

d = {1: 'a',
     2: 'b',
     3: 'c'}

#print(d[2])
#print(d.get(2, 'qqqqqqqqqqqq'))

# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# value = d.pop(1)
# print(value)
# print(d)

# pair = d.popitem()
# print(pair)
# print(d)

# value = d.setdefault(1111, 'rrrr')
# print(value)
# print(d)

# res = d.update({3: 't', 4: 'r', 5: 'x'})
# print(res)
# print(d)

# d |= {3: 't', 4: 'r', 5: 'x'}
# print(d)

d = {1: 'a',
     2: 'b',
     3: 'c'}
d2 = {3: 't', 4: 'r', 5: 'x'}

d3 = {**d, **d2}
print(d3)

# a, *b, c = [1, 2, 3, 5]
# print(a)
# print(b)
# print(c)
