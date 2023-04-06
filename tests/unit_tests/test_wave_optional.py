import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_item_has_age():
    item_a = Item(0)
    item_b = Item(2)
    item_c = Item(3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    
    assert fatimah.inventory[0].age == 0
    assert fatimah.inventory[1].age == 2
    assert fatimah.inventory[2].age == 3
    

def test_swap_by_newest_returns_True():
    item_a = Item(0)
    item_b = Item(2)
    item_c = Item(3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(1)
    item_e = Item(2)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_a in jolie.inventory
    assert result

def test_swap_by_newest_different_categories():
    camila = Vendor()
    valentina = Vendor()

    item_clothing1 = Clothing(age=5, condition=1.0, id=123, fabric="Geometric Pattern")
    item_clothing2 = Clothing(age=3, condition=2.0, id=321)
    item_electronics1 = Electronics(age=1, condition=1.0, id=456)
    item_electronics2 = Electronics(age=0, condition=2.0, id=654, type="Kitchen Appliance")
    item_decor1 = Decor(age=3, condition=1.0, id=789)
    item_decor2 = Decor(age=0, condition=2.0, id=987, width=4, length=2)

    camila = Vendor(
        inventory=[item_clothing1, item_electronics1, item_electronics2]
    )
    valentina = Vendor(
        inventory=[item_clothing2, item_decor1, item_decor2]
    )
    result = camila.swap_by_newest(valentina)

    assert len(camila.inventory) == 3
    assert item_electronics2 not in camila.inventory
    assert item_electronics1 in camila.inventory
    assert item_clothing1 in camila.inventory
    assert item_decor2 in camila.inventory
    assert len(valentina.inventory) == 3
    assert item_decor2 not in valentina.inventory 
    assert item_electronics2 in valentina.inventory
    assert item_clothing2 in valentina.inventory
    assert item_decor1 in valentina.inventory
    assert result