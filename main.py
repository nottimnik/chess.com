#Discord Libraries
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot

client = commands.Bot(command_prefix="-")

#Other Files
from src.user_stats import get_player_rating

#removes the default help command
client.remove_command("help")

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("----------")
    await client.change_presence(activity=discord.Game(name="-help"))

@client.command()
async def help(ctx):
    em = discord.Embed(title = "SOME1 Help Commands")
    em.add_field(name = "!stats <username>", value = "`get the stats of the given user`")
    await ctx.send(embed = em)

@client.command() #Stats Command
async def stats(ctx, username = None):
    if(username == None): #error if the user didn't entered a username
        em = discord.Embed(title="You need to enter the username of the user you want to get the stats of", description = "Usage: `!stats [username]`", color = 15158332)
        await ctx.send(embed = em)
    else:
        em = discord.Embed(title = f"{username}\'s Stats", description = f"The chess.com stats of the user: {username}", color = 12370112)
        ratings = get_player_rating(username)
        em.add_field(name = f"Blitz", value = f"{ratings[0]}")
        em.add_field(name = f"Rapid", value = f"{ratings[1]}")
        em.add_field(name = f"Bullet", value = f"{ratings[2]}")
        em.add_field(name = f"Daily", value = f"{ratings[3]}")
        em.add_field(name = f"Puzzles", value = f"{ratings[4]}")
        em.add_field(name = f"Puzzle Rush", value = f"{ratings[5]}")
        await ctx.send(embed = em)

@stats.error
async def stats_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        em = discord.Embed(title = "We couldn't find this user :(", color = 15158332)
        await ctx.send(embed = em)


##reads the token from the file token.txt
token = open(f"Token/token.txt", "r")
token_key = token.read()
token.close()
client.run(token_key)