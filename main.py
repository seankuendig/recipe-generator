import mail_handler
import recipes
import discord_handler

if __name__ == '__main__':
    recipe_config = recipes.RecipeConfiguration("vegetarian")
    #print(recipes.send_request(recipe_config))
    mail_handler.sendmail()


