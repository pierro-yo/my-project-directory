from lib.check_codeword import *

def test_check_codeword_isTrue():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_isElif():
    result = check_codeword("he")
    assert result == "Close, but nope."

def test_check_codeword_isFalse():
    result = check_codeword("hello")
    assert result == "WRONG!"