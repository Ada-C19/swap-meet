from swap_meet.vendor import Vendor
from swap_meet.item import Item

vendor = Vendor(["chair", 123])
# print(len(vendor.inventory))

# print(vendor.add("chair"))

# # ["a","b","c"]

item = Item()
print(item.id)
# print(item.get_category("chair"))
# print(type(item.get_category("chair")))
print(vendor.get_by_id(id = 123))

