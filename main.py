# Import discord package
import discord

# The bot
bot = discord.Client()

# creates a function
@bot.event
async def on_ready(): # async allows the function to run even though there is a delay
    general_channel = bot.get_channel(827643671171039286)

    await general_channel.send('Hello world!') # await is needed to wait for the channel to be retrieved

# when the bot gets a specific message
@bot.event
async def on_message(message):
    if message.content == 'm! motivation':
        general_channel = bot.get_channel(827643671171039286)
        await general_channel.send('You can do this!!')

# When the bot disconnects from the server
@bot.event
async def on_disconnet():
    general_channel = bot.get_channel(827643671171039286)
    await general_channel.send('Goodbye and good luck in your assignments!')


# Run the bot on server
bot.run('token')
