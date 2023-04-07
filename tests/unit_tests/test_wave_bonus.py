
import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age = 6)
    item_e = Decor(age = 4)
    item_f = Clothing(age = 3)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse,
        
    )

   
    assert result is True
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_c in jesse.inventory 
    assert item_f in tai.inventory 
