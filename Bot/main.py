import discord

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests

load_dotenv()
discord_key = os.getenv("BOT_KEY")
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():

    print("The bot is now ready for use")
    print("----------------------------")

bot.run(discord_key)