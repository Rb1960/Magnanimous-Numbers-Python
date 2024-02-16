"""
test function to list N Magnanimous_numbers
"""
import pytest

from source.number_utils import list_numbers, find_between


@pytest.fixture
def run_app():
    return list_numbers(45)


def test_list_45_numbers_length_correct(run_app):
    number_list = run_app
    assert len(number_list) == 45


def test_correct_45_numbers(run_app):
    number_list = run_app
    assert number_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                           11, 12, 14, 16,
                           20, 21, 23, 25, 29,
                           30, 32, 34, 38,
                           41, 43, 47, 49,
                           50, 52, 56, 58,
                           61, 65, 67,
                           70, 74, 76,
                           83, 85, 89,
                           92, 94, 98,
                           101, 110]


def test_find_between_241_250():
    number_list = find_between(241, 250)
    assert number_list == [17992, 19972,
                           20209, 20261, 20861,
                           22061, 22201, 22801, 22885,
                           24407]


def test_find_between_391_400():
    number_list = find_between(391, 400)
    assert number_list == [486685, 488489,
                           515116,
                           533176,
                           551558, 559952,
                           595592, 595598,
                           600881, 602081,
                           
                           ]
