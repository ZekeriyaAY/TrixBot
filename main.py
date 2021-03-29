from discord.ext import commands
import discord
import logging
import os

description = """
TrixBot Yardım İsteği
"""
intents = discord.Intents.all()
client = commands.Bot(command_prefix='?', description=description, intents=intents)

logging.basicConfig(level=logging.DEBUG)

cogs = ['cogs.owner', 'cogs.exception', 'cogs.event', 'cogs.moderation']
for cog in cogs:
    client.load_extension(cog)
    print(cog)


@client.command()
async def sa(ctx):
    await ctx.send("as")

@client.event
async def on_ready():
    print(f'{client.user} çalışıyor...')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="discord.io/ERYSTRIX"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)


client.run(os.environ.get('TOKEN'))
