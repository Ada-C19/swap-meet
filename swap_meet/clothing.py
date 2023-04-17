from swap_meet.item import Item

class Clothing(Item):
    # May have to change fabric default values to None
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        if fabric == None:
            self.fabric = "Unknown"
        else:
            self.fabric = fabric
            
    def clothing(self):
            self.clothing = self.fabric 

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."    

        # if self.fabric == "unknown":
            # return f"An object of type {self.get_category()} with id {self.id}. It is made from Unknown fabric."    
        # else:
        #     return f"An object of type {self.clothing()} with id {self.id}. It is made from {self.fabric} fabric."    
    
    def condition_description(self):
        if self.condition == 0:
            return f"Item condition is rated 0. This item is barely holding on!"
        elif self.condition == 1:
            return f"Items condition is rated 1. This item is hanging on by a thread!"
        elif self.condition == 2:
            return f"Items condition is rated 2. This item is living on a prayer."
        elif self.condition == 3:
            return f"Items condition is rated 3. This item is in working order."
        elif self.condition == 4:
            return f"Items condition is rated 4. This item is in good condition."
        else:
            return f"Items condition is rated 5. This item is in excellent condition."