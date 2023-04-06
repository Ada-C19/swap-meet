import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other_vendor=jesse)

    assert result == True
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3


def test_swap_by_newest_my_empty_returns_False():
    # me
    tai = Vendor()

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(other_vendor=jesse)

    assert not result


def test_swap_by_newest_their_empty_returns_False():
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    jesse = Vendor()

    result = tai.swap_by_newest(other_vendor=jesse)

    assert not result