import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_default_item_age():
    item = Item()
    clothing = Clothing()
    decor = Decor()
    electronic = Electronics()

    assert item.age == 0
    assert clothing.age == 0
    assert decor.age == 0
    assert electronic.age == 0

def test_swap_by_newest():
    item_a = Clothing(age=5)
    item_b = Electronics(age=6)
    item_c = Decor(age=3)
    item_d = Decor(age=1)
    item_e = Electronics(age=10)
    item_f = Clothing()

    john = Vendor(inventory=[item_a, item_b, item_c])
    mary = Vendor(inventory=[item_d, item_e, item_f])

    result = john.swap_by_newest(mary)

    assert len(john.inventory) == 3
    assert len(mary.inventory) == 3
    assert result
    assert item_a in john.inventory
    assert item_b in john.inventory
    assert item_c not in john.inventory
    assert item_f in john.inventory
    assert item_d in mary.inventory
    assert item_e in mary.inventory
    assert item_f not in mary.inventory
    assert item_c in mary.inventory

def test_swap_by_newest_different_order():
    item_a = Clothing(age=5)
    item_b = Electronics(age=6)
    item_c = Decor(age=3)
    item_d = Decor(age=1)
    item_e = Electronics(age=10)
    item_f = Clothing()

    john = Vendor(inventory=[item_b, item_c, item_a])
    mary = Vendor(inventory=[item_e, item_f, item_d])

    result = john.swap_by_newest(mary)

    assert len(john.inventory) == 3
    assert len(mary.inventory) == 3
    assert result
    assert item_a in john.inventory
    assert item_b in john.inventory
    assert item_c not in john.inventory
    assert item_f in john.inventory
    assert item_d in mary.inventory
    assert item_e in mary.inventory
    assert item_f not in mary.inventory
    assert item_c in mary.inventory   

def test_swap_by_newest_no_inventory_is_false():
    item_a = Clothing(age=5)
    item_b = Electronics(age=6)
    item_c = Decor(age=3)
    item_d = Decor(age=1)
    item_e = Electronics(age=10)
    item_f = Clothing()

    john = Vendor(inventory=[item_a, item_b, item_c])
    mary = Vendor(inventory=[item_d, item_e, item_f])
    yuri = Vendor()
    georg = Vendor()

    result_both_empty = yuri.swap_by_newest(georg)
    result_first_empty = georg.swap_by_newest(john)
    result_second_empty = mary.swap_by_newest(yuri)

    assert result_both_empty == False
    assert result_first_empty == False
    assert result_second_empty == False

def test_swap_by_newest_with_tie():
    item_a = Clothing(age=10)
    item_b = Decor(age=5)
    item_c = Clothing(age=5)
    item_d = Electronics(age=7)
    item_e = Decor(age=8)
    item_f = Decor(age=10)

    john = Vendor(inventory=[item_a, item_b, item_c])
    mary = Vendor(inventory=[item_d, item_e, item_f])

    result = john.swap_by_newest(mary)

    assert result
    assert min(mary.inventory, key=lambda item: item.age).age == 5

#@pytest.mark.skip
def test_get_items_by_category():
    item_a = Clothing()
    item_b = Electronics()
    item_c = Clothing()
    item_d = Decor()
    item_e = Item()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    items = vendor.get_by_category("Clothing")

    assert len(items) == 2
    assert item_a in items
    assert item_c in items

#@pytest.mark.skip
def test_get_no_matching_items_by_category():
    item_a = Clothing()
    item_b = Item()
    item_c = Decor()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("Electronics")

    assert len(items) == 0

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************

#@pytest.mark.skip
def test_best_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

#@pytest.mark.skip
def test_best_by_category_no_matches_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Electronics")

    assert best_item is None

#@pytest.mark.skip
def test_best_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_best_by_category("Clothing")

    # Assert
    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

#@pytest.mark.skip
def test_swap_best_by_category():
    # Arrange
    # me
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    #Assert
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3

    assert item_f in tai.inventory
    assert item_c not in tai.inventory
    assert item_c in jesse.inventory
    assert item_f not in jesse.inventory

    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other

#@pytest.mark.skip
def test_swap_best_by_category_reordered():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    #Assert
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3

    assert item_f in tai.inventory
    assert item_c not in tai.inventory
    assert item_c in jesse.inventory
    assert item_f not in jesse.inventory

    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there

#@pytest.mark.skip
def test_swap_best_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

#pytest.mark.skip
def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

#@pytest.mark.skip
def test_swap_best_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3

    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories

#@pytest.mark.skip
def test_swap_best_by_category_no_other_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    #Assert
    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3

    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories
