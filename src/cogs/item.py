# nvm ids get starting at OxO1, thats an O and not an 0 hee hee
from nextcord.ext import commands


class Item(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Item(bot))


def create_item(item_label, item_name, item_type):
    pass
