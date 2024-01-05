import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
discord_key = os.getenv("BOT_KEY")
api_key = os.getenv("API_KEY")
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():

    print("The bot is now ready for use")
    print("----------------------------")

@bot.command()
async def si(ctx, arg):
    #API call here
    params = {"name": arg}
    
    url = f"https://api.starcitizen-api.com/{api_key}/v1/auto/ships"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, params=params)

    json_data = response.content.decode("utf-8")

    prices = []

    for ship in json.loads(json_data)["data"]:
        price = ship["price"]
        prices.append(price)

    print(prices)

   

    #Send the information
   # channel = bot.get_channel(939767212716199949)
   # await channel.send (response.json())









bot.run(discord_key)