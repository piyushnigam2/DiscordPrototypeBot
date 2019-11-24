import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = discord.Client()
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
    if message.content.find("!owner") != -1:
        await message.channel.send("This bot is created by Piyush")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
