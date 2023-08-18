import pytest
from string_manipulation import *


def test_count_vowels():
    assert count_vowels("hello") == 2
    
def test_count_words():
    assert count_words("Ada Lovelace is the first programmer in the world.") == 9
    
def test_count_consonants():
    string = "hello"
    assert (len(string) - count_vowels(string)) == 3
    
def test_truncate_string():
    sentence = "Ada Lovelace is the first programmer in the world."
    index = 12
    assert trucate_string(sentence, index) == "Ada Lovelace..."
    
def test_remove_char():
    sentence = "Ada Lovelace is the first programmer in the world."
    char = "a"
    assert remove_character_from_string(sentence, char) == "Ad Lovelce is the first progrmmer in the world."