
from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item 
    
    def get_by_id(self, id):
        for items in self.inventory:
            if items.id == id:
                return items
        return None
        

    def swap_items(self, other_vendor, my_item ,their_item):
        if my_item in self.inventory:
            if their_item in other_vendor.inventory:
                other_vendor.inventory.append(my_item)
                self.inventory.remove(my_item)
                self.inventory.append(their_item)
                other_vendor.inventory.remove(their_item)
            else:
                return None 
        else: 
            return None
        
        return other_vendor.inventory and self.inventory
    
    def swap_first_item(self, other_vendor):
        if other_vendor.inventory ==[] or self.inventory ==[]:
            return False
        else:
            my_first = self.inventory[0] 
            other_first = other_vendor.inventory[0]

            other_vendor.inventory.append(my_first)
            self.inventory.append(other_first)
            
            other_vendor.remove(other_first)
            self.inventory.remove(my_first)
            
            return self.inventory and other_vendor.inventory
        
    def get_by_category(self, category):
        #try:
            return [item for item in self.inventory if item.category==category]
        #except: 
            
    #    for item in self.inventory:
    #        if item.category == category: 
    #           
    #             return item 
        # variable = self.get_by_category(category)
        #max(variable, key= lambda item: item.condition)
    def get_best_by_category(self, category):
        invent_category = self.get_by_category(category)
        if not invent_category:
            return None
        result= max(invent_category, key= lambda item: item.condition)
        return result
        
            

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        mine= self.get_best_by_category(their_priority)
        theirs = other_vendor.get_best_by_category(my_priority)
        #if not other_vendor.inventory or self.inventory:
            #return False
        if not mine or not theirs:
            return False 
        try:
            for item in mine: 
                if item.category not in their_priority:
                    return False
            for item in theirs:
                if item.category not in my_priority:
                    return False
        except:
            self.swap_items(other_vendor, mine, theirs) 
            return self.inventory and other_vendor.inventory
    
            # if their_priority not in self.inventory:
            #     return False
            # elif my_priority not in other_vendor.inventory:
            #     return False


    #