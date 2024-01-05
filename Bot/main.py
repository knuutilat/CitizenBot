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
async def price(ctx, arg):
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
        name = ship["name"]

    print(prices[0])


    channel = bot.get_channel(1192813043244089444)
    await channel.send(f"Price for {name} is {prices[0]} dollars")

   

@bot.command()
async def info(ctx, arg):

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
        name = ship["name"]
        description = ship["description"]
        shiptype = ship["type"]
        size = ship["size"]
        capacity = ship["cargocapacity"]
        focus = ship["focus"]
        speed = ship["scm_speed"]

    print(prices[0])

    embed = discord.Embed(title=name, url="https://google.com", description=description, color=0x4dff4d)
    embed.add_field(name="Price", value=prices[0], inline=True)
    embed.add_field(name="Type", value=shiptype, inline=True)
    embed.add_field(name="Size", value=size, inline=True)
    embed.add_field(name="Cargo capacity", value=capacity, inline=True)
    embed.add_field(name="Focus", value=focus, inline=True)
    embed.add_field(name="SCM Speed", value=speed, inline=True)
    await ctx.send(embed=embed)








bot.run(discord_key)