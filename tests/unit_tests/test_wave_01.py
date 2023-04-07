# The following line imports the Vendor class from the module vendor inside the swap_meet package.
import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item


def test_vendor_has_inventory():
    vendor = Vendor()
    assert len(vendor.inventory) == 0

'''
updated test to accomodate new functionality that only allows instances
of Item or its subclasses to be in the inventory list attribute
'''
def test_vendor_takes_optional_inventory():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    inventory = [item_a, item_b, item_c]
    vendor = Vendor(inventory=inventory)
    assert len(vendor.inventory) == 3
    assert item_a in vendor.inventory
    assert item_b in vendor.inventory
    assert item_c in vendor.inventory

'''
updated tests to accomodate new functionality that only allows add method
to add instances of Item or its subclasses to the inventory list attribute
'''
def test_adding_to_inventory():
    vendor = Vendor()
    item = Item()

    result = vendor.add(item)

    assert len(vendor.inventory) == 1
    assert item in vendor.inventory
    assert result == item

'''
updated test to accomodate new functionality that only allows instances
of Item or its subclasses to be in the inventory list attribute
'''
def test_removing_from_inventory_returns_item():
    remove_item = Item()
    item_a = Item()
    item_b = Item()
    item_c = Item()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, remove_item]
    )

    result = vendor.remove(remove_item)

    assert len(vendor.inventory) == 3
    assert remove_item not in vendor.inventory
    assert result == remove_item

'''
updated test to accomodate new functionality that only allows instances
of Item or its subclasses to be in the inventory list attribute
'''
def test_removing_not_found_is_false():
    remove_item = Item()
    item_a = Item()
    item_b = Item()
    item_c = Item()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = vendor.remove(remove_item)

    assert result == False