from lib.counter import *

def test_to_add_numbers_in_class():
    maths = Counter()
    maths.add(10)
    result = maths.report()
    assert result == f"Counted to {10} so far."
    