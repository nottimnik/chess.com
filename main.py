#Discord Libraries
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot

client = commands.Bot(command_prefix="-")

#Other Files
from src.user_stats import get_current_player_rating, get_status

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
    em.add_field(name = "-stats <username>", value = "`get the stats of the given user`", inline = False)
    em.add_field(name = "-status <username>", value = "`check if the user is online or offline`")
    await ctx.send(embed = em)

@client.command() #Stats Command
async def stats(ctx, username = None):
    if(username == None): #error if the user didn't entered a username
        em = discord.Embed(title="You need to enter the username of the user you want to get the stats of", description = "Usage: `!stats [username]`", color = 15158332)
        await ctx.send(embed = em)
    else:

        status = "" #the status of the user
        if(get_status(username)): 
            status = "Online" #the user is online on chess.com
        else:
            status = "Offline" #the user is offline on chess.com

        em = discord.Embed(title = f"{username}\'s Stats", description = f"Status: {status}", color = 0x2ecc71)
        current_ratings = get_current_player_rating(username)
        em.add_field(name = f"Blitz", value = f"Current: {current_ratings[0]}", inline=False)
        em.add_field(name = f"Rapid", value = f"Current: {current_ratings[1]}", inline=False)
        em.add_field(name = f"Bullet", value = f"Current: {current_ratings[2]}", inline=False)
        em.add_field(name = f"Daily", value = f"Current: {current_ratings[3]}", inline=False)
        em.add_field(name = f"Puzzles", value = f"Best: {current_ratings[4]}", inline=False)
        em.add_field(name = f"Puzzle Rush", value = f"Best: {current_ratings[5]}", inline=False)
        await ctx.send(embed = em)

@stats.error
async def stats_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        em = discord.Embed(title = "We couldn't find this user :(", color = 15158332)
        await ctx.send(embed = em)

@client.command() #Status Command
async def status(ctx, username = None):
    if(username == None): #error if the user didn't entered a username
        em = discord.Embed(title="You need to enter the username of the user you want to get the status of", description = "Usage: `!status [username]`", color = 15158332)
        await ctx.send(embed = em)
    else:

        if(get_status(username)):  #the user is online on chess.com
            em = discord.Embed(title = f"{username} is online!", color = 0x2ecc71)
            await ctx.send(embed = em)
        else: #the user is offline on chess.com
            em = discord.Embed(title = f"{username} is offline :(", color = 15158332)
            await ctx.send(embed = em)           
        

@status.error
async def status_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        em = discord.Embed(title = "We couldn't find this user :(", color = 15158332)
        await ctx.send(embed = em)


##reads the token from the file token.txt
token = open(f"token/token.txt", "r")
token_key = token.read()
token.close()
client.run(token_key)