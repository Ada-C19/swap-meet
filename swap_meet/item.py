import uuid

class Item:
    def __init__(self, age = 0.0 , id = None, condition = 0.0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
        self.age = age
            
    def __str__(self):
        return f'An object of type {self.__class__.__name__} with id {self.id}.'

    def get_category(self):
        return self.__class__.__name__
    
    def get_age(self):
        return self.age
    
    def condition_description(self):
        if self.condition >= 0.0 and self.condition < 1.0:
            return "Should you get this? IT DEPENDS! ʕ •ᴥ• ʔ"
        elif self.condition >= 1.0 and self.condition < 2.0:
            return "One person's garbage is another's treasure."
        elif self.condition >= 2.0 and self.condition < 3.0:
            return "If you squint, you can't even tell."
        elif self.condition >= 3.0 and self.condition < 4.0:
            return "This is a bargan for the price."
        elif self.condition >= 4.0 and self.condition < 5.0:
            return "This item has been well cared for, but you can tell you're not the first owner."
        elif self.condition >= 5.0:
            return "This item is immaculate. If you don't buy it, I will!"
        
    def age_description(self):
        if self.age >= 0.0 and self.age < 1.0:
            return "I've had this for less than a year!"
        elif self.age >= 1.0 and self.age < 2.0:
            return "I've had this for a little over a year!"
        elif self.age >= 2.0 and self.age < 3.0:
            return "I've had this for over two years but not more than three!" 
        elif self.age >= 3.0 and self.age < 4.0:
            return "I've had this for over three years but not more than four!" 
        elif self.age >= 4.0 and self.age < 5.0:
            return "I've had this for over four years but not more than five!" 
        elif self.age >= 5.0:
            return "I've had this for over five years!"
    