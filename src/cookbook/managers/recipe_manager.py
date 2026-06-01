from pathlib import Path
from cookbook.utils import normalize_filename

class RecipeManager:

    def __init__(self, storage):
        self.storage = storage

    def save_recipe(self, recipe):
        self.storage.save_recipe(recipe)

    def get_recipe(self, recipe_name):
        return self.storage.load_recipe(recipe_name)

    def list_recipes(self):

        recipes = []

        for file in self.storage.data_folder.glob("*.json"):
            recipes.append(file.stem)

        return sorted(recipes)

    def recipe_exists(self, recipe_name):

        filename = (
            self.storage.data_folder /
            f"{normalize_filename(recipe_name)}.json"
        )

        return filename.exists()

    def delete_recipe(self, recipe_name):

        filename = (
            self.storage.data_folder /
            f"{normalize_filename(recipe_name)}.json"
        )

        if filename.exists():
            filename.unlink()
            return True

        return False