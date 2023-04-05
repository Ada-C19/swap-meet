import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition 

    def get_category(self):
        return __class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Heavily used"
        elif self.condition == 1:
            return "Used"
        elif self.condition == 2:
            return "Average"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Great"
        elif self.condition == 5:
            return "Perfect"
        
        # condition = {
        #     0 : "Heavily used",
        #     1 : "Used",
        #     2 : "Average",
        #     3 : "Good",
        #     4 : "Great",
        #     5 : "Perfect"
        # }
        # return f"condtion[self.condtion]"

        # condition = [ "Heavily used", "Used", "Average", "Good", "Great", "Perfect"]
        # retun f"condition[self.condition]"


