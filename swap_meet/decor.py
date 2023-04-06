import uuid
class Decor:
    def __init__(self, id=None, width=0, length=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.width = width
        self.length = length
       # self.condition = condition

    def get_category(self):
        return "Decor"

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

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