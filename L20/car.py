import re

import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, format="%(name)s %(asctime)s %(levelname)s %(message)s")


class Car:

    def __init__(self, number_plate, owner, number_of_seats=5):
        logger.info("Initializing car")
        self.number_plate = number_plate
        self.owner = owner
        self.passengers = []
        self.number_of_seats = number_of_seats
        #self.start_loading()


    def add_passenger(self, passenger):
        logger.info(f"Adding {passenger} to passenger list")
        if len(self.passengers) == self.number_of_seats:
            logger.warning("Adding extra passenger")
            raise PassengersNumberExceededError(self.number_of_seats)
        self.passengers.append(passenger)


    def validate_number_plate(self):
        """
        Validates number plate.
        ABC1234
        AB1234C
        :param number_plate:
        :return:
        """
        pattern = r"[a-zA-Z]{3}\d{4}|[a-zA-Z]{2}\d{4}[a-zA-Z]{1}"
        return bool(re.fullmatch(pattern, self.number_plate))


    def start_loading(self):
        print(self.number_plate)
        print("Loading car")

    def close_connection(self):
        print("Closing connection")

    def __str__(self):
        return f"CAR {self.number_plate}\nOWNER: {self.owner}"

    def save_car_info(self, file_path):
        with open(file_path, 'w') as f:
            f.write(str(self))



class CarException(Exception):
    pass


class PassengersNumberExceededError(CarException):

    def __init__(self, number_of_seats):
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Expected {self.number_of_seats} passengers in the car, but one more wants take a seat."


if __name__ == '__main__':

    mini_car = Car('QWE1234', 'Frederick Cruger', number_of_seats=2)
    mini_car.save_car_info('data.txt')

    mini_car.add_passenger('Alan Poe')
    mini_car.add_passenger('Stephen King')
    try:
        mini_car.add_passenger('Lord Bairon')
    except PassengersNumberExceededError as exc:
        print(exc)
        a = 3

