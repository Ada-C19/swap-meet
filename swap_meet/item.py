import uuid
# from swap_meet.vendor import Vendor

class Item:
    def __init__(self, id = None, condition = 0):
        if id != None:
            self.id = id
        else:
            self.id = uuid.uuid4().int
        self.condition = condition

    
    def get_category(self):
        class_name = "Item"
        # class_name = __class__.__name__
        return class_name
    
    def __str__(self):
        item_id = self.id
        return f"An object of type Item with id {item_id}."
    
    def condition_description(self):
        condition_dict = {
            0 : "This sucks real bad",
            1: "smelly",
            2: "stinky",
            3 : "this is pretty mid",
            4 : "heyo this pretty cool",
            5 : "THIS IS AMAZING YES"
        }
        return condition_dict[self.condition]
        
        

    
    




        
    
    


    
