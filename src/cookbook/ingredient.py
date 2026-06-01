class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["quantity"],
            data["unit"]
        )

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"