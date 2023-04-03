class Clothing:
    def __init__(self, id, fabric = "Unknown"):
        self.id = id
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."
