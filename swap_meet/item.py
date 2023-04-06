import uuid

class Item:
    def __init__(self, age=0, id=None, condition=0):
        
        if id: 
            self.id = id
        else:
            self.id = uuid.uuid4().int
        self.condition = condition
        #Added AGE
        if isinstance(age, int):
            self.age = age
        else:
            self.age = None

    
    def get_category(self):
        # Holds the class name and returns it as a str
        return self.__class__.__name__
    
    # This method will return the type this class as a Str not as an "An object of type Item with id <id value>."
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition > 0 and self.condition <= 2:
            return "Heavily used"
        elif self.condition >= 3 and self.condition <= 4:
            return "Used"
        else:
            return "Mint condition"
        
    

    


    