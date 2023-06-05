import sys
import pytest

sys.path.append(r"/home/olytvynov/Projects/HL/hl_pyauto_27mar23")

from L20.tests.p3_cov_example.structure_without_list import StructureWithoutList


def test_adding_one_element_new():
    struct = StructureWithoutList()
    struct.add(1)
    assert 1 == struct.get(1)


def test_adding_two_elements():
    struct = StructureWithoutList()
    struct.add(1)
    struct.add(2)
    assert 1 == struct.get(1)
    assert 2 == struct.get(2)

# TODO: test adding elements when HEAD not at the end
def test_adding_elements_when_head_not_a_the_end(structure_of_4_elements_index_on_the_second_item):
    structure_of_4_elements_index_on_the_second_item.add(5)
    assert 1 == structure_of_4_elements_index_on_the_second_item.get(1)
    assert 2 == structure_of_4_elements_index_on_the_second_item.get(2)
    assert 3 == structure_of_4_elements_index_on_the_second_item.get(3)
    assert 4 == structure_of_4_elements_index_on_the_second_item.get(4)
    assert 5 == structure_of_4_elements_index_on_the_second_item.get(5)

def test_get_elements_in_forward_direction(structure_of_4_elements_index_at_the_end):
    assert 1 == structure_of_4_elements_index_at_the_end.get(1)
    assert 2 == structure_of_4_elements_index_at_the_end.get(2)
    assert 3 == structure_of_4_elements_index_at_the_end.get(3)
    assert 4 == structure_of_4_elements_index_at_the_end.get(4)


def test_get_elements_in_backward_direction(structure_of_4_elements_index_at_the_end):
    assert 4 == structure_of_4_elements_index_at_the_end.get(4)
    assert 3 == structure_of_4_elements_index_at_the_end.get(3)
    assert 2 == structure_of_4_elements_index_at_the_end.get(2)
    assert 1 == structure_of_4_elements_index_at_the_end.get(1)


def test_get_element_from_empty_structure(empty_structure):
    with pytest.raises(IndexError):
        assert empty_structure.get(1)


# def test_get_zero_element_from_non_empty_structure(structure_of_4_elements_index_at_the_end):
#     with pytest.raises(IndexError):
#         assert structure_of_4_elements_index_at_the_end.get(0)


def test_get_element_with_index_greater_than_length(structure_of_4_elements_index_at_the_end):
    with pytest.raises(IndexError):
        assert structure_of_4_elements_index_at_the_end.get(5)


def test_delete_first_element(structure_of_4_elements_index_at_the_end):
    structure_of_4_elements_index_at_the_end.delete(1)
    assert 2 == structure_of_4_elements_index_at_the_end.get(1)
    assert 3 == structure_of_4_elements_index_at_the_end.get(2)
    assert 4 == structure_of_4_elements_index_at_the_end.get(3)
    assert 3 == structure_of_4_elements_index_at_the_end.length


# def test_delete_element_in_the_middle(structure_of_4_elements_index_at_the_end):
#     structure_of_4_elements_index_at_the_end.delete(3)
#     assert 1 == structure_of_4_elements_index_at_the_end.get(1)
#     assert 2 == structure_of_4_elements_index_at_the_end.get(2)
#     assert 4 == structure_of_4_elements_index_at_the_end.get(3)
#     assert 3 == structure_of_4_elements_index_at_the_end.length


def test_delete_last_element(structure_of_4_elements_index_at_the_end):
    structure_of_4_elements_index_at_the_end.delete(4)
    assert 1 == structure_of_4_elements_index_at_the_end.get(1)
    assert 2 == structure_of_4_elements_index_at_the_end.get(2)
    assert 3 == structure_of_4_elements_index_at_the_end.get(3)
    assert 3 == structure_of_4_elements_index_at_the_end.length


# TODO: delete in reverse and random order

def test_delete_all_elements(structure_of_4_elements_index_at_the_end):
    structure_of_4_elements_index_at_the_end.delete(4)
    structure_of_4_elements_index_at_the_end.delete(3)
    structure_of_4_elements_index_at_the_end.delete(2)
    structure_of_4_elements_index_at_the_end.delete(1)
    assert 0 == structure_of_4_elements_index_at_the_end.length


def test_delete_element_from_empty_structure(empty_structure):
    with pytest.raises(IndexError):
        assert empty_structure.delete(1)


def test_delete_zero_element_from_non_empty_structure(structure_of_4_elements_index_at_the_end):
    with pytest.raises(IndexError):
        assert structure_of_4_elements_index_at_the_end.delete(0)


def test_delete_element_with_index_greater_than_length(structure_of_4_elements_index_at_the_end):
    with pytest.raises(IndexError):
        assert structure_of_4_elements_index_at_the_end.delete(5)


def test_get_exc():
    lst = StructureWithoutList()
    with pytest.raises(IndexError):
        lst.get(3)


@pytest.fixture()
def empty_structure():
    return StructureWithoutList()


@pytest.fixture()
def structure_of_4_elements_index_at_the_end():
    struct = StructureWithoutList()
    struct.add(1)
    struct.add(2)
    struct.add(3)
    struct.add(4)
    return struct

@pytest.fixture()
def structure_of_4_elements_index_on_the_second_item():
    struct = StructureWithoutList()
    struct.add(1)
    struct.add(2)
    struct.add(3)
    struct.add(4)
    struct.get(2)
    return struct

