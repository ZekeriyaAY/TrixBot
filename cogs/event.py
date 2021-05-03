from discord.ext import commands
from discord.utils import get
from datetime import datetime
import discord
import json


class EventCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if isinstance(after.activity, discord.Streaming) and after.id == 149575209026846721:
            with open('./settings.json') as f:
                data = json.load(f)
            announceChannelID = data['announceChannel']
            announceChannel = self.client.get_channel(announceChannelID)

            stream_platform = after.activity.platform
            stream_title = after.activity.name
            stream_game = after.activity.game
            stream_url = after.activity.url
            streamer_name = after.activity.twitch_name

            twitchLiveMessage = f"""
                ** <:pepeshh:824718515092455455> `{streamer_name}` *{before.name}*  `{stream_game}` YAYINI AÇTI HEM DE `720p60fps`** <:pog:824718033138090044> 
            <:twitch:824718148258889818> ** `{stream_title}` **
            <:live:824718114947989624> *** {stream_url} *** <:live:824718114947989624> @everyone
            """
            await self.client.change_presence(
                activity=discord.Streaming(name=streamer_name, url=stream_url, details=stream_title))
            await announceChannel.send(twitchLiveMessage)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('./settings.json') as f:
            data = json.load(f)

        autoRole = data['autoRole']
        role = get(member.guild.roles, id=autoRole)
        await member.add_roles(role)

        logChannelID = data['logChannel']
        logChannel = self.client.get_channel(logChannelID)
        embed = discord.Embed(description=f':white_check_mark: {member.mention} üyesine {role} verildi. ',
                              color=discord.Color.green())
        embed.set_footer(text=f'{datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}')
        await logChannel.send(embed=embed)

        welcomeMessage = f""" 
            Aramıza 
            HoşGeldin 
                {member.mention}
        """
        await logChannel.send(welcomeMessage)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('./settings.json') as f:
            data = json.load(f)

        logChannelID = data['logChannel']
        logChannel = self.client.get_channel(logChannelID)
        leaveMessage = f"""
            Kendine İyi Bak 
                {member.mention}
        """
        await logChannel.send(leaveMessage)


def setup(client):
    client.add_cog(EventCog(client))
