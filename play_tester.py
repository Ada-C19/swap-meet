from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


item_a = Clothing()
item_b = Electronics()
item_c = Clothing()
item_d = Decor()
item_e = Item()
vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

test= Vendor()
C = test.get_by_category("Clothing")
# print(C)





# test_id = 12345
# Item(id=test_id)
# item_custom_id = Item(id=test_id)
# my_instance = Vendor([Item(), Item(), item_custom_id])
# my_instance.get_by_id(12345)
# my_instance = Item()
# my_instance

# test_id = 12345
# Item(id=test_id)
# item_custom_id = Item(id=test_id)
# vendor = Vendor(
#     inventory=[Item(), Item(), item_custom_id]
# )
# print(inventory)
