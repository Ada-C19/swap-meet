from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory =inventory
    #     self.inventory = inventory
    #     word_list = [] if word_list is None else word_list
    # word_list.append(word)
    
    def add(self, item):
        self.inventory.append(item)
        return  item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, id):
        if id in self.inventory:
            return id 
        else:
            return None
        
        