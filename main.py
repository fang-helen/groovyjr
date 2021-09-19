import discord
import os
from dotenv import load_dotenv

client = discord.Client()

# ---------------------------


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('-gd'):
        await message.channel.send('AWAKE')

    elif message.content.startswith('-join'):
        if message.author.voice and message.author.voice.channel:
            channel = message.author.voice.channel
            await message.channel.send('Groovy Jr. in ' + channel.name)
            await message.guild.change_voice_state(channel=channel, self_mute=False, self_deaf=True)
        else:
            await message.channel.send("You are not connected to a voice channel")
            return
    if  message.content.startswith('-leave'):
        if message.author.voice and message.author.voice.channel:
            print('leaving')
            await message.guild.change_voice_state(channel=None)
        else:
            await message.channel.send("You are not connected to a voice channel")

# ----------------------------

load_dotenv()
client.run(os.getenv('TOKEN'))
