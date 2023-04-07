import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_one_vendor_empty():
    # Test swapping when one vendor has no items
    item_a = Decor(age=5)
    tai = Vendor(
        inventory=[item_a]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    assert not result, "Expected swap_best_by_category to return False when one vendor has no items"
    assert len(tai.inventory) == 1, "Expected tai's inventory to have 1 item"
    assert len(jesse.inventory) == 0, "Expected jesse's inventory to have 0 items"
    assert item_a in tai.inventory, "Expected item_a to be in tai's inventory"

#  @pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    item_a = Decor(age=5)
    item_b = Electronics(age = 4)
    item_c = Decor(age = 1)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age = 3)
    item_e = Decor(age = 1)
    item_f = Clothing(age = 0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse
    )
    # Assert
    assert result, "Expected swap_best_by_category to return truthy value"
    assert len(tai.inventory) == 3, "Expected tai's inventory to have 3 items"
    assert len(jesse.inventory) == 3, "Expected jesse's inventory to have 3 items"
    assert item_a in tai.inventory, "Expected item_a to be in tai's inventory"
    assert item_b in tai.inventory, "Expected item_b to be in tai's inventory"
    assert item_f in tai.inventory, "Expected item_e to be in tai's inventory"
    assert item_d in jesse.inventory, "Expected item_d to be in jesse's inventory"
    assert item_e in jesse.inventory, "Expected item_f to be in jesse's inventory"
    assert item_c in jesse.inventory, "Expected item_c to be in jesse's inventory"
    assert item_c not in tai.inventory, "Expected item_c to not be in tai's inventory"
    assert item_f not in jesse.inventory, "Expected item_f to not be in jesse's inventory"
    # additional assert statements
    assert item_e not in tai.inventory, "Expected item_e to not be in tai's inventory"
    assert item_d not in tai.inventory, "Expected item_d to not be in tai's inventory"
    assert item_b not in jesse.inventory, "Expected item_b to not be in jesse's inventory"
    assert item_a not in jesse.inventory, "Expected item_a to not be in jesse's inventory"


    #  @pytest.mark.skip
def test_swap_by_newest_both_have_same_item():
    # Test swapping when both vendors have the same newest item
    # Arrange
    item_a = Electronics(age = 7)
    item_b = Electronics(age = 4)
    # Act
    tai = Vendor(
        inventory=[item_b, item_a]
    )

    jesse = Vendor(
        inventory=[item_b]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse
    )
    # Assert
    assert result, "Expected swap_by_newest to return True when both vendors have the same newest item"
    assert len(tai.inventory) == 2, "Expected tai's inventory to have 2 items"
    assert len(jesse.inventory) == 1, "Expected jesse's inventory to have 1 item"
    assert item_a in tai.inventory, "Expected item_a to be in tai's inventory"
    assert item_b in jesse.inventory, "Expected item_b to be in jesse's inventory"
    assert item_b in tai.inventory, "Expected item_b to not be in tai's inventory"

# @pytest.mark.skip
def test_swap_by_newest_other_has_newer_item():
    # Test swapping when the other vendor has a newer item
    # Arrange
    item_a = Electronics(age = 7)
    item_b = Electronics(age = 4)
    item_c = Electronics(age = 2)
    # Act
    tai = Vendor(
        inventory=[item_b, item_a]
    )

    jesse = Vendor(
        inventory=[item_b, item_c]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse
    )
    # Assert
    assert result, "Expected swap_by_newest to return True when other vendor has newer item"
    assert len(tai.inventory) == 2, "Expected tai's inventory to have 2 items"
    assert len(jesse.inventory) == 2, "Expected jesse's inventory to have 2 items"
    assert item_c in tai.inventory, "Expected item_c to be in tai's inventory"
    assert item_b in jesse.inventory, "Expected item_b to be in jesse's inventory"
    assert item_a in tai.inventory, "Expected item_a to not be in tai's inventory"

# @pytest.mark.skip
def test_swap_by_newest_self_has_newer_item():
    # Test swapping when the self vendor has a newer item
    # Arrange
    item_a = Electronics(age = 7)
    item_b = Electronics(age = 4)
    item_c = Electronics(age = 2)
    # Act
    tai = Vendor(
        inventory=[item_b, item_c]
    )

    jesse = Vendor(
        inventory=[item_b, item_a]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse
    )
    # Assert
    assert result, "Expected swap_by_newest to return True when self vendor has newer item"
    assert len(tai.inventory) == 2, "Expected tai's inventory to have 2 items"
    assert len(jesse.inventory) == 2, "Expected jesse's inventory to have 2 items"
    assert item_a in jesse.inventory, "Expected item_a to be in tai's inventory"
    assert item_c in jesse.inventory, "Expected item_c to be in jesse's inventory"
    assert item_b not in jesse.inventory, "Expected item_c to be in jesse's inventory"
    assert item_b in tai.inventory, "Expected item_b to not be in tai's inventory"

