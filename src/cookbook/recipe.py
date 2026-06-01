from ingredient import Ingredient
from step import Step


class Recipe:
    def __init__(self, title: str, servings: int = 1):
        self.title = title
        self.servings = servings
        self.ingredients = []
        self.steps = []

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def add_step(self, step: Step):
        self.steps.append(step)

    def show(self):
        print(f"\n=== {self.title} ===")
        print(f"Porciones: {self.servings}")

        print("\nIngredientes:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

        print("\nPasos:")
        for index, step in enumerate(self.steps, start=1):
            print(f"{index}. {step}")