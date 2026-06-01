from recipe import Recipe


def main():
    recipe = Recipe("Pizza Margarita")

    recipe.add_ingredient("500 g harina")
    recipe.add_ingredient("300 ml agua")

    recipe.add_step("Mezclar ingredientes")
    recipe.add_step("Amasar durante 10 minutos")

    recipe.show()


if __name__ == "__main__":
    main()