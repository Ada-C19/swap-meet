import uuid

#from item import Item


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory #each vendor will have an attribute named :inventory (an empty list)
        
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
        print(item)
        return item 
    
    def remove(self, item): 
        
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            print(item.id)
            print(id)
            if item.id == id:
                return item
        return None
        

    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in other_vendor.inventory: 
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True 
    # these functions will return uuid objects **(not int)**  

    def swap_first_item(self, other_vendor):
        if other_vendor.inventory == [] or self.inventory == []:
            return False
        else:
            #look at the syntax here
            other_vendor.add(self.inventory[0])
            self.remove(self.inventory[0])
            self.add(other_vendor.inventory[0])
            other_vendor.remove(other_vendor.inventory[0])
            return True
    
    def get_by_category(self, category):
        objects = []

        for item in self.inventory:
            if item.get_category() == category:
                objects.append(item)
        return objects
    
    def get_best_by_category(self, category):
    
        items = self.get_by_category(category)
        if items == []:
            return None
        else:
            highest_condition = items[0]
            for item in items:
                if item.condition >= highest_condition.condition:
                    highest_condition = item
            return highest_condition
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)

        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item == None or their_best_item == None:
            return False
        else:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True
