from swap_meet.item import Item

class Clothing(Item):
    # May have to change fabric default values to None
    def __init__(self, id, fabric="unknown"):
        super().__init__(id)
        if fabric == None:
            self.fabric = "unknown"

        else:
            self.fabric = fabric
            
    def clothing(self):
            self.clothing = self.fabric   

    def get_category(self):
        return self.clothing 
    
    def __str__(self):
        if self.fabric == "unknown":
            return f"An object of type {self.get_category()} with id {self.id}. It is made from Unknown fabric."    
        else:
            return f"An object of type {self.clothing()} with id {self.id}. It is made from {self.fabric} fabric."    

    def condition_description(self):
        pass