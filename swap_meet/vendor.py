# from item import Item


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
        if self.item_id in self.inventory:
            return item_id
        else:
            return None
