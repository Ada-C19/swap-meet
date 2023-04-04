import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Item(age=0)
    item_b = Item(age=1)
    item_c = Item(age=2)
    item_d = Item(age = 1)
    vendor = Vendor(
        inventory=[item_a, item_b]
    )
    other_vendor = Vendor(
        inventory=[item_c, item_d]
        )
    
    result = vendor.swap_by_newest(other_vendor)

    assert result == True
    assert len(vendor.inventory) == 2
    assert len(other_vendor.inventory) == 2
    assert item_b in vendor.inventory
    assert item_d in vendor.inventory
    assert item_a in other_vendor.inventory
    assert item_c in other_vendor.inventory


def test_swap_by_newest_empty_inventory():
    item_a = Item(age=0)
    item_b = Item(age=1)
    vendor = Vendor(
        inventory=[item_a, item_b]
    )
    other_vendor = Vendor()
    
    result = vendor.swap_by_newest(other_vendor)

    assert result == False
    assert len(vendor.inventory) == 2
    assert len(other_vendor.inventory) == 0
    assert item_b in vendor.inventory
    assert item_a in vendor.inventory

def test_swap_by_newest_tie():
    item_a = Item(age=0)
    item_b = Item(age=0)
    item_c = Item(age=2)
    item_d = Item(age = 1)
    vendor = Vendor(
        inventory=[item_a, item_b]
    )
    other_vendor = Vendor(
        inventory=[item_c, item_d]
        )
    
    result = vendor.swap_by_newest(other_vendor)

    assert result == True
    assert len(vendor.inventory) == 2
    assert len(other_vendor.inventory) == 2
    assert item_b in vendor.inventory
    assert item_d in vendor.inventory
    assert item_a in other_vendor.inventory
    assert item_c in other_vendor.inventory