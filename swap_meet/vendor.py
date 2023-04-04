class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory


    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item


    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        return False
    

