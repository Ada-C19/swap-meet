import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_newest_by_category():
    item_a = Clothing(age=1)
    item_b = Electronics(age=3)
    item_c = Electronics(age=2)

    vendor = Vendor(inventory=
                    [item_a, item_b, item_c])
    
    items = vendor.get_newest_by_category("Electronics")

    assert items == item_c

def test_same_age():
    item_a = Decor(age=6)
    item_b = Clothing(age=1)
    item_c = Electronics(age=3)
    item_d = Decor(age=6)

    vendor = Vendor(inventory=
                    [item_a, item_b, item_c, item_d])
    
    items = vendor.get_newest_by_category("Decor")

    assert items == item_a