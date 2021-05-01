# Import discord package
import discord
from discord.ext import commands
import time

# The bot
bot = commands.Bot(command_prefix='m! ')

@bot.command(name = 'motivate')
async def motivate(context):
    
    await context.message.channel.send('You can do this! I believe in you!')

@bot.command(name = 'pomodoro')
async def pomodoro(context):
    answer = input("Do you want 1. 25 min work 5 min break or 2. 50 min work 10 min break")
    if answer == 1:
        mins = 25
        sec = 0
        timer = '{:02d}:{:02d}'.format(mins, sec)

    await context.message.channel.send('You have .. minutes left')

@bot.command(name = 'help')
async def help(context):
    myEmbed = discord.Embed(title = "List of functions")
    myEmbed.add_field(name = "m! motivate", value = "a message that motivates you")
    myEmbed.add_field(name = "m! pomodoro", value = "creates a new 25 min pomodoro session")
    myEmbed.add_field(name = "m! help", value = "shows all functions of the bot")
    myEmbed.add_field(name = "m! version", value = "shows version number")
    
    await context.message.channel.send(embed = myEmbed)

@bot.command(name = 'version')
async def version(context):

    myEmbed = discord.Embed(title = "Current Version", description = "The bot is in version 1.0", color = 0x00ff00) # hexadecimal for number color
    myEmbed.add_field(name = "Version Code: ", value = "v1.0.0", inline = False)
    myEmbed.add_field(name = "Date Released: ", value = "April 5th, 2020", inline = False)
    myEmbed.set_footer(text = "itsannb production")
    myEmbed.set_author(name = "Ann B")

    await context.message.channel.send(embed = myEmbed)

# creates a function
@bot.event
async def on_ready(): # async allows the function to run even though there is a delay
    general_channel = bot.get_channel(827643671171039286)

    await general_channel.send('Hello world!') # await is needed to wait for the channel to be retrieved

# when the bot gets a specific message
@bot.event
async def on_message(message):
    if message.content == 'what is the version':
        general_channel = bot.get_channel(827643671171039286)
        myEmbed = discord.Embed(title = "Current Version", description = "The bot is in version 1.0", color = 0x00ff00) # hexadecimal for number color
        myEmbed.add_field(name = "Version Code: ", value = "v1.0.0", inline = False)
        myEmbed.add_field(name = "Date Released: ", value = "April 5th, 2020", inline = False)
        myEmbed.set_footer(text = "itsannb production")
        myEmbed.set_author(name = "Ann B")

        await general_channel.send(embed = myEmbed)
    
    await bot.process_commands(message)

# When the bot disconnects from the server
@bot.event
async def on_disconnet():
    general_channel = bot.get_channel(827643671171039286)
    await general_channel.send('Goodbye and good luck in your assignments!')


# Run the bot on server
bot.run('token')
