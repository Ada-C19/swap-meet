import uuid
class Item:
    """
    A class that represents item.
    Each Item have an attribute named id, which is a quique integer as default; an attribute named condition, which is an integer represent the item's condition, default value is 0 (the poorest).
    """
    def __init__(self, id=None, condition=0):
        # when manually set id, check if it's an integer, if not: raise TypeError.
        if id:
            if isinstance(id, int):
                self.id = id
            else:
                raise TypeError("Id must be an integer.")
        # when id is not provided, generate an id with integer.
        else:
            self.id = uuid.uuid4().int
        self.condition = condition
    
    def get_category(self):  
        """
        Return the class name as a string.
        """  
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        """
        Return funny description based on the item's condition.
        """
        if self.condition == 5:
            return "This item is in tip-top shape!"
        elif self.condition == 4:
            return "This item still has plenty of life left and character to spare."
        elif self.condition == 3:
            return "It's not down for the count - it's still got some fight left in it!"
        elif self.condition == 2:
            return "Don't judge this item by its appearence. It's still got some tricks up its sleeve and plenty of use left."
        elif self.condition == 1:
            return "This item may not have much life left in it, but it's not quite ready to give up the ghost yet."
        else:
            return "Oh... :'( This item has seen better days."