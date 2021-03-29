from datetime import datetime
from discord.ext import commands
import discord


class z3k(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Verilen cog\'u yükler')
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        self.client.load_extension(f'cogs.{cog}')
        embed = discord.Embed(description=f':white_check_mark: **{cog}** Yüklendi', color=discord.Color.green())
        await ctx.send(embed=embed)
        print(f'{datetime.now().strftime("%H:%M:%S")} cogs.{cog} Yüklendi')

    @commands.command(brief='Verilen cog\'u kaldırır')
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        self.client.unload_extension(f'cogs.{cog}')
        embed = discord.Embed(description=f':white_check_mark: **{cog}** Kaldırıldı', color=discord.Color.green())
        await ctx.send(embed=embed)
        print(f'{datetime.now().strftime("%H:%M:%S")} cogs.{cog} Kaldırıldı')

    @commands.command(brief='Verilen cog\'u tekrar yükler')
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        self.client.reload_extension(f'cogs.{cog}')
        embed = discord.Embed(description=f':white_check_mark: **{cog}** Tekrar Yüklendi', color=discord.Color.green())
        await ctx.send(embed=embed)
        print(f'{datetime.now().strftime("%H:%M:%S")} cogs.{cog} Tekrar Yüklendi')


def setup(client):
    client.add_cog(z3k(client))
