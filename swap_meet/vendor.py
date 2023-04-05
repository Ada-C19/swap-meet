class Vendor:
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory 
    
    def add(self,new_item):
        self.inventory.append(new_item)
        return new_item 
    
    def remove(self,item):
        try:
            self.inventory.remove(item)
            return item 
        except:
            return False
        
    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None 
    
    def swap_items(self,other_vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            self.inventory.append(their_item)
            other_vendor.inventory.remove(their_item)
            return True  
        
    def swap_first_item(self,other_vendor):
        if (not self.inventory) or (not other_vendor.inventory):
            return False
        my_item = self.inventory.pop(0)
        their_item = other_vendor.inventory.pop(0)
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        return True 
    
    def get_by_category(self,category):
        lst = []
        for item in self.inventory:
            if item.get_category() == category:
                lst.append(item)
        return lst 
    
    def get_best_by_category(self,category):
        category_lst = self.get_by_category(category)
        if category_lst == []:
            return None
        best_condition_item = category_lst[0]
        for item in category_lst:
            if item.condition > best_condition_item.condition:
                best_condition_item = item 
        return best_condition_item  
    
    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        
        if my_item and their_item:
            self.swap_items(other_vendor,my_item,their_item)
            return True
        return False 