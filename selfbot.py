import discord
from discord import Color
from discord.ext import commands
from ext.context import CustomContext
from ext.helpformatter import helpformatter
from ext import embedtobox
import aiohttp
import json
import os
import re
import traceback
from colorama import Fore, init
import sys
import requests
import datetime

with open("./data/config.json") as f:
    config = json.load(f)

SNIPER = config.get("SNIPER")

__version__ = "3.2.1"
__author__ = "Daddie0 || https://daddie.xyz"


class Selfbot(commands.Bot):
    def __init__(self, **attrs):
        super().__init__(
            command_prefix=self.get_pre,
            self_bot=True,
            help_command=helpformatter(),
            guild_subscriptions=False,
        )
        self.load_extensions()
        self.snipes = {}

    def load_extensions(self):
        for extension in (
            "anim",
            "crypto",
            "misc",
            "mod",
            "memes",
            "malicious",
            "nukes",
            "noble",
            "skid",
            "source",
            "textemotes",
            "utils",
        ):
            try:
                self.load_extension(f"cogs.{extension}")
                print(f"{Fore.GREEN}[-] {Fore.RESET}Loaded extension: {extension}")
            except:
                print(
                    f"{Fore.RED}[-] {Fore.RESET}LoadError: {extension}\n"
                    f"{traceback.print_exc()}"
                )

    @property
    def token(self):
        """Returns your token wherever it is"""
        with open("data/config.json") as f:
            config = json.load(f)
            if config.get("TOKEN") == "-":
                if not os.environ.get("TOKEN"):
                    self.run_wizard()
            else:
                token = config.get("TOKEN").strip('"')
        return os.environ.get("TOKEN") or token

    @staticmethod
    async def get_pre(bot, message):
        """Returns the prefix."""
        with open("data/config.json") as f:
            prefix = json.load(f).get("PREFIX")
        return os.environ.get("PREFIX") or prefix or "r."

    def restart(self):
        os.execv(sys.executable, ["python"] + sys.argv)

    @staticmethod
    def run_wizard():
        """Wizard for first start"""
        print("------------------------------------------")
        token = input("Enter your token:\n> ")
        print("------------------------------------------")
        prefix = input("Enter a prefix for your selfbot:\n> ")
        print("------------------------------------------")
        sniper = input("Do you want to snipe discord nitro codes? [True, False]\n> ")
        data = {"TOKEN": token, "PREFIX": prefix, "SNIPER": sniper}
        with open("data/config.json", "w") as f:
            f.write(json.dumps(data, indent=4))
        print("------------------------------------------")
        print("Restarting...")
        print("------------------------------------------")
        os.execv(sys.executable, ["python"] + sys.argv)

    @classmethod
    def init(bot, token=None):
        """Starts the actual bot"""
        print(
            f"""{Fore.GREEN}
  $$$$$$$  /$$                               /$$$$$$$
| $$__  $$|__/                              | $$__  $$
| $$  \ $$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$
| $$  | $$| $$ /$$_____/ /$$_____/ /$$__  $$| $$$$$$$/ |____  $$ /$$__  $$ /$$__  $$
| $$  | $$| $$|  $$$$$$ | $$      | $$  \ $$| $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$$$
| $$  | $$| $$ \____  $$| $$      | $$  | $$| $$  \ $$ /$$__  $$| $$  | $$| $$_____/
| $$$$$$$/| $$ /$$$$$$$/|  $$$$$$$|  $$$$$$/| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$
|_______/ |__/|_______/  \_______/ \______/ |__/  |__/ \_______/| $$____/  \_______/
                                                                | $$
                                                                | $$
                                                                |__/

                                                                Version > {Fore.RESET}{__version__}
                                                                {Fore.GREEN}Made by > {Fore.RESET}{__author__}
    """
        )
        print(f"{Fore.GREEN}[-] {Fore.RESET}Made with <3 by Daddie")
        print(f"{Fore.GREEN}[-] Nitro Sniper | {Fore.CYAN}{SNIPER}")

        selfbot = bot()
        safe_token = token or selfbot.token.strip("")
        try:
            selfbot.run(safe_token, bot=False, reconnect=True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        print("connected")

    async def on_ready(self):
        """Bot startup"""
        print("Logged in!")
        await self.change_presence(status=discord.Status.online, afk=True)

    async def process_commands(self, message):
        """Utilises the CustomContext subclass of discord.Context"""
        ctx = await self.get_context(message, cls=CustomContext)
        self.ctx = await self.get_context(message, cls=CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)

    @classmethod
    def black(cls):
        return cls(0x000000)

    discord.Color.black = black

    async def on_message_delete(self, message):
        if len(message.content) != 1:
            self.snipes[message.channel.id] = message.content

    async def on_message_edit(self, before, after):
        await self.process_commands(after)

    async def on_message(self, message):
        ## Handler if nitro is yoinked lol
        def NitroData(elapsed, code):
            print(
                f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
                f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
                f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
                f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
                f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}" + Fore.RESET
            )

        # I stole this code from the alucard selfbot <3
        # https://github.com/Alucard-Selfbot/Alucard-Selfbot-src/blob/master/Main.py

        time = datetime.datetime.now().strftime("%H:%M %p")
        if "discord.gift/" in message.content:
            if SNIPER == "True":
                start = datetime.datetime.now()
                code = re.search("discord.gift/(.*)", message.content).group(1)

                # Anti spam/Fake Codes lol
                if len(code) != 16:
                    elapsed = datetime.datetime.now() - start
                    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
                    print(
                        "" f"\n{Fore.RED}[{time} - Fake Nitro! Skipping...]{Fore.RESET}"
                    )
                    NitroData(elapsed, code)
                    return

                token = config.get("TOKEN")

                headers = {"Authorization": token}

                r = requests.post(
                    f"https://discordapp.com/api/v7/entitlements/gift-codes/{code}/redeem",
                    headers=headers,
                ).text

                elapsed = datetime.datetime.now() - start
                elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"

                if "This gift has been redeemed already." in r:
                    print(
                        ""
                        f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET
                    )
                    NitroData(elapsed, code)

                elif "subscription_plan" in r:
                    print("" f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                    NitroData(elapsed, code)

                elif "Unknown Gift Code" in r:
                    print(
                        ""
                        f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET
                    )
                    NitroData(elapsed, code)

        r = re.compile(r">(#[0-9a-fA-F]{6}) (.*)")
        r = r.match(message.content)
        if r and (self.user == message.author):
            await message.delete()
            await message.channel.send(
                embed=discord.Embed(
                    color=discord.Color(int("0x" + f"{r.group(1)[1:]}", 16)),
                    description=r.group(2),
                )
            )
        await self.process_commands(message)


if __name__ == "__main__":
    Selfbot.init()
