class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        try:
            for i in range(len(self.inventory)):
                if self.inventory[i].id == id:
                    return self.inventory[i]
        except:
            return None

    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.remove(my_item)
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False   

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return True
    
    def get_by_category(self, category):
        category_list = []
        for element in self.inventory:
            if element.get_category() == category:
                category_list.append(element)
        
        return category_list

    def get_best_by_category(self, category):
        best_condition = 0
        best_item = None
        for element in self.inventory:
            if element.get_category() == category and element.condition > best_condition:
                best_item = element
                best_condition = element.condition
        return best_item
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if other_vendor.get_best_by_category(my_priority) == None or self.get_best_by_category(their_priority) == None:
            return False

        i_want = other_vendor.get_best_by_category(my_priority)
        they_want = self.get_best_by_category(their_priority)

        self.swap_items(other_vendor, they_want, i_want)
        return True

    def swap_by_newest(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        my_newest = None
        their_newest = None
        my_min_age = 500
        for item in self.inventory:
            if item.age < my_min_age:
                my_min_age = item.age
                my_newest = item
        their_min_age = 500
        for item in other_vendor.inventory:
            if item.age < their_min_age:
                their_min_age = item.age
                their_newest = item 
        self.swap_items(other_vendor, my_newest, their_newest)
        return True
