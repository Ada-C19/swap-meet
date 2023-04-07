import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_age_is_assigned_to_item_instances():
    # Act
    item_a = Clothing(age=2.0)
    item_b = Decor(age=3.0)
    item_c = Electronics(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b]
    )

    item_a_age, item_b_age, item_c_age = item_a.age, item_b.age, item_c.age

    assert item_a_age == 2.0
    assert item_b_age == 3.0
    assert item_c_age == 4.0

def test_get_age_returns_correct_age_value():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b]
    )
    result = item_a.get_age()

    assert result == 2.0

def test_get_by_age_returns_items_with_matching_age():
    item_a = Clothing()
    item_a.age = 2.0  
    item_b = Electronics()
    item_b.age = 3.0
    item_c = Decor()
    item_c.age = 3.0
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )


    items = vendor.get_by_age(3.0)

    assert item_b in items
    assert item_c in items
    assert item_a not in items

def test_get_best_by_age_return_newest_item():
    item_a = Clothing()
    item_a.age = 2.0  
    item_b = Clothing()
    item_b.age = 3.0
    item_c = Clothing()
    item_c.age = 4.0
    item_d = Electronics()
    item_d.age = 1.0
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    result = vendor.get_best_by_age(vendor)

    assert result == item_d

def test_swap_best_by_age_returns_True():
    item_a = Clothing()
    item_a.age = 2.0  
    item_b = Clothing()
    item_b.age = 3.0
    item_c = Clothing()
    item_c.age = 4.0
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    item_d = Clothing()
    item_d.age = 4.0  
    item_e = Clothing()
    item_e.age = 3.0
    item_f = Clothing()
    item_f.age = 2.0
    james = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    result = vendor.swap_best_by_age(james)

    assert result
    assert item_a in james.inventory
    assert item_f in vendor.inventory

def test_items_have_age_descriptions_that_are_the_same_regardless_of_type():
    items = [
        Clothing(age=5),
        Decor(age=5),
        Electronics(age=5)
    ]
    five_age_description = items[0].age_description()
    assert isinstance(five_age_description, str)
    for item in items:
        assert item.age_description() == five_age_description
    items[0].age = 1
    one_age_description = items[0].age_description()
    assert isinstance(one_age_description, str)
    for item in items:
        item.age = 1
        assert item.age_description() == one_age_description

    assert one_age_description != five_age_description