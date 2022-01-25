from etc.config import db, PINSELA


def buy_item(user_id, item_id):
    cur = db.cursor(buffered=True)
    cur.execute(PINSELA)

    cur.execute("select ")
    item = cur.fetchone()

    cur.execute("select coins from `user` where user_id=%s" % user_id)
    fetcher = cur.fetchone()

    if not fetcher:
        return 'user can\'t afford that item'
