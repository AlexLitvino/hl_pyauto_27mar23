from L20.car import Car


import pytest

@pytest.fixture()
def data():
    print("Setup data")
    data = 42
    yield data
    print("Tear down data")

@pytest.mark.xfail
class TestCar:

    def setup_class(self):
        print("Setup class")
        self.car = Car('ABC1234', 'John')
        self.car.start_loading()

    def setup_method(self):
        print("Setup method")

    @pytest.mark.skip(reason='Just skip')
    def test_default_seating_number(self):
        #car = Car('ABC1234', 'John')
        #assert car.number_of_seats == 5
        assert self.car.number_of_seats == 5

    def test_default_seating_number_2(self):
        #car = Car('ABC1234', 'John')
        #assert car.number_of_seats == 5
        self.car.number_of_seats = 3
        assert self.car.number_of_seats == 3


    def test_default_seating_number_3(self):
        #car = Car('ABC1234', 'John')
        #assert car.number_of_seats == 5
        assert self.car.number_of_seats == 5

    def test_valid_number(self):
        car = Car('ABC1234', 'John')
        assert car.validate_number_plate()

    def test_simple_data(self, data):
        assert data == 43

    def teardown_method(self):
        print("Teardown method")
        self.car.number_of_seats = 5

    def teardown_class(self):
        print("Teardown class")
        self.car.close_connection()


@pytest.mark.parametrize('number,owner', [('ABC1234', 'John'), ('QWE5467', 'Anna')])
class TestCarParametrized:

    def test_validate_number(self, number, owner):
        car = Car(number, owner)
        assert car.validate_number_plate()

    def test_seating_numbers(self, number, owner):
        car = Car(number, owner)
        assert car.number_of_seats == 5
