import discord
import asyncio
from discord.ext import commands
import requests


class crypto(commands.Cog):
    """Uhhh discord coding is shit"""

    def __init__(self, bot):
        self.bot = bot

### Discord blockbypass coming soon. Creds to Yaekith for that shit
    #@commands.command()


def setup(bot):
    bot.add_cog(malicious(bot))
