import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_by_age_success():
    #arrange
    item_a = Item(age=10)
    item_b = Item(age=20)
    item_c = Item(age=30)
    item_d = Item(age=15)
    item_e = Item(age=5)
    
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )
    
    #act
    items = vendor.get_by_age(20)
    

    #assert
    assert len(items) == 1

def test_swap_by_newest():
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

