from discord.ext import commands
import discord
import datetime


class Genel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='Selam çak')
    async def sa(self, ctx):
        await ctx.send(f'Aleyküm borax {ctx.message.author.mention}')

    @commands.command(brief='Davet linkleri',
                      aliases=['davet', 'davetet'])
    async def invite(self, ctx):
        await ctx.send(f'Davet linkleriyle insanları çağırarak büyümemize yardımcı olur musun {ctx.message.author.mention}?'
                       '\nhttps://discord.gg/DDxf9SjWPA'
                       '\n<https://discord.io/erystrix>')

    @commands.command(brief='Bot ile Discord arası gecikme süresi')
    async def ping(self, ctx):
        async with ctx.typing():
            pass
        embed = discord.Embed(description=f':magnet: *Ping: **{round(self.client.latency * 1000)}ms***', color=discord.Color.red())
        await ctx.send(embed=embed)

    @commands.command(brief='Sunucuya ne zaman girdin?')
    async def girdi(self, ctx, member: discord.Member):
        async with ctx.typing():
            pass
        embed = discord.Embed(description=f'<:pog:824718033138090044> {member.mention}, ***{member.joined_at}*** sunucuya girdi.',
                              color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command(brief='Sunucu hakkında bilgi al',
                      aliases=['serverbilgi', 'serverinfo'])
    async def info(self, ctx):
        guild = ctx.guild

        voice_channels = len(guild.voice_channels)
        text_channels = len(guild.text_channels)

        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)

        now = datetime.datetime.now()

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=now.strftime("%X  •  %x  •  %A"))

        embed.add_field(name="Sunucu Adı", value=guild.name, inline=False)
        embed.add_field(name="Ses Kanalları", value=voice_channels)
        embed.add_field(name="Yazı Kanalları", value=text_channels)
        embed.add_field(name="AFK Kanalı", value=guild.afk_channel, inline=False)
        embed.add_field(name="Sunucu Emojileri", value=emoji_string or "None", inline=False)

        async with ctx.typing():
            pass
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Genel(client))
