class Wrapper:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __getattr__(self, item):
        print(f"Delegation: {item}")
        #return getattr(self.wrapped, item)
        res = self.wrapped.__getattribute__(item)
        print(res)
        return self.wrapped.__getattribute__(item)

    def __getitem__(self, item):
        return self.wrapped.__getitem__(item)

    # def append(self, item):
    #     print("Append of Wrapper")
    #     self.wrapped.append(item)

    def method_of_wrapper(self):
        print("Pure wrapper method")

    # def __getattribute__(self, item):
    #     print("In __getattribute__")
    #     return super().__getattribute__(item)



lst = Wrapper([1, 2, 3, 4])
print(lst.wrapped)
lst.method_of_wrapper()
lst.append(3)
print(lst.wrapped)
print(lst[3])  # magic methods can't be caught that's why need to implement them
