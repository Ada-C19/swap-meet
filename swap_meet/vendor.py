# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None): 
        if inventory is None:
            inventory = []
        self.inventory = inventory
        self.name = "Vendor"
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False 
        
        self.inventory.remove(item)
        return item

    def get_by_id(self, current_id):
        # item_id = Item().id
        for item in self.inventory:
            if current_id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):

        if not self.inventory or not other_vendor.inventory:
            return False

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # assigning specific item index to variable
        my_item_index = self.inventory.index(my_item)
        their_item_index = other_vendor.inventory.index(their_item)

        # simultaneously pops specific item off list and appends it to another
        other_vendor.inventory.append(self.inventory.pop(my_item_index))
        self.inventory.append(other_vendor.inventory.pop(their_item_index))
        
        return True

    def swap_first_item(self, other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False

        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])


    def get_by_category(self, category):
        same_category_list = []

        for item in self.inventory:
            if category == item.get_category():
                same_category_list.append(item)

        return same_category_list
    
    def get_best_by_category(self, category):
        highest_score = 0
        highest_item = None
        for item in self.inventory:
            if item.condition >= highest_score and category == item.get_category():
                highest_score = item.condition
                highest_item = item
        
        return highest_item   
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
            return False
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, my_best_item, their_best_item)
        