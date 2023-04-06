import uuid

class Clothing:
    def __init__(self, condition=0, fabric="Unknown", id=None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.fabric = fabric
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
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    # def __init__(self, condition):
    #     self.condition = condition
    #     self.condition_description = lambda: {
    #         0: "overused eww",
    #         1: "on the edge",
    #         2: "ehhh but doable",
    #         3: "not bad",
    #         4: "oooh nice",
    #         5: "so shiney aaah"
    #     }.get(self.condition, "invalid condition value")()

