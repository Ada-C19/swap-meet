import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=1)
    item_b = Electronics(age=2)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=1)
    item_e = Decor(age=2)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_c, item_d]
    assert jesse.inventory == [item_e, item_f, item_a]

#@pytest.mark.skip
def test_swap_by_newest_reordered():
    # Arrange
    # me
    item_a = Decor(age=1)
    item_b = Electronics(age=2)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    # them
    item_d = Clothing(age=1)
    item_e = Decor(age=2)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_c, item_b, item_d]
    assert jesse.inventory == [item_f, item_e, item_a]

#@pytest.mark.skip
def test_swap_by_neweest_no_inventory():
    # Arrange
    # me
    tai = Vendor(
        inventory=[]
    )

    # them
    item_d = Clothing(age=1)
    item_e = Decor(age=2)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == False
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert tai.inventory == []
    assert jesse.inventory == [item_d, item_e, item_f]

#@pytest.mark.skip
def test_swap_by_newest_no_other_inventory():
    # Arrange
    # me
    item_a = Decor(age=1)
    item_b = Electronics(age=2)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse)
    
    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert tai.inventory == [item_a, item_b, item_c]
    assert jesse.inventory == []

#@pytest.mark.skip
def test_if_instance_is_not_int():
    # Arrange
    with pytest.raises(ValueError):
        item = Item(id="abc")
    
