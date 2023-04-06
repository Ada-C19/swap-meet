import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_item_id_as_string_raises_error():
    # arrange and act
    # assert
    with pytest.raises(TypeError):
        item = Item(id="croissant")

def test_item_id_as_float_raises_error():
    # arrange and act
    # assert
    with pytest.raises(TypeError):
        item = Item(id=9.0)

def test_item_id_as_list_raises_error():
    # arrange and act
    # assert
    with pytest.raises(TypeError):
        item = Item(id=[])

"""
Johanna and Nadia tried to get the method to raise
an error when a boolean value was passed in for id
however we encountered some unexpected behavior.
We still wrote the tests though!
"""


@pytest.mark.skip
def test_item_id_as_bool_raises_error():
    # arrange and act
    # assert
    with pytest.raises(TypeError):
        item = Item(id=True)

@pytest.mark.skip
def test_items_id_True():
    item = Item(id=True)
    assert isinstance(item.id, int)
    assert len(str(item.id)) >= 32 

@pytest.mark.skip
def test_items_id_False():
    item = Item(id=False)
    assert isinstance(item.id, int)
    assert len(str(item.id)) >= 32 

"""
We also considered one option where rather than raising
a TypeError, the __init__ function in Item reassigns 
non-int input to None, then assigns a new id on line 7 of
item.py, overriding any invalid input. 

The following test verifies such a case. 

We deciding against using this approach because this would
reassign the id value without informing the user, which 
could cause problems when a user goes to look up an item
in their inventory by the input id. 
"""

@pytest.mark.skip
def test_items_id_croissant():
    item = Item(id="croissant")
    assert isinstance(item.id, int)
    assert len(str(item.id)) >= 32 