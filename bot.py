from discord.ext import commands
import discord, tokens, sansify, os

if not os.path.exists("tempin"):
    os.makedirs("tempin")

if not os.path.exists("tempout"):
    os.makedirs("tempout")

Client = discord.Client()
client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects

@client.event
async def on_message(message):
    if message.content.lower().startswith('#sansify'):
          await sansify.sans(message, client)
          print("sansified")
client.run(tokens.discord)