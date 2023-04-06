
class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
    
    def add(self,element):
        self.inventory.append(element)
        return element
    
    def get_by_id(self, id):
        for element in self.inventory:
            if id == element.id:
                return element
        return None
    
    def swap_items(self, other_vendor, my_item, their_item,):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        return False
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.inventory.append(other_vendor.inventory[0])
        other_vendor.inventory.append(self.inventory[0])
        self.inventory.pop(0)
        other_vendor.inventory.pop(0)
        return True
        # swap_item() can be used here if we pass self.inventory[0] and other_vendor.inventor[0]
        # however this has more time complexity because of remove() vs pop()
        # the overall time complexity would probably be O(n) anyway because of "in" 
        # so maybe it is worth it to use swap_item() 
        # could also refactor swap_items using range(len()) to iterate indexes so that
        # pop could be used in both scenarios. is this over optimization lol 
    
    def get_by_category(self, category):
        list_of_category = []
        for element in self.inventory:
            if element.get_category() == category:
                list_of_category.append(element)
        return list_of_category

    def get_best_by_category(self, category):
        best_condition = 0
        best_item = None
        items_to_search = self.get_by_category(category)
        for element in items_to_search:
            if element.condition > best_condition:
                best_item = element
                best_condition = element.condition
        return best_item
    #dry-er : lambdas**

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item_in_the_category_they_want  = self.get_best_by_category(their_priority)
        their_best_item_in_the_category_I_want = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, 
                                my_best_item_in_the_category_they_want, 
                                their_best_item_in_the_category_I_want)

        


