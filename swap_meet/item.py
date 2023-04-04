import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        if not id:
            id=int(uuid.uuid4())
        self.id = id 
        self.condition=condition
    

    def get_category(self):
        return (f"{self.__class__.__name__}")
    
    
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}.")

    def condition_description(self):

        if self.condition==0:
            return "Trash"
        if self.condition==1:
            return "Has lived"
        if self.condition==2:
            return "Trashy but classic"
        if self.condition==3:
            return "Above Average"
        if self.condition==4:
            return "Almost New"
        return "Like New"
        
