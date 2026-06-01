import uuid
from cookbook.ingredient import Ingredient
from cookbook.step import Step



class Recipe:

    def __init__(self, title: str, servings: int = 1, recipe_id=None):

        self.id = recipe_id or str(uuid.uuid4())
        self.title = title
        self.servings = servings
        self.ingredients = []
        self.steps = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_step(self, step):
        self.steps.append(step)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "servings": self.servings,
            "ingredients": [
                ingredient.to_dict()
                for ingredient in self.ingredients
            ],
            "steps": [
                step.to_dict()
                for step in self.steps
            ]
        }

    @classmethod
    def from_dict(cls, data):

        recipe = cls(
            title=data["title"],
            servings=data["servings"],
            recipe_id=data["id"]
        )

        for ingredient_data in data["ingredients"]:
            recipe.add_ingredient(
                Ingredient.from_dict(ingredient_data)
            )

        for step_data in data["steps"]:
            recipe.add_step(
                Step.from_dict(step_data)
            )

        return recipe

    def show(self):
        print(f"\n=== {self.title} ===")
        print(f"Porciones: {self.servings}")

        print("\nIngredientes:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

        print("\nPasos:")
        for i, step in enumerate(self.steps, start=1):
            print(f"{i}. {step}")