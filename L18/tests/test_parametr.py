import pytest

from L18.car import Car


# def test_valid_1():
#     car = Car('ABC1234', 'John')
#     assert car.validate_number_plate()
#
# def test_valid_2():
#     car = Car('AB1234C', 'John')
#     assert car.validate_number_plate()
#
# def test_valid_3():
#     car = Car('QE1234C', 'John')
#     assert car.validate_number_plate()

# @pytest.mark.parametrize("number,owner", [('ABC1234', 'John'),
#                                           ('AB1234C', 'Anna'),
#                                           ('QE1234C', 'James')])
# def test_valid_all(number, owner):
#     car = Car(number, owner)
#     assert car.validate_number_plate()

# test_data = [('ABC1234', 'John'), ('AB1234C', 'Anna'), ('QE1234C', 'James')]
# @pytest.mark.parametrize("number,owner", test_data)
# def test_valid_all(number, owner):
#     car = Car(number, owner)
#     assert car.validate_number_plate()


# @pytest.mark.parametrize("number,owner", [('ABC1234', 'John'),
#                                           ('AB1234C', 'Anna'),
#                                           ('QE1234C', 'James')], ids=["min", "min+1", "nominal"])
# def test_valid_all(number, owner):
#     car = Car(number, owner)
#     assert car.validate_number_plate()

# def ids_func(value):
#     return f"Q{value}Q"
#
#
# @pytest.mark.parametrize("number,owner", [('ABC1234', 'John'),
#                                           ('AB1234C', 'Anna'),
#                                           ('QE1234C', 'James')], ids=ids_func)
# def test_valid_all(number, owner):
#     car = Car(number, owner)
#     assert car.validate_number_plate()

# test_data = [pytest.param('ABC1234', 'John', id="first"),
#              pytest.param('AB1234C', 'Anna', marks=pytest.mark.skip(reason="Just"), id="second"),
#              pytest.param('QE1234C', 'James', id="third")]
#
#
# @pytest.mark.parametrize("number,owner", test_data)
# def test_valid_all(number, owner):
#     car = Car(number, owner)
#     assert car.validate_number_plate()

def add(a, b):
    return a+b

@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [1, 2, 3])
def test_add(a, b):
    assert add(a, b) > 0
