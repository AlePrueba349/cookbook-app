import json
from pathlib import Path

from recipe import Recipe


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
            f"{recipe.title.lower().replace(' ', '_')}.json"
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
            f"{recipe_name.lower().replace(' ', '_')}.json"
        )

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        return Recipe.from_dict(data)