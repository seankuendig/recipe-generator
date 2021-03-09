import json_handler
import mail_handler
import recipes

if __name__ == '__main__':
    recipe_config = recipes.RecipeConfiguration("vegetarian")
    #print(recipes.send_request(recipe_config))
    user = json_handler.get_all_users()[0]
    mail_handler.sendmail(recipes.send_request(recipe_configuration=recipe_config), user)


