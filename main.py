import recipes

if __name__ == '__main__':
    recipe_config = recipes.RecipeConfiguration("vegetarian")
    print(recipes.send_request(recipe_config))

