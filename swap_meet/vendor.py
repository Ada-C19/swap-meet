# from swap_meet.item import Item 

####################### WAVE 1 #############################

class Vendor:
    # inventory is an empty list
    def __init__(self, inventory=None):

        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        if item:
            self.inventory.append(item)
            return item
        
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
            # return self.inventory


####################### WAVE 2 #############################
    def get_by_id(self, id): 

        for item in self.inventory:
            if id == item.id:
                return item
        
        return None
    

################### WAVE 3 ########################
    def swap_items(self, other_vendor, my_item, their_item):

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True 
    
################### WAVE 4 #############################

    def swap_first_item(self, other_vendor):

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        
################ WAVE 6 #################

    def get_by_category(self, category):

        list_of_inventory_with_that_category = []

        for item in self.inventory:
            if category == item.get_category():
                list_of_inventory_with_that_category.append(item)
                
        return list_of_inventory_with_that_category



        # if category not in self.inventory:
        #     return list_of_inventory_with_that_category
        
        # if category in self.inventory:
        #     list_of_inventory_with_that_category.append(category)
        #     return list_of_inventory_with_that_category


        # list_of_inventory_with_that_category = []

        # if self.inventory not in category:
        #     return []

        # return list_of_inventory_with_that_category.append(category)
        # return [self.inventory[category]]




    def get_best_by_category(self, category):
        
        list_of_items_with_matching_category = self.get_by_category(category)


        if len(list_of_items_with_matching_category) == 0:
            return None

        best_condition = -1
        best_item = None
        for item in list_of_items_with_matching_category:
            if best_item == None or item.condition > best_condition:
                best_condition = item.condition
                best_item = item 

        return best_item 
        


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
    
        my_best_item = self.get_best_by_category(their_priority)

        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item == None or their_best_item == None:
            return False
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)


        

        

