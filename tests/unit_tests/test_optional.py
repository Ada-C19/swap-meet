import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_get_newest_age_returns_item():
    item_a = Item(age=10)
    item_b = Item(age=5)
    vendor = Vendor(
        inventory=[item_a, item_b]
    )

    newest_item = vendor.get_newest_item()

    assert newest_item == item_b

def test_swap_by_newest_no_newest_returns_False():
    item_a = Item(age=10)
    item_b = Item(age=5)
    vendor = Vendor(
        inventory=[item_a, item_b]
    )
    other_vendor = Vendor(
        inventory=[]
    )

    result = vendor.swap_by_newest(other_vendor)
    
    assert result is False

def test_swap_by_newest_reordered():
    item_a = Item(age=10)
    item_b = Item(age=5)
    item_c = Item(age=12)
    item_d = Item(age=2)
    vendor = Vendor(
        inventory=[item_a, item_b]
    )
    other_vendor = Vendor(
        inventory=[item_c, item_d]
    )

    result = vendor.swap_by_newest(other_vendor)

    assert result is True
    assert item_b in other_vendor.inventory
    assert item_d in vendor.inventory
    assert len(vendor.inventory) == 2
    assert len(other_vendor.inventory) == 2
