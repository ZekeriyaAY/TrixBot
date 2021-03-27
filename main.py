from discord.ext import commands
import logging
import os

description = """
TrixBot Yardım İsteği
"""
client = commands.Bot(command_prefix='?', description=description)

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

cogs = ['cogs.owner', 'cogs.exception', 'cogs.event']
for cog in cogs:
    client.load_extension(cog)
    print(cog)

@commands.command()
async def sa(ctx):
    await ctx.send("as")

@client.event
async def on_ready():
    print(f'{client.user} çalışıyor...')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)


client.run(os.environ.get('TOKEN'))