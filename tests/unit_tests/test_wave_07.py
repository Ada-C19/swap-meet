import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor

def test_swap_by_newest():
    # Arrange
    item_a = Item(age=3.0)
    item_b = Item(age=0.0)
    item_c = Item(age=5.7)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=0.5)
    item_e = Item(age=2.0)
    item_f = Item(age=3.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    # Assert
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_d in tai.inventory
    assert item_c in tai.inventory
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

