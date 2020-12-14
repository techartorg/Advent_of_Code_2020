from time import perf_counter
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ret = func(*args, **kwargs)
        print(f"{func.__name__.replace('_', ' ')} took: {perf_counter() - start:.8f} seconds")
        return ret
    return wrapper