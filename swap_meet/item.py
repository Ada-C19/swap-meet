import uuid
class Item:
    
    def __init__(self, id=None): 
        # self.self = self
        
        if id is None:
            # Generate a random UUID
            random_uuid = uuid.uuid4()
            # Convert the UUID to an integer using its hex representation
            random_id = int(random_uuid.hex, 16)
            #Assign the integer id to self
            self.id = random_id
        else:
            self.id = id

        self.category = "Item"

    def get_category(self):
        return f"{self.category}"
    
    #Use dunder str to stringify the id
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "No condition description."
        elif self.condition == 1:
            return "This item is in poor condition."
        elif self.condition == 2:
            return "This item is in fair condition."
        elif self.condition == 3:
            return "This item is in good condition."
        elif self.condition == 4:
            return "This item is in excellent condition."
        else:
            return "This item is in like-new condition."

    




    