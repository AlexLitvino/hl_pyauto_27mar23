# __add__, __radd__, __iadd__, __del__, __and__ &, __or__ |



class AnimalStr:
    def __str__(self):
        return f"{self.__class__.__name__}(speed: {self.speed} strength: {self.strength})"


class Donkey(AnimalStr):
    def __init__(self):
        self.speed = 1
        self.strength = 4

    def __add__(self, other):
        print("In Donkey ADD")
        return Mul(self.speed + other.speed, self.strength + other.strength)

    def __radd__(self, other):
        print("In Donkey RADD")
        return Mul(self.speed + other.speed, self.strength + other.strength)


class Horse(AnimalStr):
    def __init__(self):
        self.speed = 5
        self.strength = 2

    def __add__(self, other):
        print("In Horse ADD")
        return Mul(self.speed + other.speed, self.strength + other.strength)

    def __radd__(self, other):
        print("In Horse RADD")
        return Mul(self.speed + other.speed, self.strength + other.strength)

    def __iadd__(self, other):
        print("In Horse IADD")
        self.strength += other.strength
        self.speed += other.speed
        return self

    def __del__(self):
        print("Horse is dead")


class Mul(AnimalStr):
    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

donkey = Donkey()
horse = Horse()
#del horse
mule = donkey + horse
print(mule)
# print(mule.speed)
# print(mule.strength)

mule = horse + donkey
print(mule)

horse += donkey
#horse = horse + donkey
print(horse)