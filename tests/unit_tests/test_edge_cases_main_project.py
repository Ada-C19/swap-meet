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
        
#@pytest.mark.skip       
def test_int_valued_optional_parameters_accept_string_convertable_to_int():
    item_a = Item(id='5289045', condition='3.2')
    item_b = Decor(width='9', length='0')
    assert isinstance(item_a.id, int)
    assert isinstance(item_a.condition, float)
    assert isinstance(item_b.width, int)
    assert isinstance(item_b.length, int)
    assert item_a.id == 5289045
    assert item_a.condition == 3.2
    assert item_b.width == 9
    assert item_b.length == 0

#@pytest.mark.skip
def test_contition_description_functions_if_float_condition_is_passed():
    item = Item(condition=3)
    expected_description_for_int = print('3.5 green bottles\n' 
                    'Hanging on the wall\n'
                    '3.5 green bottles\n'
                    'Hanging on the wall\n'
                    'And if one green bottle\n'
                    'Should accidentally fall\n'
                    'There will be 2.5 green bottles\n'
                    'Hanging on the wall.')

    assert isinstance(item.condition, int)
    assert print(item.condition_description()) == expected_description_for_int
    
#@pytest.mark.skip
def test_contition_description_functions_if_float_condition_is_passed():
    item = Item(condition=3.5)
    expected_description_for_float = print('3.5 green bottles\n' 
                    'Hanging on the wall\n'
                    '3.5 green bottles\n'
                    'Hanging on the wall\n'
                    'And if one green bottle\n'
                    'Should accidentally fall\n'
                    'There will be 2.5 green bottles\n'
                    'Hanging on the wall.')

    assert isinstance(item.condition, float)
    assert print(item.condition_description()) == expected_description_for_float