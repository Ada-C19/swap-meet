from swap_meet.vendor import Vendor
from swap_meet.item import Item

import uuid


vendor = Vendor()
# print(len(vendor.inventory))

# print(vendor.add("chair"))

# # ["a","b","c"]

chair = Item(id)
print("id", uuid.uuid4().int)
# print(chair)
# # print(item.get_category("chair"))
# # print(type(item.get_category("chair")))
# print(vendor.get_by_id(id = 123))
# print(vendor.inventory)

vendor.inventory.append(chair)
for item in vendor.inventory:
    # print(type(item))
    print(item)
    print(vars(item))
