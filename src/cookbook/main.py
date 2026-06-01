from ingredient import Ingredient
from step import Step
from recipe import Recipe
from cookbook import CookBook


def main():

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

    pizza.show()

    libro = CookBook("Recetas Italianas")

    libro.add_recipe(pizza)

    libro.show()


if __name__ == "__main__":
    main()