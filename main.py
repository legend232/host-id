import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import platform
import time
import colorsys
import random
prefix = "§"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="owner" #change which role you need!



@bot.event
async def on_ready():
    print('Online')
    print("Created by RaghavRaider")
    print("REBELLION :")
    print("https://discord.gg/reop")
    print("Raghav Op As Always")
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="INDIAS TOP 1 RAIDER"))
    	await asyncio.sleep(5)
   
    	await bot.change_presence(activity=discord.Activity(type=1,name="C4 OP"))
    	await asyncio.sleep(5)
        
@bot.command(name="hi")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
    
bot.run("Nzg3OTQwMTc1Nzk1MDYwNzM2.YL-2ag.Y50jE3PDqn6NDG-Gzymbonj7_zA",bot=False)
