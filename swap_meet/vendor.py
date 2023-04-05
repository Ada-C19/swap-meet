from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def get_by_id(self,id):
        for items in self.inventory:
            if items.id == id:
                return items
        return None
    
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False 

        my_first_item = self.inventory[0]
        friends_first_item = other_vendor.inventory[0]
        self.remove(my_first_item)
        self.add(friends_first_item)
        other_vendor.remove(friends_first_item)
        other_vendor.add(my_first_item)
        return True

    def get_by_category(self, category=None):
        self.category = None if category is None else category
        category_list = []
        for item in self.inventory:
            if item not in self.inventory:
                return category_list
            else:
                if item.get_category() == self.category:
                    category_list.append(item)
            
        return category_list
    
    def get_best_by_category(self, category=None):
        self.category = None if category is None else category
        highest_condition = 0
        best_item = None
        
        for item in self.inventory:
            if item.get_category() == self.category and item.condition >= highest_condition:
                highest_condition = item.condition
                best_item = item

        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        if my_best_item == None:
            return False
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if their_best_item == None:
            return False
        return self.swap_items(other_vendor, my_best_item, their_best_item)
        


        
        
        
        
        
        
        
        # category_list = self.get_by_category(category)
        # value = []

        # for item in category_list:
        #     value.append(item.condition)
        
        # max_value = max(value)

        # for item in category_list:
        #     if item.condition == max_value:
        #         return item




            # if item not in self.inventory:
            #     return None
            # else:
            #     if item.condition_description() == max_value and item.get_category() == self.category:
            #   return item