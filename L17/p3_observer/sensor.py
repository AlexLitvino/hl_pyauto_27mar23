import random


class Sensor:

    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_all(self):
        temperature = self.get_current_temperature()
        for subscriber in  self._subscribers:
            subscriber.update(temperature)

    def notify(self, subscriber):
        temperature = self.get_current_temperature()
        subscriber.update(temperature)

    def get_current_temperature(self):
        return 12 + 20 * random.random()
