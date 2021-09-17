##Test File
import discord
import os
from dotenv import load_dotenv

client = discord.Client()
##---------------------------
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('-gd'):
        await message.channel.send('AWAKE')


##----------------------------
load_dotenv()
print(client)
client.run(os.getenv('TOKEN'))