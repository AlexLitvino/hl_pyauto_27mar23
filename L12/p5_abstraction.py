import abc

class Cat(abc.ABC):
#class Cat(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name
        self.health = 50

    def feed(self, amount):
        self.health += amount

    @abc.abstractmethod
    def meow(self):
        raise NotImplementedError

    #@abc.abstractstaticmethod

    @staticmethod
    @abc.abstractmethod
    def calculate():
        pass


class DomesticCat(Cat):
    pass

    def meow(self):
        print("Meow")

class WildCat(Cat):

    def meow(self):
        print("Rrrr!")

# cat = Cat('Cat')
# cat.meow()

domestic = DomesticCat('Murzik')
domestic.meow()
wild = WildCat('Simba')
wild.meow()