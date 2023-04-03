from swap_meet.vendor import Vendor

vendor = Vendor()
print(len(vendor.inventory))

print(vendor.add("chair"))

# ["a","b","c"]