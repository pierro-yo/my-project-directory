from lib.gratitudes import *

def test_add_item_to_list():
    add_item = Gratitudes()
    add_item.add("motorbikes")
    result = add_item.format()
    assert result == "Be grateful for: motorbikesls"