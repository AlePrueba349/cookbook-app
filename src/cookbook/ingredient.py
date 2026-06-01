class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"