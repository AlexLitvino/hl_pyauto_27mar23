class Donkey:

    name = 'Donny'

    def __init__(self):
        print("IN CONSTRUCTOR DONKEY")
        self.strength = 54

    def say(self):
        print('Ia-ia')


class Horse:

    name = 'Vognyk'

    def __init__(self):
        print("IN CONSTRUCTOR HORSE")
        self.speed = 87

    def say(self):
        print('Ig-go')


class Mule(Horse, Donkey):

    name = 'Just mule'

    def __init__(self):
        Donkey.__init__(self)
        Horse.__init__(self)

    def print_parents_name(self):
        print(f"{Donkey.name} and {Horse.name}")

    @classmethod
    def set_name(cls):
        cls.name = Donkey.name + ' ' + Horse.name

    def say(self):
        Donkey.say(self)
        Horse.say(self)

mule = Mule()
print(mule.strength)
print(mule.speed)
print(mule.name)
mule.print_parents_name()
Mule.set_name()
print(mule.name)
mule.say()