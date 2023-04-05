import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        if id is  None:
            self.id =  uuid.uuid4().int 
        else:
            self.id = id 
        
        if isinstance(condition, (int, float)):
            if 0 <= condition <= 5:
                self.condition = condition 
            else:
                raise ValueError("Condition must be between 0 and 5")
        else: 
            raise TypeError("Condition must be a number")

    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        if self.condition == 5:
            return "Best condition"
        elif self.condition > 4:
            return "Great condition"
        elif self.condition > 3:
            return "Good condition"
        elif self.condition > 2:
            return "Fair condition"
        elif self.condition > 1:
            return "Poor condition"
        else:
            return "Bad Condition"    