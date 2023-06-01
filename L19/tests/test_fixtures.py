import pytest

from L19.car import Car

# @pytest.fixture
# def default_car():
#     car = Car('ABC5466', 'Anna')
#     car.start_loading()
#     #raise Exception # error
#     yield car
#     car.close_connection()


# # bad test
# def test_plate_number():
#     car = Car('ABC5466', 'Anna')
#     car.start_loading()
#     assert car.number_plate == 'ABC54667'
#     car.close_connection()


# def test_plate_number(default_car):
#     #car = Car('ABC5466', 'Anna')
#     default_car.start_loading()
#     assert default_car.number_plate == 'ABC5466'
#     #car.close_connection()
#
# def test_plate_number2(default_car):
#     #car = Car('ABC5466', 'Anna')
#     default_car.start_loading()
#     default_car.number_plate = 'ABC54667'
#     assert default_car.number_plate == 'ABC54667'
#     #car.close_connection()

def test_plate_number(default_car):
    default_car.number_plate = 'ABC54667'
    assert default_car.number_plate == 'ABC54667'


def test_plate_number2(default_car):
    #default_car.number_plate = 'ABC54667'
    assert default_car.number_plate == 'ABC5466'


def test_config_car(configurable_car):
    car = configurable_car('5463565', 'Anna')
    car.number_of_seats = 54
    assert car.number_of_seats == 54


def test_invalid_number(car_with_invalid_number):
    assert not car_with_invalid_number.validate_number_plate()


@pytest.mark.parametrize('number, owner', [('4534554', 'Anna'), ('#$%$%$%%', 'Oksana'), ('', '')], ids=['only numbers', 'special symbols', 'empty'])
def test_car_number_invalid_in_test(number, owner, configurable_car):
    #car = Car(number, owner)
    car = configurable_car(number, owner)
    assert not car.validate_number_plate()


# Pathlib
def test_car_file(default_car, tmp_path):
    print(tmp_path)
    data = tmp_path / 'data'
    data.mkdir()
    file_path = data / 'car_data.txt'
    default_car.save_car_info(file_path)
    with open(file_path, 'r') as f:
        car_data = f.read()

    assert car_data == f"CAR {default_car.number_plate}\nOWNER: {default_car.owner}"


def test_data_for_all(data_for_cars):
    print(data_for_cars)
    with open(data_for_cars, 'r') as f:
        data = f.read()

    assert data

def test_data_for_all2(data_for_cars):
    print(data_for_cars)
    with open(data_for_cars, 'r') as f:
        data = f.read()

    assert data


def test_for_debugging():
    a = 434534
    lst = [5, 6, 7]
    assert a == lst