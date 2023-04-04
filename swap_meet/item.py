import uuid
class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

#--- Wave 2 ----------------------------
    def get_category(self):
        """return a string holding the name of the class"""
        return self.__class__.__name__

# --- Wave 3 ----------------------------
    def __str__(self):
        my_string = f'{self.id}'
        return f"An object of type {self.get_category()} with id {my_string}."
#--- Wave 5 -----------------------------
    def condition_description(self):
        if self.condition <= 1:
            return 'very used'
        elif self.condition >= 1 and self.condition < 2:
            return 'some used'
        elif self. condition >= 2 and self.condition < 3:
            return 'good'
        elif self. condition >= 3 and self.condition < 4:
            return 'very good'
        elif self. condition >= 4 and self.condition <= 5:
            return 'This is a treassure'
    
    
    