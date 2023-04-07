from swap_meet.item import Item

class Electronics(Item):
    
    # Wave 05
    def __init__(self, condition=0, id=0, type="Unknown"):
        super().__init__(category="Electronics",condition=condition,id=id)

        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def condition_description(self):
        if self.condition == 5:
            return "Great find!"
        if self. condition == 4:
            return "Twas in good care"
        if self.condition == 3:
            return "Morally right"
        if self.condition == 2:
            return "Do it for the turtles"
        if self. condition == 1:
            return "Rethinking thrifting"
        else:
            return "I mean it's free"