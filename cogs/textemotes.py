import discord
import asyncio
from discord.ext import commands
import random


class textemotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thumbs(self, ctx):
        """(👍' - ')👍"""
        await ctx.message.edit(content="(👍' - ')👍")

    @commands.command()
    async def cookie(self, ctx):
        """(  ' - ')-🍪"""
        await ctx.message.edit(content="(  ' - ')-🍪")

    @commands.command()
    async def cat(self, ctx):
        await ctx.message.edit(
            content="""{ \  / }
( ^ - ^ )
( u   u )～"""
        )

    @commands.command()
    async def pew(self, ctx):
        """(   ' - ')>---------- pew pew"""
        await ctx.message.edit(content="(   ' - ')>---------- pew pew")

    @commands.command()
    async def lpew(self, ctx):
        """pew pew ----------<(' - '   )"""
        await ctx.message.edit(content="pew pew ----------<(' - '   )")

    @commands.command()
    # Credits to Daddy Ræd#6358 for cow design lol
    async def cow(self, ctx):
        cnt = """```
 __________
 |        |
 |  Moo   |
 |        |
 ¯¯¯¯¯¯¯¯¯¯
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
```"""

        em = discord.Embed(color=random.randint(0, 0xFFFFFF))
        em.description = cnt
        await ctx.send(embed=em)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(textemotes(bot))
