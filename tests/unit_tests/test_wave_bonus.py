import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor

def test_swap_by_newest_is_True():
    #Arrange
    item_a= Item(age=5)
    item_b= Item(age=6)
    item_c= Item(age=7)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    
    item_d= Item(age=8)
    item_e= Item(age=9)
    item_f= Item(age=4)
    jesse = Vendor(inventory=[item_d, item_e, item_f])

    #Act
    result = jesse.swap_by_newest(other_vendor=tai)

    #Assert
    assert result is not False 
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory 
    assert item_f in tai.inventory

