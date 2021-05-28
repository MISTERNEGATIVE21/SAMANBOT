import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.idle, activity= discord.Activity(type= discord.ActivityType.playing, name="With Suman's Heart & %help"))
    print('Bot is online')


client.run('ODI0MzcxODY3MzA5MTc4OTAw.YFuaIQ.BH1iYXisNS0TkBWYQD3u6JClSoE')