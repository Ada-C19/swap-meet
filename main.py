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

clothing = Clothing()
item = Item()

other_vendor = Vendor([clothing, item])
# print(vendor.swap_first_item(other_vendor))



# print(clothing.get_category())
# print(clothing)
# print(other_vendor.inventory)
print(other_vendor.get_by_category("Clothing"))
