class Vendor:

    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        else:
            return None
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0] 
        their_first_item = other_vendor.inventory[0]
        self.add(their_first_item)
        other_vendor.add(my_first_item)
        self.remove(my_first_item)
        other_vendor.remove(their_first_item)
        return True

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list
    
    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)

        if not category_list:
            return None
        else:
            highest_rated = category_list[0]
            for item in category_list:
                if item.condition > highest_rated.condition:
                    highest_rated = item
            return highest_rated
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = self.get_best_by_category(my_priority) 
        if my_best_item and their_best_item:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True
        else:
            return False


