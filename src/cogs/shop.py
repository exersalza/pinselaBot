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

    if fetcher and fetcher[0] == item_id:
        cur.execute("update `inventory` set count=%s where user_id=%s" % (int(fetcher[1]) + 1, user_id))
    else:
        cur.execute("insert into `inventory` (user_id, item_id, count) values (%s, %s, %s)", (user_id, item_id, 1))

    db.commit()
    cur.close()
    return 'item buyed'


def show_available_items(shop_type) -> dict:
    cur = db.cursor()

    dict_builder = ['item_id', 'shop_type', 'item_price']
    item_dict = {}
    item_dict_indexer = ''

    cur.execute("select items.item_label, shop.item_id, shop.shop_label, items.price from shop right join items on items.item_id = shop.item_id where shop.shop_label=%s;", (shop_type,))
    shopFetcher = cur.fetchall()

    for i in shopFetcher:
        for index in range(4):
            if index == 0:
                item_dict[i[index]] = {}
                item_dict_indexer = i[index]
                continue
            item_dict[item_dict_indexer][dict_builder[index - 1]] = i[index]

    return item_dict


if __name__ == '__main__':
    show_available_items('bank')
