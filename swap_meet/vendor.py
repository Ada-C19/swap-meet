class Vendor:

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory else []

    def add(self, item = 'new item'):
        self.inventory.append(item)
        return item
    
    def remove(self, item = 'item to remove'):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        
    def get_by_id(self, id = int):
        for item in self.inventory:
            if item.id == id:
                return item
            
    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        
        else:
            other_vendor.remove(their_item)
            self.add(their_item)
            self.remove(my_item)
            other_vendor.add(my_item)
            
            return True

    def swap_first_item(self,other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        
        return True
    
    def get_by_category(self, category = None):
        if category == None:
            return []
        
        category_list = [item for item in self.inventory if item.get_category() == category]
        
        return category_list

    def get_best_by_category(self, category):
        condition_value_dict = {}

        if self.get_by_category(category):
            for item in self.get_by_category(category):
                condition_value_dict[item] = item.condition
            
            best_item = max(condition_value_dict, key = condition_value_dict.get)
            
            return best_item
        
        else:
            return None
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if self.get_best_by_category(their_priority) and other_vendor.get_best_by_category(my_priority):
            self.swap_items(other_vendor, self.get_best_by_category(their_priority), other_vendor.get_best_by_category(my_priority))
            return True
        
        return False

    def get_newest_item(self):
        age_dict = {}

        for item in self.inventory:
            age_dict[item] = item.age

        newest_item = min(age_dict, key = age_dict.get)

        return newest_item
        
    def swap_by_newest(self, other_vendor):
        return self.swap_items(other_vendor, self.get_newest_item(), other_vendor.get_newest_item())
