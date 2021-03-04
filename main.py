import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")

##reads the token from the file token.txt
token = open(f"Token/token.txt", "r")
token_key = token.read()
token.close()
client.run(token_key)