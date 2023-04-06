import uuid
class Item:

    def __init__(self, id=None, condition= 0.0): # initializing constructor 
        self.id = id if id is not None else int(uuid.uuid4()) # creating an id attribute, getting random ID
        self.condition = condition # setting a condition attribute, a float

    def get_category(self):
        return f"{self.__class__.__name__}" #returning a string to name each class. 
    
    def __str__(self):
        return f"An object of type Item with id {self.id}." #setting a string to convey the items ID
    
    def condition_description(self): # setting the condition data structure. 
        
        condition_dict = {
            0: "Horrible",
            1: "Damaged",
            2: "Average",
            3: "Good",
            4: "Great",
            5: "Mint"
        }

        return condition_dict[self.condition]

    
    