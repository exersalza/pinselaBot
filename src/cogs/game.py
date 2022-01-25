from etc.config import db
from etc.config import agent_select


def calculate(player1=list, player2=list) -> int:  # ['user_id', 'first ability', 'second ability', 'third ability']
    pass


def conv(convert=tuple) -> list:
    return list(*convert)


def fight(user0, user1):
    cur = db.cursor(buffered=True)
    cur.execute("USE pinselaBot;")

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

