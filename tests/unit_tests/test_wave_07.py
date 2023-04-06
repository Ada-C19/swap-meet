import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_newest():
    item_a = Clothing(age=50)
    item_b = Decor(age=40)
    item_c = Clothing(age=30)
    item_d = Decor(age=20)
    item_e = Clothing(age=10)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest()

    assert newest_item.age == 10

def test_get_newest_with_duplicates():
    item_a = Item(age=40)
    item_b = Item(age=20)
    item_c = Clothing(age=20)
    croissant = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = croissant.get_newest()

    assert newest_item.age == 20

def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=20)
    item_b = Electronics(age=40)
    item_c = Decor(age=30)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=20)
    item_e = Decor(age=40)
    item_f = Clothing(age=40)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)
    # Assert
    assert result is True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_c, item_d]
    assert jesse.inventory == [item_e, item_f, item_a]

def test_swap_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=20)
    item_b = Decor(age=40)
    item_c = Clothing(age=40)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(jesse)

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

def test_swap_newest_their_inventory_empty_is_false():
    item_a = Clothing(age=20)
    item_b = Decor(age=40)
    item_c = Clothing(age=40)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory