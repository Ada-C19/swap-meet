import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor

def test_item_has_age():
    item_a = Item(0)
    item_b = Item(2)
    item_c = Item(3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    
    assert fatimah.inventory[0].age == 0
    assert fatimah.inventory[1].age == 2
    assert fatimah.inventory[2].age == 3
    

def test_swap_by_newest_returns_True():
    item_a = Item(0)
    item_b = Item(2)
    item_c = Item(3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(1)
    item_e = Item(2)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_a in jolie.inventory
    assert result