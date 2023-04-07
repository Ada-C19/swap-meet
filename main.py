from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

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

print(result)