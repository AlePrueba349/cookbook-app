from cookbook.ingredient import Ingredient
from cookbook.step import Step
from cookbook.recipe import Recipe

from cookbook.storage.json_storage import JsonStorage
from cookbook.managers.recipe_manager import RecipeManager


def main():

    storage = JsonStorage()
    manager = RecipeManager(storage)

    pizza = Recipe("Pizza Margarita", 4)

    pizza.add_ingredient(
        Ingredient("Harina", 500, "g")
    )

    pizza.add_ingredient(
        Ingredient("Agua", 300, "ml")
    )

    pizza.add_step(
        Step("Mezclar ingredientes")
    )

    pizza.add_step(
        Step("Amasar", 10)
    )

    manager.save_recipe(pizza)

    print("\nRecetas disponibles:")

    for recipe_name in manager.list_recipes():
        print("-", recipe_name)

    recipe = manager.get_recipe(
        "Pizza Margarita"
    )

    recipe.show()


if __name__ == "__main__":
    main()