import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

'''Tests for Optional Part: '''

'''item.py add_ons'''

#@pytest.mark.skip
def test_item_year_incorrect_parameter_passed_raises_ValueError():
    with pytest.raises(ValueError):
        item = Item(year='year')
        
#@pytest.mark.skip        
def test_int_valued_optional_parameters_accept_string_convertable_to_int():
    item = Item(year='2014')
    
    assert isinstance(item.year, int)
    assert item.year == 2014

#@pytest.mark.skip
def test_item_year_default_is_none():
    item = Item()
    
    assert item.year is None
    
#@pytest.mark.skip
def test_item_use_custom_year_if_passed():
    item = Item(1989)
    
    assert item.year == 1989
    
#@pytest.mark.skip
def test_item_instances_have_different_year_if_passed():
    item1 = Item(1968)
    item2 = Item(2017)
    
    assert item1.year == 1968
    assert item2.year == 2017
    
#@pytest.mark.skip
def test_item_subclass_instances_have_different_year_if_passed():
    toaster = Electronics(2021)
    hoodie = Clothing(2023)
    
    assert toaster.year == 2021
    assert hoodie.year == 2023
    
#@pytest.mark.skip   
def test_calculate_age_with_incorrect_arguments_raises_valueerror():
    item = Item()
    
    with pytest.raises(TypeError):
        item.calculate_age('unknown argument')
        
#@pytest.mark.skip         
def test_calculate_age_returns_how_many_years_ago_from_today_item_was_created():
    '''WARNING: Its date sensitive!!! 
    Before testing make sure to change the value of 'current_year' for the actual current year.'''
    current_year = 2023 
    item = Item(year=2013)
    # (current_year - item.year (2023-2013) = 10)
    expected = 10
    
    actual = item.calculate_age()
    
    assert actual == expected
    assert isinstance(actual, int)
    
#@pytest.mark.skip     
def test_calculate_age_returns_false_if_no_year_is_given():
    item = Item()
    
    actual = item.calculate_age()
    
    assert actual is False
    

'''vendor.py add_ons'''

#@pytest.mark.skip 
def test_get_by_newest_returns_youngest_item_from_non_empty_inventory():
    item_a = Item(year=2018)
    item_b = Item(year=2006)
    item_c = Item(year=1978)
    inventory = [item_a, item_b, item_c]
    
    vendor = Vendor(inventory)
    expected = item_a
    
    actual = vendor.get_by_newest()
    
    assert actual is item_a

#@pytest.mark.skip     
def test_get_by_newest_returns_false_if_empty_inventory():
    inventory = []
    vendor = Vendor(inventory)
    
    actual = vendor.get_by_newest()
    
    assert actual is False
    
#@pytest.mark.skip     
def test_get_by_newest_returns_false_if_year_has_default_value():
    item_a = Item(year=2018)
    item_b = Item()
    item_c = Item(year=1978)
    inventory = [item_a, item_b, item_c]
    vendor = Vendor(inventory)
    
    actual = vendor.get_by_newest()
    
    assert actual is False
    assert len(inventory) == len(vendor.inventory)

#@pytest.mark.skip    
def test_swap_by_newest_swaps_self_newest_item_and_others_newest_item_succesfully():
    item_a = Item(year=2018)
    item_b = Item(year=2006)
    item_c = Item(year=1978)
    inventory = [item_a, item_b, item_c]
    us = Vendor(inventory)
    
    item_x = Item(year=2003)
    item_y = Item(year=2017)
    item_z = Item(year=1953)
    other_inventory = [item_x, item_y, item_z]
    other_vendor = Vendor(other_inventory)
    
    our_expected_inventory = [item_b, item_c, item_y]
    their_expected_inventory = [item_x, item_z, item_a]
    
    us.swap_by_newest(other_vendor)
    
    assert len(us.inventory) == 3
    assert len(other_vendor.inventory) == 3
    assert item_a not in us.inventory
    assert item_y not in other_vendor.inventory
    assert us.inventory == our_expected_inventory
    assert other_vendor.inventory == their_expected_inventory
    
#@pytest.mark.skip
def test_swap_by_newest_returns_false_if_ones_inventory_is_empty():
    item_a = Item(year=2018)
    item_b = Item(year=2006)
    item_c = Item(year=1978)
    inventory = [item_a, item_b, item_c]
    us = Vendor(inventory)
    
    other_inventory = []
    other_vendor = Vendor(other_inventory)
    
    result = us.swap_by_newest(other_vendor)
    
    assert len(us.inventory) == 3
    assert len(other_vendor.inventory) == 0
    assert us.inventory == inventory
    assert other_vendor.inventory == []
    assert not result

#@pytest.mark.skip    
def test_swap_by_newest_returns_false_if_year_attribute_has_default_value():
    item_a = Item(year=2018)
    item_b = Item(year=2006)
    item_c = Item(year=1978)
    inventory = [item_a, item_b, item_c]
    us = Vendor(inventory)
    
    item_x = Item(year=2003)
    item_y = Item()
    item_z = Item(year=1953)
    other_inventory = [item_x, item_y, item_z]
    other_vendor = Vendor(other_inventory)
    
    result = us.swap_by_newest(other_vendor)
    
    assert len(us.inventory) == 3
    assert len(other_vendor.inventory) == 3
    assert us.inventory == inventory
    assert other_vendor.inventory == other_inventory
    assert not result