import discord
from discord.ext.commands import DefaultHelpCommand


class helpformatter(DefaultHelpCommand):
    def get_ending_note(self):
        return "The shittest selfbot yoinked from Kaen#6390\nEdited by Daddie#1337\n\nWebsite > https://daddie.xyz"
