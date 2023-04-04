from swap_meet.vendor import Vendor
from swap_meet.item import Item


test_id = 12345
Item(id=test_id)
item_custom_id = Item(id=test_id)
my_instance = Vendor([Item(), Item(), item_custom_id])
my_instance.get_by_id(12345)
# my_instance = Item()
# my_instance

# test_id = 12345
# Item(id=test_id)
# item_custom_id = Item(id=test_id)
# vendor = Vendor(
#     inventory=[Item(), Item(), item_custom_id]
# )
# print(inventory)
