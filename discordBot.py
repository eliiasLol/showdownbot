import discord
from discord.ext import commands
from discord import Intents
import httpsRequest
import json




url_events = "https://api.brawlapi.com/v1/events"
url_brawler = "https://api.brawlapi.com/v1/brawlers"



def getData(url):
    data = httpsRequest.getData(url)
    return data

def getBrawlerName(id):
    data = getData(url_brawler+f"/{id}")
    name = data["name"]
    return name

def GetCurrentMap():
    data = getData(url_events)
    data = data["active"][0]["map"]
    imageUrl = data["imageUrl"]
    name = data["name"]
    brawlers = []
    for i in range(0,5):
        brawlers.append(getBrawlerName(data["stats"][i]["brawler"]))
    data = [imageUrl,name,brawlers]
    return data

def GetNextMap():
    data = getData(url_events)
    data = data["upcoming"][0]["map"]
    imageUrl = data["imageUrl"]
    name = data["name"]
    brawlers = []
    for i in range(0,5):
        brawlers.append(getBrawlerName(data["stats"][i]["brawler"]))
    data = [imageUrl,name,brawlers]
    return data

def makeEmbed(data):
    embed = discord.Embed(
        title="Map",
        description=data[1],
        color=0x00FFFF
    )
    names = data[2]
    embed.add_field(
        name="Best Brawlers (by Winrate):",
        value=f"1. {names[0]}\n2. {names[1]}\n3. {names[2]}\n4. {names[3]}\n5. {names[4]}",
        inline=True
    )
    embed.set_image(url=str(data[0]))

    return embed

intents = Intents.default()
intents.messages = True  
intents.message_content = True



bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def helpMe(ctx):
    txt = "Place Holder"
    await ctx.send(txt)

@bot.command()
async def hi(ctx):
    await ctx.send(f"Hi {ctx.message.author}")

@bot.command()
async def currentmap(ctx):
    data = GetCurrentMap()
    embed = makeEmbed(data)
    await ctx.send(embed=embed)
   


@bot.command()
async def nextmap(ctx):
    data = GetNextMap()
    embed = makeEmbed(data)
    await ctx.send(embed=embed)




bot.run("MTI2NTkzNjM4MTM3MzQ1MjQwOA.Gkclxi.R4YfE5Oang-Tji80Ri9NOD8n1XCtgIQkqPu39c")