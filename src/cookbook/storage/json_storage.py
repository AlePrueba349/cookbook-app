import json
from pathlib import Path
from cookbook.recipe import Recipe
from cookbook.utils import normalize_filename

class JsonStorage:

    def __init__(self, data_folder="data/recipes"):
        self.data_folder = Path(data_folder)
        self.data_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_recipe(self, recipe: Recipe):

        filename = (
            self.data_folder /
            f"{normalize_filename(recipe.title)}.json"
        )

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                recipe.to_dict(),
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_recipe(self, recipe_name: str):

        filename = (
            self.data_folder /
            f"{normalize_filename(recipe_name)}.json"
        )

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        return Recipe.from_dict(data)