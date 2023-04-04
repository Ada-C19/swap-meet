import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item


def test_swap_by_newest_returns_true():
    item_a = Item(age=2)
    item_b = Item(age=5)
    item_c = Item(age=10)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=3)
    item_e = Item(age=1)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert result
    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 2
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_e in fatimah.inventory
    assert item_e not in jolie.inventory
    assert item_a in jolie.inventory
    assert item_d in jolie.inventory


def test_swap_by_newest_my_empty_returns_false():
    fatimah = Vendor(inventory=[])

    item_d = Item(age=3)
    item_e = Item(age=1)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 2
    assert not result


def test_swap_by_newest_their_empty_returns_false():
    item_a = Item(age=2)
    item_b = Item(age=5)
    item_c = Item(age=10)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(inventory=[])

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 0
    assert not result
