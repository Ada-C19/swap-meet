from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing

import uuid


vendor = Vendor(["cake", "shirt", "water"])
# print(len(vendor.inventory))

# print(vendor.add("chair"))

# # ["a","b","c"]

# chair = Item(id)
# print("id", uuid.uuid4().int)
# # print(chair)
# # print(item.get_category("chair"))
# # print(type(item.get_category("chair")))
# print(vendor.get_by_id(id = 123))
# print(vendor.inventory)

clothing = Clothing(condition= 2.0)
item = Item(condition=4.0)
clothing2 = Clothing(condition=5.0)

other_vendor = Vendor([clothing, item,clothing2])
# print(vendor.swap_first_item(other_vendor))



# print(clothing.get_category())
# print(clothing)
# print(other_vendor.inventory)
# print(other_vendor.get_by_category("Clothing"))
print(other_vendor.get_best_by_category("Clothing"))
