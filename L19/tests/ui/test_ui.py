import pytest

from L19.car import Car


# @pytest.fixture
# def default_car():
#     print("==== IN UI MODULE ====")
#     car = Car('ABC5466', 'Anna')
#     car.start_loading()
#     yield car
#     car.close_connection()

@pytest.fixture()
def number():
    return 432626

def test_plate_number(default_car, number):
    default_car.number_plate = 'ABC54667'
    print(number)
    assert default_car.number_plate == 'ABC54667'