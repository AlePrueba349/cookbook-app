class Recipe:
    def __init__(self, title: str):
        self.title = title
        self.ingredients = []
        self.steps = []

    def add_ingredient(self, ingredient: str):
        self.ingredients.append(ingredient)

    def add_step(self, step: str):
        self.steps.append(step)

    def show(self):
        print(f"\nReceta: {self.title}")

        print("\nIngredientes:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

        print("\nPasos:")
        for index, step in enumerate(self.steps, start=1):
            print(f"{index}. {step}")