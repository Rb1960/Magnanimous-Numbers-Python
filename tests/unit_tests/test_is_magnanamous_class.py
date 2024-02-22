"""
The test class provides all unit tests for the finction:
is_mangnanimous(candidate) -> bool:

"""
import pytest
from source.magnanimous_numbers import is_magnanimous


class TestIsMagnanimous:
    
    @pytest.mark.parametrize("value", [0, 9])
    def test_accept_single_digit_numbers(self, value):
        """
        single digit numbers are considered Manganimous so the function will return True
        :return:
        """
        assert is_magnanimous(value) is True
    
    def test_negative_numbers_return_false(self):
        assert is_magnanimous(-1) is False
    
    @pytest.mark.parametrize("value", [-0.0, 0.0, "a value"])
    def test_non_ints_return_false(self, value):
        assert is_magnanimous(value) is False
    
    def test_recognize_valid_number(self):
        assert is_magnanimous(6425) is True
    
    def test_reject_valid_number_but_not_magnanimous(self):
        assert is_magnanimous(3538) is False
