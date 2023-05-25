from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def update(self, temperature):
        pass


class MobileApp(Subscriber):

    def update(self, temperature):
        print(f"MOBILE APP: {temperature}")


class WebApp(Subscriber):

    def update(self, temperature):
        print(f"WEB APP: {temperature}")


class AirConditioneer(Subscriber):

    def __init__(self, min_temp, max_temp):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def update(self, temperature):
        if temperature > self.max_temp:
            print("Cooling...")
        elif temperature < self.min_temp:
            print("Heating...")
        else:
            print("Air cond do nothing...")
