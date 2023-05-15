class Data:

    def __init__(self, data):
        self.data = data

    # def get_corrupted_data(self):
    #     return f"0000{self.data}"

    def __getattr__(self, item):
        print(f"Get {item}")
        if item == 'corrupted_data':
            return f"0000{self.data}"
        else:
            raise AttributeError

    # def corrupted_data(self):
    #     return "Method"

    def __setattr__(self, key, value):
        print(f"In setattr {key}: {value}")
        if key == 'owner':
            print("Setting data owner")
            #self.owner = value
            self.__dict__['owner'] = value
        else:
            self.__dict__[key] = value

    def __getattribute__(self, item):
        print(f"In getattribute {item}")
        # if item == 'data':
        #     return self.data
        # return self.__dict__[item] # error
        return super().__getattribute__(item)



# import sys
# sys.setrecursionlimit()

data = Data("4f7fgfwfqgffwgffwgwfjhg")
#print(data.get_corrupted_data())
print(data.data)
print(data.corrupted_data)
#print(data.unknown_data)
data.owner = 'Aleksey'