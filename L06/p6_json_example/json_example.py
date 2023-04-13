import json

data = {'a': 1, 'b': 2}

json_string = json.dumps(data)
print(json_string)
print(type(json_string))
print(type(data))

restored_data = json.loads(json_string)
print(restored_data)
print(type(restored_data))

with open('data.json', 'w') as f:
    res = json.dump(data, f)
    print(res)

with open('data.json', 'r') as f:
    restored_data2 = json.load(f)

print(restored_data2)
print(restored_data2 == data)
