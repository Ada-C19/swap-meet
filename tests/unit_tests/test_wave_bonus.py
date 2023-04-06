import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_by_age_success():
    #arrange
    item_a = Item(age=10)
    item_b = Item(age=20)
    item_c = Item(age=30)
    item_d = Item(age=15)
    item_e = Item(age=5)
    
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )
    
    #act
    items = vendor.get_by_age(20)
    

    #assert
    assert len(items) == 1
