import uuid

class Item:
    def __init__(self, id=None, condition=0.0, age=0.0):
        if not id:
            id = int(uuid.uuid4())
        self.id = id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return ('An object of type ' + self.__class__.__name__ +
                ' with id ' + str(self.id) + '.')
    
    def condition_description(self):
        if self.condition <= 1:
            return 'almost in tatters'
        elif self.condition <= 2:
            return 'ragged but useable'
        elif self.condition <= 3:
            return 'fair'
        elif self.condition <= 4:
            return 'good used condition'
        elif self.condition < 5:
            return 'excellent used condition'
        elif self.condition == 5:
            return 'mint new condition'
    
    def age_description(self):
        if self.age == 0.0:
            return 'brand new'
        elif self.age < 1:
            return 'less than 1 year old'
        elif self.age < 5:
            return 'less than 5 years old'
        else:
            return 'over 5 years old'


