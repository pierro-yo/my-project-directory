from lib.string_builder import *

def test_to_return_made_strings():
    aString = StringBuilder()
    aString.add("hello")
    result = aString.output()
    assert result == "hello"

def test_to_return_input_string_length():
    count_string = StringBuilder()
    count_string.add("hi")
    result = count_string.size()
    assert result == 2