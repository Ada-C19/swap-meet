from swap_meet.vendor import Vendor
from swap_meet.item import Item

# vendor = Vendor()
# print(len(vendor.inventory))

# print(vendor.add("chair"))

# # ["a","b","c"]

item = Item(300)
print(item.get_category("chair"))