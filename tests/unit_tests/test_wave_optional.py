import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_newest_item_is_returned():
    item_a = Clothing(age=12)
    item_b = Decor(age=1)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=6)
    kat = Vendor(inventory=[item_a, item_b, item_c, item_d, item_e])
    
    result = kat.get_newest_item()
    
    assert result is item_b

# @pytest.mark.skip
def test_newest_with_duplicates():
    item_a = Clothing(age=12)
    item_b = Decor(age=12)
    item_c = Clothing(age=4)
    item_d = Decor(age=4)
    item_e = Clothing(age=6)
    kat = Vendor(inventory=[item_a, item_b, item_c, item_d, item_e])
    
    result = kat.get_newest_item()
    
    assert result is item_c

# @pytest.mark.skip
def test_swap_newest():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # arrange
    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_newest_item(
        other_vendor=jesse
    )

    assert result
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_b in tai.inventory
    assert item_f in jesse.inventory
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory

# @pytest.mark.skip
def test_swap_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_newest_item(
        other_vendor=jesse
    )
    
    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_newest_no_other_inventory_is_false():
    jesse = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = jesse.swap_newest_item(
        other_vendor=tai
    )
    
    assert not result
    assert len(jesse.inventory) == 0
    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory