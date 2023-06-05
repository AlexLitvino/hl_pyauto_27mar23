from unittest import TestCase, main
import sys
sys.path.insert(0, r'/home/olytvynov/Projects/HL/hl_pyauto_27mar23')


from L20.car import Car


class TestCar(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("In setup class")

    def setUp(self) -> None:
        print("In setup")

    def test_default_numbers_of_seats(self):
        print("In test: test_default_numbers_of_seats")
        car = Car('ABC1234', 'Martin Stuart')
        self.assertEqual(car.number_of_seats, 5, 'Number of seats is not 5 by default')

    def test_adding_passengers(self):
        print("In test: test_adding_passengers")
        car = Car('ABC1234', 'Martin Stuart')
        car.add_passenger('Andrew Olafson')
        self.assertIn('Andrew Olafsons', car.passengers, 'Andrew Olafson is not in passengers')

    def tearDown(self) -> None:
        print("In teardown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("In tear down class")


if __name__ == '__main__':
    main()
