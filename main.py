from swap_meet.vendor import Vendor
from swap_meet.item import Item

item_a = Item()
item_b = Item()
item_c = Item()
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Item()
item_e = Item()
jolie = Vendor(
    inventory=[item_d, item_e]
)

print(fatimah.inventory)
result = fatimah.swap_first_item(jolie)
print(result)