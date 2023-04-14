import uuid
class Item:
    def __init__(self, id = None, condition = 0, age = 0):
        # If no id is provided, generate a unique id using the uuid package 
        # Instead of using uuid package to generate unique ids for Item instances,
        #  I could use the built-in id function to generate unique ids based on the object's memory address. 
        # This can simplify the code and avoid the dependency on an external package.
        if id is None:
            self.id = uuid.uuid4().int  # could be if use built-in function self.id = id(self) 
        elif not isinstance(id, int):
            raise ValueError("id must be an integer")
        # Otherwise, use the provided id
        else:
            self.id = id
        # Check that condition is within valid range (0-5)
        if not 0 <= condition <= 5:
            raise ValueError("condition must be between 0 and 5")
        self.condition = condition
        
        # Check that age is a non-negative integer
        if not isinstance(age, int) or age < 0:
            raise ValueError("age must be a non-negative integer")
        self.age = age
        

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
        descriptions = {
            0: "Destroyed beyond repair. Don't even try.",
            1: "Well-loved. It's been around the block a few times.",
            2: "It's seen some use, but it's still got some life left.",
            3: "In good condition. A solid choice.",
            4: "Excellent condition. Like new, but not quite.",
            5: "Mint condition. You won't find one better."
        }
        try:
            return descriptions.get(round(self.condition))
        except KeyError:
            return "Seriously?!!! is this a condition oo--oo???!!!"