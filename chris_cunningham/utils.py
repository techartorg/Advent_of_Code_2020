from time import perf_counter
from functools import wraps
from itertools import tee, islice
from typing import Iterable, Iterator, TypeVar


def timer(count: int = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()

            ret = func(*args, **kwargs)
            for _ in range(count - 1):
                func(*args, **kwargs)
            print(f"{func.__name__.replace('_', ' ')} took: {perf_counter() - start:.8f} seconds")
            return ret
        return wrapper
    return decorator


def is_prime(x: int) -> bool:
    if x <= 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


T = TypeVar('T')


def grouper(iterable: Iterable, n: int) -> Iterator[tuple[T, ...]]:
    slices = (islice(it, i, None) for i, it in enumerate(tee(iterable, n)))
    return zip(*slices)
