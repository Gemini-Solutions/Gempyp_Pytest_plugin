from  basic_ops import *
import pytest


@pytest.mark.reverse
def test_string_reverse():
    text = reverse("pytest")
    assert(text == "tsetyp")

# @pytest.mark.reverse
def test_list_reverse():
    reversed_list = reverse([89 ,56 , 'abd', 34])
    assert(reversed_list == [34, 'abd', 56, 89])
    
def test_palidrome_string():
    assert(palindromeString("hello") == False)
    
# @pytest.mark.reverse
def test_reverse_number():
    assert(reverseNumber(105) == 501)

@pytest.mark.parametrize("number_1, number_2", [(2,3), (6,5), (10,8)])
def test_calculate_sum(number_1, number_2):
    sum = number_1 + number_2
    assert(calculate_sum(number_1, number_2) == sum)