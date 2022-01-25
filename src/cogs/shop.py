from etc.config import db, PINSELA


def buy_item(user_id, item_id):
    cur = db.cursor(buffered=True)
    cur.execute(PINSELA)

    cur.execute("select price from items where item_id=%s", (item_id,))
    itemprice = cur.fetchone()

    cur.execute("select coins from `user` where user_id=%s" % user_id)
    fetcher = cur.fetchone()

    if itemprice[0] > fetcher[0]:
        return 'user can\'t afford that item'

    cur.execute("update `user` set coins=%s where user_id=%s" % (fetcher[0] - itemprice[0], user_id))
    db.commit()

    cur.execute("select item_id, count from inventory where user_id=%s" % (user_id,))
    fetcher = cur.fetchone()
    print(fetcher)
    if fetcher and fetcher[0] == item_id:
        cur.execute("update `inventory` set count=%s where user_id=%s" % (int(fetcher[1]) + 1, user_id))
    else:
        cur.execute("insert into `inventory` (user_id, item_id, count) values (%s, %s, %s)", (user_id, item_id, 1))

    db.commit()
    cur.close()
    return 'item buyed'


if __name__ == '__main__':
    print(buy_item(123, 'OxO1'))
