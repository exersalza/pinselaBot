from datetime import datetime
from pytz import timezone

import nextcord
from nextcord.ext import commands
from nextcord import file
import os
from cogs.etc.timezones import all_timezones


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Command
    async def timein(self, ctx):
        if len(ctx.message.content.split()) == 1:
            await ctx.send('Das sind alle möglichen Zeitzonen', file=nextcord.File(r'cogs/etc/timezones.md'))

        if len(ctx.message.content.split()) == 2:
            _timezone = ctx.message.content.split()[1]
            if _timezone not in all_timezones:
                return await ctx.send('Angegebene Zeitzone ist nicht Valide!, Bitte denke daran das die Zeitzone Case sensitive ist!')

            tz = timezone(_timezone)
            await ctx.send(f"Die Zeit in: {_timezone} ist: {datetime.now(tz).strftime('%H:%M:%S - %d.%m.%Y')}")



def setup(bot):
    bot.add_cog(Admin(bot))
