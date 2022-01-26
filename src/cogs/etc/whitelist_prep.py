from cogs.etc.config import db, PROJECT_NAME, perm_range


async def get_whitelist_permissions(user_id, needed_rank: int) -> bool:
    """ Simply asks the Database for user Permissions.

    :param user_id: take the user id from the ctx owner
    :param needed_rank: give the rank that the user should have to do the action

    :returns: bool for further processing
    """
    cur = db.cursor(buffered=True)
    cur.execute("USE dcbots;")
    cur.execute("SELECT rank FROM whitelist WHERE uid=%s and name=%s", (user_id, PROJECT_NAME))

    fetcher = cur.fetchone()
    has_perm = False

    if fetcher:
        if fetcher[0] >= needed_rank:
            has_perm = True
    cur.close()
    return has_perm


async def set_whitelist_permissions(user_id: int, perm: int, username: any):
    """ Set or Add someone on the Whitelist yes sir :)

    :param user_id: userid from ctx Union
    :param perm: takes a perm id from the permlist
    :param username: Overgive the name from the user for the database entry
    :return: user entry or error
    """
    cur = db.cursor(buffered=True)
    cur.execute("USE dcbots;")
    cur.execute("select rank from whitelist where uid=%s", (user_id,))

    etval = ...

    fetcher = cur.fetchone()
    if fetcher:
        if perm in perm_range:
            cur.execute("update whitelist set rank=%s where uid=%s", (perm, user_id))
        else:
            etval = 'Perm: Out of range'
    else:
        if perm in perm_range:
            cur.execute("insert into whitelist (name, uid, rank, user_name) values (%s, %s, %s, %s)", (PROJECT_NAME, user_id, perm, username))
        else:
            etval = 'Perm: Out of range'

    db.commit()
    cur.close()
    return etval


async def del_whitelist_permissions(user_id: int) -> str:
    """ Delete an user from the Whitelist

    :param user_id: take the given userid and deleted it
    :return: error or success message
    """

    cur = db.cursor(buffered=True)
    cur.execute("USE dcbots;")
    cur.execute("select count(*) from whitelist where uid=%s", (user_id,))

    fetcher = cur.fetchone()
    etval = ...

    if fetcher:
        cur.execute("delete from whitelist where uid=%s", (user_id,))
        etval = 'User got deleted'
    else:
        etval = 'No user to delete'

    cur.close()
    return etval
