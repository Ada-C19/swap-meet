class Decor:
    def __init__(self, id, width = 0, length = 0):
        self.id = id
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It takes up a {self.width} by {self.length} sized space."