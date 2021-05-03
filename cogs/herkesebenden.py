from discord.ext import commands
import discord


class HerkeseBenden(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief=' Yeni yıl mesajı gönder',
                      aliases=["yeniyil", "yy", "yeniyıl"])
    async def herkesebendenyeniyıl(self, ctx):
        embed = discord.Embed(title=f'Koca Yürekli *{ctx.author.name}*  Herkese Yeni Yıl Diledi',
                              colour=discord.Color.red())
        embed.set_image(
            url='https://reactiongifs.me/wp-content/uploads/2013/12/christmas-is-coming-candice-swanepoel-victorias-secret-angel.gif')
        await ctx.send(embed=embed)

    @commands.command(brief='Çay ısmarla',
                      aliases=["çay", "cay"])
    async def herkesebendençay(self, ctx):
        embed = discord.Embed(title=f'Koca Yürekli *{ctx.author.name}*  Herkese Çay Ismarladı',
                              colour=discord.Color.green())
        embed.set_image(url='https://i.sozcu.com.tr/wp-content/uploads/2018/08/iecrop/cay_16_9_1533630396.jpg')
        await ctx.send(embed=embed)

    @commands.command(brief='Nude gönder',
                      aliases=["nude"])
    async def herkesebendennude(self, ctx):
        embed = discord.Embed(title=f'Koca Yürekli *{ctx.author.name}*  Herkese Nude Yolladı',
                              colour=discord.Color.purple())
        embed.set_image(url='https://i.ytimg.com/vi/-9BSbY8fUWY/maxresdefault.jpg')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(HerkeseBenden(client))
