import pickle

object_to_serialize = {
    'name': 'John Smith',
    'age': 25,
    'lucky numbers': (1, 2, 3, 4, 5)
}

with open('pickle.pkl', 'wb') as f:
    pickle.dump(object_to_serialize, f)

with open('pickle.pkl', 'rb') as f:
    restored_object = pickle.load(f)

print(object_to_serialize == restored_object)

# ######################################################################################################################

import shelve

obj1 = "Line1"
obj2 = "Line2"

# Keys should be only strings and unique
with shelve.open('shelve.shl') as f:
    f['line1'] = obj1
    f['line2'] = obj2


with shelve.open('shelve.shl') as f:
    restored_ob1 = f['line1']
    restored_ob2 = f['line2']

print(obj1 == restored_ob1)
print(obj2 == restored_ob2)
