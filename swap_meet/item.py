import uuid


class Item:
    def __init__(self, id=None, condition=0, age=0):
        if id is None:
            id = uuid.uuid4().int
        elif not isinstance(id, int):
            raise ValueError("id must be an integer")
        self.id = id
        self.condition = condition
        self.age = age

    def get_category(self):
        """This function returns the category of the item"""
        return "Item"

    def __str__(self):
        """This function a string with the object type and id"""
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        """This function returns a string depending on the condition of the item"""
        if isinstance(self.condition, int) or isinstance(self.condition, float):
            if self.condition == 0:
                return "Wear a hazmat suit for pickup"
            elif self.condition == 1:
                return "Ask your Mom to come pick you up, you will be scared"
            elif self.condition == 2:
                return "This just needs some tender-lovin' care"
            elif self.condition == 3:
                return "Meh, it's okay, might need a wash"
            elif self.condition == 4:
                return "Good find, just one or two problems with this one"
            elif self.condition == 5:
                return "Perfect condition! Someone probably accidently gave this away, but I guess you got lucky"
            else:
                return "Condition must be between range 1-5"
        else:
            print("Condition must be numerical")
