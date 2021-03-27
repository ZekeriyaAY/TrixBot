from discord.ext import commands
from discord.utils import get
from datetime import datetime
import discord
import json

class EventCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('./settings.json') as f:
            data = json.load(f)

        autoRole = data['autoRole']
        role = get(member.guild.roles, id=autoRole)
        await member.add_roles(role)

        logChannelID = data['logChannel']
        logChannel = self.client.get_channel(logChannelID)
        embed = discord.Embed(description=f':white_check_mark: {member.mention} üyesine {role} verildi. ', color=discord.Color.green())
        embed.set_footer(text=f'{datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}')
        await logChannel.send(embed=embed)

        welcomeChannelID = data['welcomeChannel']
        welcomeChannel = self.client.get_channel(welcomeChannelID)

        welcomeMessage = f"""
                Aramıza 
                HoşGeldin 
                    {member.mention}
                """
        await welcomeChannel.send(welcomeMessage)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('./settings.json') as f:
            data = json.load(f)

        welcomeChannelID = data['welcomeChannel']
        welcomeChannel = self.client.get_channel(welcomeChannelID)

        leaveMessage = f"""
                        Kendine İyi Bak 
                            {member.mention}
                        """
        await welcomeChannel.send(leaveMessage)


def setup(client):
    client.add_cog(EventCog(client))
