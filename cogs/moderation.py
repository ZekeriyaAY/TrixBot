from discord.ext import commands
import discord


class ModerationCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            description=f':white_check_mark: *{member.mention}*, *{ctx.message.author.mention}* tarafından **atıldı**. :hammer:'
                        f'\n***Sebep:*** **`{reason}`**',
            colour=discord.Color.green())
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(client):
    client.add_cog(ModerationCog(client))
