import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_get_newest_item():
    item_a = Item(age = 4)
    item_b = Item(age = 10)
    item_c = Item(age = 1)
    rika = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = rika.get_newest_item()

    assert result == item_c

#@pytest.mark.skip
def test_swap_by_newest():
    item_a = Item(age = 4)
    item_b = Item(age = 10)
    item_c = Item(age = 1)
    rika = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age = 7)
    item_e = Item(age = 10)
    item_f = Item(age = 4)
    stacy = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = rika.swap_by_newest(stacy)

    assert item_c in stacy.inventory
    assert item_f in rika.inventory
    assert result == True
    assert len(rika.inventory) == 3
    assert len(stacy.inventory) == 3