from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item_add):
        self.inventory.append(item_add)
        return item_add
    
    def remove(self, item_remove):
        if item_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_remove)
            return item_remove
        
    def get_by_id(self, id):
        test_item = Item(id)
        for item in self.inventory:
            if item.id == test_item.id:
                return item
        return None

            
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else:
            user_first_item = self.inventory[0]
            friend_first_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, user_first_item, friend_first_item)
            # self.inventory.remove(user_first_item)
            # other_vendor.inventory.remove(friend_first_item)
            # other_vendor.inventory.append(user_first_item)
            # self.inventory.append(friend_first_item)
            return True
        
    def get_by_category(self, category):
        #category of type string
        resulting_list = []
        for item in self.inventory:
            if item.get_category() == category:
                resulting_list.append(item)
        return resulting_list
    
    def get_best_by_category(self, category):
        resulting_list = self.get_by_category(category)
        if len(resulting_list) == 0:
            return None
        else:
            best_item = resulting_list[0]
            best_condition = resulting_list[0].condition
            for item in resulting_list:
                if item.condition > best_condition:
                    best_item = item
                    best_condition = item.condition
            return best_item    
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        user_best_match = self.get_best_by_category(their_priority)
        other_best_match = other_vendor.get_best_by_category(my_priority)
        if user_best_match is None or other_best_match is None:
            return False
        else: 
            self.swap_items(other_vendor, user_best_match, other_best_match)
            return True