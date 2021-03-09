import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
from dotenv import load_dotenv
import discord

import json_handler
import recipes
# import mail_handler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


async def dm():
    for user in json_handler.get_all_users():
        recipe_config = recipes.RecipeConfiguration(user['diet'], user['exclude'],
                                                    user['target_calories'])
        recipe_data = recipes.send_request(recipe_config)
        # mail_handler.sendmail(recipe_data, user)
        user = await bot.fetch_user(int(user['user_id']))
        embedVar = discord.Embed(title="Recipes", description="Todays recipes")
        for meal in recipe_data['meals']:
            embedVar.add_field(name=meal['title'], value=meal['sourceUrl'])
        embedVar.add_field(name="Nutrition", value=recipe_data['nutrients'])
        await user.send(embed=embedVar)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("------")
    scheduler = AsyncIOScheduler()
    scheduler.add_job(dm, CronTrigger(minute="09"))
    scheduler.start()


@bot.command(name='configure')
async def on_message(ctx, email, diet, exclude, target_calories: int):
    if ctx.author == bot.user:
        return
    if not ctx.guild:
        config = {'email': email, 'user_id': ctx.author.id, 'diet': diet, 'exclude': exclude,
                  'target_calories': target_calories}
        json_handler.update(config)
        await ctx.send("Successfully updated config.")


bot.run(TOKEN)
