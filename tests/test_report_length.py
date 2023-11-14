from lib.report_length import *

def test_report_length_of_hello():
    result = report_length("hello")
    assert result == f"This string was {5} characters long."