import pytest

from L19.car import Car


@pytest.fixture(scope='function')
def default_number():
    return 'ABC5466'

@pytest.fixture(scope='function')
def default_car(default_number):
    print("==== IN MAIN ====")
    car = Car(default_number, 'Anna')
    car.start_loading()
    yield car
    car.close_connection()

@pytest.fixture(scope='session', autouse=True)
def start_environment():
    print("Start env")
    yield
    print("Stop env")

# start_environment() dont do it

@pytest.fixture(name='short_name')
def fixture_with_looooooooooooooooooooooooooooooooooooooooooooooooong_name():
    return 42


# def start_service():
#     pass
#
# def create_table(start_service):
#     pass


@pytest.fixture(scope='function')
def configurable_car(request):

    def _configure_car(number, owner):

        car = Car(number, owner)

        def stop_car():
            car.close_connection()

        request.addfinalizer(stop_car)

        return car

    return _configure_car


@pytest.fixture(params=[('4534554', 'Anna'), ('#$%$%$%%', 'Oksana'), ('', '')], ids=['only numbers', 'special symbols', 'empty'])
def car_with_invalid_number(request):
    number, owner = request.param
    car = Car(number, owner)
    yield car
    car.close_connection()

@pytest.fixture(scope='session')
def data_for_cars(tmp_path_factory):
    car_data = "cwf483yff7wyfw7fyfe78fy7fyf78eyf78e"
    print(tmp_path_factory)
    data = tmp_path_factory.mktemp('data')
    file_path = data / 'car_data.txt'
    with open(file_path, 'w') as f:
        f.write(car_data)
    return file_path
