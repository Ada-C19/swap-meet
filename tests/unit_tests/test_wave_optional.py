import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Decor(age=2.4)
    item_b = Electronics(age=4.4)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2.9)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=1.5)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = tai.swap_by_newest(other_vendor=jesse)

    assert result   
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    
    assert item_a in jesse.inventory
    assert item_f in tai.inventory
    assert item_a not in tai.inventory
    assert item_f not in jesse.inventory

def test_swap_by_newest_empty_inventory_is_false():
    item_a = Decor(age=2.4)
    item_b = Electronics(age=4.4)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(other_vendor=jesse)

    assert result == None
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory