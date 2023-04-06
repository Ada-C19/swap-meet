
class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
         #why dont we import^^^? is it becuase it's not an instance method...

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        first_item_self = self.inventory[0]
        first_item_other = other_vendor.inventory[0]

        self.swap_items(other_vendor, first_item_self, first_item_other)

        return True
    
    def get_by_category(self, string_category):
        category_list = []
        # print(self.inventory)
        # for thing in self.inventory:

            # print("self.inventory", thing.self.inventory.get_category)
        for thing in self.inventory:
            # print(thing)
            if thing.get_category() == string_category:
                category_list.append(thing)
        # print("categorlist", category_list)
        return category_list
    
    def get_best_by_category(self, string_category):
        highest_condition = 0
        highest_condition_category = ''
        index = 0

        list_of_category = self.get_by_category(string_category)

        while index < len(list_of_category):
            

        # for category in list_of_category:
        #     highest_condition = category[0] 
        #     if highest_condition < category.condition:
        #         highest_condition = category.condition
        #         highest_condition_category = category
        # # print(highest_condition)
    

