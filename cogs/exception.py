from discord.ext import commands
import discord


class ExceptionCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, "original", error)
        ignored = (commands.CommandNotFound,)
        if isinstance(error, ignored):
            return
        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(description=f':bangbang: Bu komutu **sadece <@!149575209026846721>** kullanabilir',
                                  colour=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f':interrobang: **{type(error).__name__}** - {error}',
                                  color=discord.Color.red())
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ExceptionCog(client))
