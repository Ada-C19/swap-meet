# from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        for n in self.inventory:
            if n == item:
                self.inventory.remove(item)
                return item
        return False

    # def get_by_id(self, id):
    #     for item in self.inventory:
    #         if item.id == id:
    #             return item
    #     return None
