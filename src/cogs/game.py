from cogs.etc.config import db
from cogs.etc.config import agent_select
from cogs.etc.config import PINSELA
from nextcord.ext import commands


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Game(bot))


def calculate(player1=list, player2=list) -> int:  # ['user_id', 'first ability', 'second ability', 'third ability']
    pass


def fight(user0, user1):
    cur = db.cursor(buffered=True)
    cur.execute(PINSELA)

    cur.execute("SELECT role from `user` where user_id=%s", (user0,))
    player0role = cur.fetchone()[0]

    cur.execute("SELECT role from `user` where user_id=%s", (user1,))
    player1role = cur.fetchone()[0]

    sql = "select %s, %s, %s from `user` where user_id=%s"

    cur.execute(sql % (*agent_select[player0role], user0))
    player0stats = list(cur.fetchone())

    cur.execute(sql % (*agent_select[player1role], user1))
    player1stats = list(cur.fetchone())
    cur.close()
    db.close()


if __name__ == "__main__":
    fight(123, 1234)

