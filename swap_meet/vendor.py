class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, item_id):
        self.item_id = item_id
        for item in self.inventory:
            if self.item_id == item.id:
                return item
        else:
            return None

    def swap_items(self, other_vendor, my_item, their_item):
        if self.inventory == [] or other_vendor.inventory == []:
            return False

        if their_item not in other_vendor.inventory:
            return False

        if my_item not in self.inventory:
            return False

        other_vendor.add(my_item)
        self.add(their_item)

        self.remove(my_item)
        other_vendor.remove(their_item)

        return True
