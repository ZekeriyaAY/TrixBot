from discord.ext import commands
import discord
import logging
import os

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
        activity=discord.Activity(type=discord.ActivityType.watching, name="discord.io/ERYSTRIX"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    async def sa(ctx):
        await ctx.send(f'Aleyküm borax {ctx.message.author.mention}')

    await client.process_commands(message)


client.run(os.environ.get('TOKEN'))
