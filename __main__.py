import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
from pygame import mixer
# Replace with the channel ID you want to monitor
MONITOR_CHANNEL_ID = 1333064517114007582  # Replace with the actual channel ID

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.event
async def on_message(message):

    # Check if the message is from the specific channel
    if message.channel.id == MONITOR_CHANNEL_ID:
        print(f"""Panic button! 
        Location: {message.content}""")
        mixer.init()
        mixer.music.load('python_projektit\AndroidApp\panic-button.mp3')
        mixer.music.play()
        

    # Optionally, if you want the bot to continue processing commands
    await bot.process_commands(message)

bot.run("MTMzMzA3NjE5NDQ4MDA5NTIzMg.Geirk5.7fvWN-1Cq91x163zFV8K6Ar2j19sNgySnE3GvQ")

 