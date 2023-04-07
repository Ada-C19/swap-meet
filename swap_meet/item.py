import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if not isinstance(id, int) and id is not None:
            raise TypeError("id needs to be integer")
        if not isinstance(condition, int) and not isinstance(condition, float):
            raise TypeError("condition needs to be integer")
        
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        
        self.condition = condition
        
#--- Wave 2 ----------------------------
    def get_category(self):
        """Return a string holding the name of the class"""
        return self.__class__.__name__

# --- Wave 3 ----------------------------
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
#--- Wave 5 -----------------------------
    def condition_description(self):
        """Return the condition in words based on the value"""
        if self.condition <= 1:
            return 'very used'
        elif self.condition <= 2:
            return 'some used'
        elif self.condition <= 3:
            return 'good'
        elif self.condition <= 4:
            return 'very good'
        else:
            return 'This is a treassure'
        

    