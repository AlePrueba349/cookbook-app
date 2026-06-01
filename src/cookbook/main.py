from ingredient import Ingredient
from step import Step
from recipe import Recipe

from storage.json_storage import JsonStorage


def main():

    storage = JsonStorage()

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

    storage.save_recipe(pizza)

    receta = storage.load_recipe(
        "Pizza Margarita"
    )

    receta.show()


if __name__ == "__main__":
    main()