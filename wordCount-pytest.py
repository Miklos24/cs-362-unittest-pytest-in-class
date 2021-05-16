from wordCount import getWordCount
import pytest

def test_simple_sentence():
    assert getWordCount("Hi I'm Bob.") == 3
    
def test_number():
    with pytest.raises(AttributeError):
        getWordCount(1234)
    
def test_extra_spaces():
    assert getWordCount("   Hi I'm     Bob.  ") == 3
