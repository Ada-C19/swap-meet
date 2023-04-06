import uuid
class Item:
    def __init__(self, id = None, condition = 0):
        # If no id is provided, generate a unique id using the uuid package
        if id is None:
            self.id = uuid.uuid4().int
        # Otherwise, use the provided id
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        # Return the name of the class
        return  self.__class__.__name__


    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
        str: A string containing information about the object type and id.
        """
        # Use the __class__.__name__ method to get the class name and concatenate with the id
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Destroyed beyond repair. Don't even try."
        elif self.condition == 1:
            return "Well-loved. It's been around the block a few times."
        elif self.condition == 2:
            return "It's seen some use, but it's still got some life left."
        elif self.condition == 3:
            return "In good condition. A solid choice."
        elif self.condition == 4:
            return "Excellent condition. Like new, but not quite."
        elif self.condition == 5:
            return "Mint condition. You won't find one better."
