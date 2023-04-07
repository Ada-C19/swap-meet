

class Vendor:
    #
    def __init__(self, inventory=None):
        # if inventory is truthy, values will be assigned to inventory
        if inventory:
            self.inventory = inventory
            # otherwise, []
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

# if theres a match, item gets removed
    def remove(self, item):

        if item in self.inventory:
            self.inventory.remove(item)
            return item

        else:
            return False

# chhecking if id matches any in the invetory
#
    def get_by_id(self, id):
        for each_item in self.inventory:
            if each_item.id == id:
                return each_item

        return None

    def swap_items(self, other_vendor, my_item, their_item):
        # if either of these are not found, returns False
        if my_item not in self.inventory:
            return False

        if their_item not in other_vendor.inventory:
            return False
# if found
# performs the swap
        self_item_idx = self.inventory.index(my_item)
        their_item_idx = other_vendor.inventory.index(their_item)
# using a temp variable to hold the value then swap values
        temp = self.inventory[self_item_idx]
        self.inventory[self_item_idx] = their_item
        other_vendor.inventory[their_item_idx] = temp

        return True

    def swap_first_item(self, other_vendor):

        # check if any is empty
        if self.inventory == []:
            return False

        if other_vendor.inventory == []:
            return False
# swap the first items
        self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory[0]

        return True

# loops through the inventory to sotre items in the list
    def get_by_category(self, category):

        category_list = []
        for each_item in self.inventory:
            if each_item.get_category() == category:
                category_list.append(each_item)
        return category_list

    def get_best_by_category(self, category):

        items = self.get_by_category(category)

        best_item = items[0]
        for item in items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
