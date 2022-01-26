from cogs.etc.config import db, PINSELA
from nextcord.ext import commands


class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Shop(bot))
