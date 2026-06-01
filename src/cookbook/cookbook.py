class CookBook:
    def __init__(self, title: str):
        self.title = title
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def show(self):
        print(f"\nLibro: {self.title}")

        for recipe in self.recipes:
            print(f"- {recipe.title}")