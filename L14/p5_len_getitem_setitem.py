class Building:

    def __init__(self, address, floor_numbers=6):
        self.floor_numbers = floor_numbers
        self.address = address
        self.floors = [None] * floor_numbers

    def __getitem__(self, item):
        #print(item)
        return self.floors[item]

    def __setitem__(self, key, value):
        self.floors[key] = value

    def __len__(self):
        return self.floor_numbers
        #[None, None, 'GL', None, None, None]
        #return len(list(filter(None, self.floors)))

    def __bool__(self):
        return bool(len(list(filter(None, self.floors))))


building1 = Building("Kharkiv")
print(building1.floors)
#building1.floors[2] = "GL"
building1[2] = 'GL'
# print(building1.floors)
# print(building1[2])
# print(building1[0:4])
# print(building1[slice(0, 4, None)])

# for i in building1:
#     print(i)


print(bool(building1))
print(len(building1))
