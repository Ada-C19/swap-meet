from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric = "Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
        
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."



#     - This attribute describes what fabric the clothing is made from; 
#     some example values might be `"Striped"`, `"Cotton"`, or `"Floral"`
#     - When we instantiate an instance of `Clothing`, 

#     we can optionally pass in a string with the keyword argument `fabric`


#   - Has a stringify method that returns `"An object of type
# Clothing with id <id value>. It is made from <fabric value> fabric."`
#     - For example, if we had a `Clothing` instance with an `id` of `123435` 
#     and a `fabric` attribute that holds `"Wool"`, its stringify method should
#     return `"An object of type Clothing with id 12345. It is made from Wool fabric."`

    # def __str__(self):
        # return f"An object of type {self.__class__.__name__} with id {self.id}."
        # f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."


        # def __init__(self, id=None, fabric="Unknown",) 
        # self.fabric = fabric

    # def get_category(self):
    #     return "Clothing"
    
    # def stringify(self):
    #     return f"An object of type {self.id}. It is made from {self.fabric} fabric."

