import yaml

with open('example.yaml', 'r') as f:
    #data = yaml.safe_load(f)
    data = yaml.load(f, yaml.Loader)

print(data)
#print(data[0]['martin'])


# data_to_write = data[0]['martin']
#
# data_to_write = {'name': "Martin D'vloper", 'job': 'Developer', 'skills': ['python', 'perl', 'pascal']}
# with open('output.yml', 'w') as f:
#     yaml.dump(data_to_write, f)