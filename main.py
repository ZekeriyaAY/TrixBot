from discord.ext import commands
import discord
import logging
import os
import json

description = """
TrixBot Yardım Merkez | Sorun varsa--> @z3k#9977
"""
intents = discord.Intents.all()
client = commands.Bot(command_prefix='?', description=description, intents=intents)

logging.basicConfig(level=logging.INFO)

cogs = ['cogs.owner', 'cogs.exception', 'cogs.event', 'cogs.moderation', 'cogs.command', 'cogs.herkesebenden']
for cog in cogs:
    client.load_extension(cog)
    print(cog)


@client.event
async def on_ready():
    print(f'{client.user} çalışıyor...')
    await client.change_presence(
        activity=discord.Streaming(name="twitch.tv/ERYSTRIX", url="https://www.twitch.tv/erystrix"))


    with open('./settings.json') as f:
            data = json.load(f)
    chatChannelID = data['chatChannel']
    chatChannel = client.get_channel(chatChannelID)
    await chatChannel.send(f'Ohh! Kodlarım çok güzel çalışıyor <3 <@149575209026846721> :magnet: *Ping: **{round(client.latency * 1000)}ms***')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('sa'):
        await message.channel.send(f'Aleyküm borax {message.author.mention}')

    await client.process_commands(message)


client.run(os.environ.get('TOKEN'))
