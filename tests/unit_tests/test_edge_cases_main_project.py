import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


'''Additional edge test cases for main project: '''

#@pytest.mark.skip
def test_item_id_incorrect_parameter_passed_raises_ValueError():
    with pytest.raises(ValueError):
        item = Item(id='obviously not an ID')
        
#@pytest.mark.skip
def test_item_condition_incorrect_parameter_passed_raises_ValueError():
    with pytest.raises(TypeError):
        item = Item(condition=['0'])

#@pytest.mark.skip
def test_item_condition_raises_ValueError_if_condition_below_0():
    with pytest.raises(ValueError):
        item = Item(condition=-1)
        
#@pytest.mark.skip        
def test_item_condition_raises_ValueError_if_condition_above_5():
    with pytest.raises(ValueError):
        item = Item(condition=6)
        
#@pytest.mark.skip       
def test_clothing_fabric_incorrect_parameter_passed_raises_ValueError():
    with pytest.raises(ValueError):
        item = Clothing(fabric=5)      
        
#@pytest.mark.skip       
def test_electronics_type_incorrect_parameter_passed_raises_ValueError():
    with pytest.raises(ValueError):
        item = Electronics(type=56697)
        
#@pytest.mark.skip       
def test_decor_width_incorrect_parameter_passed_raises_ValueError():
    with pytest.raises(ValueError):
        item = Decor(width='tree')

#@pytest.mark.skip
def test_decor_width_raises_ValueError_if_condition_below_0():
    with pytest.raises(ValueError):
        item = Decor(width=-1)

#@pytest.mark.skip       
def test_decor_length_incorrect_parameter_passed_raises_ValueError():
    with pytest.raises(ValueError):
        item = Decor(length='not an int')

#@pytest.mark.skip
def test_decor_length_raises_ValueError_if_condition_below_0():
    with pytest.raises(ValueError):
        item = Decor(length=-10000)