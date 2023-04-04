import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Decor(age = 2.0)
    item_b = Electronics(age = 4.0)
    item_c = Decor(age = 4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age = 2.0)
    item_e = Decor(age = 4.0)
    item_f = Clothing(age = 4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse,        
        my_priority="Clothing",
        their_priority="Decor")

    
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory 
