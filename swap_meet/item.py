import uuid

class Item:
    
    def __init__(self, id=None, condition=0, age=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition
        self.age = age
        
    def __str__(self):
        category = self.get_category()
        return f"An object of type {category} with id {self.id}."

    def get_category(self):
            return "Item"
        
    def condition_description(self):
        condition_description = [
            "Just as you go to examine this item, it disintegrates to dust.",
            "You barely know what it is now, but you have no idea what it WAS.",
            "More pokey bumps than a pineapple! Good? Bad? You decide!",
            "Perfectly acceptable quality if this is a gift... for your frenemy.",
            "While not perfect, the flaws make it unique and priceless!",
            "You gasp and clutch your chest as your eyes begin to water. Until now, you had never seen something so perfect."
        ]
        
        if self.condition < 1:
            return condition_description[0]
        elif self.condition < 2:
            return condition_description[1]
        elif self.condition < 3:
            return condition_description[2]
        elif self.condition < 4:
            return condition_description[3]
        elif self.condition < 5:
            return condition_description[4]
        elif self.condition == 5:
            return condition_description[5]