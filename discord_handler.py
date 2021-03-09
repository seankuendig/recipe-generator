import os

from discord.ext import commands
from dotenv import load_dotenv

import json_handler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


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
