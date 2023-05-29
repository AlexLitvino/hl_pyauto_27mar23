import pytest

from L18.car import Car, PassengersNumberExceededError


# def test_something():
#     print("Start test")
#     assert 2 == 3
#
#
# def test_something2():
#     assert 2 == 2
#
# def add(a, b):
#     return a + b
#
#
# def test_sum_3_5():
#     result = add(3, 5)
#     assert result == 9, f"Expected 9 but received {result}"
#     assert 3 == 3, "Success"

# def test_range():
#     actual = 7.4
#     #assert actual == pytest.approx(5, abs=2)
#     assert actual == pytest.approx(5, rel=0.4)
#     # assert 3 <= actual <= 7
#     # assert 3 <= actual and actual  <= 7
#
# def test_range_list():
#     assert [100, 101, 106] == pytest.approx([100, 100, 100], abs=10)
#
#
# def test_range_list2():
#     assert [100, 101, 106] == [100, 100, 100]


def test_exception():
    print("Start test")
    car = Car('ABC1234', 'John', number_of_seats=3)
    car.add_passenger("P1")
    car.add_passenger("P2")
    car.add_passenger("P3")
    with pytest.raises(PassengersNumberExceededError) as exc_info:
    #with pytest.raises(ArithmeticError) as exc_info:
        car.add_passenger("P4")
    print(exc_info)


