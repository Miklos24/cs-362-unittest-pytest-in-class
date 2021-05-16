from palindrome import isPalindrome
import pytest

def test_basic_string():
    assert isPalindrome('racecar')
    
def test_number():
    with pytest.raises(TypeError):
        isPalindrome(12321)

def test_mixed_cases():
    assert not isPalindrome('raCecAR')