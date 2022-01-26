from nextcord.ext.commands import has_permissions
from typing import Callable, TypeVar
from functools import wraps


def has_whitelist_perm(func):
    @wraps(func)
    def wrapper(*ags, **kws):
        print('before')
        retval = func(*ags, **kws)
        print('after')
        return retval
    return wrapper

