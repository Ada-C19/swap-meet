import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_newest_by_category():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    pedro = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = pedro.get_best_by_category("Clothing")

    assert newest_item.get_category() == "Clothing"
    assert newest_item.age == pytest.approx(2.0)

def test_swap_newest_by_category():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Electronics(age=1.0)
    pedro = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Clothing(age=4.0)
    item_f = Electronics(age=1.0) 
    juan = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = pedro.swap_newest_by_category(
        other_vendor=juan,
        my_priority="Clothing",
        their_priority="Decor"
    )

    #Assert
    assert result 
    assert len(pedro.inventory) == 3
    assert len(juan.inventory) == 3

    assert item_b in pedro.inventory
    assert item_c in pedro.inventory
    assert item_d in pedro.inventory
    
    assert item_a in juan.inventory
    assert item_e in juan.inventory
    assert item_f in juan.inventory