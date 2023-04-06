import uuid

class Electronics:

    def __init__(self,condition=0,id=None, type="Unknown"):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.type = type
        self.condition = condition
        self.condition_description = lambda: {
            0: "overused eww",
            1: "on the edge",
            2: "ehhh but doable",
            3: "not bad",
            4: "oooh nice",
            5: "so shiney aaah"
        }.get(self.condition, "invalid condition value")

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
        