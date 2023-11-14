from lib.greet import *

def test_greet_user():
    result = greet("piers")
    assert result == "Hello, piers!"