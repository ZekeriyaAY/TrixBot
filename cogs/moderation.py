from discord.ext import commands
import discord


class Moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Mesaj yazdırır')
    # @commands.has_permissions(mention_everyone=True)
    async def yaz(self, ctx, *, msg):
        if '@everyone','@here' in msg:
            await ctx.send("Everyone kullanamazsın!")
        await ctx.send(msg)

    @commands.command(brief='Sunucudan atar')
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
    client.add_cog(Moderator(client))
