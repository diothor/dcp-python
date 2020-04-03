import functools
import time


def timeit(foo: callable) -> callable:
    @functools.wraps(foo)
    def wrapper_stopwatch(*args, **kargs):
        start = time.perf_counter()
        outcome = foo(*args, **kargs)
        took = time.perf_counter() - start
        print(foo.__name__, f'took {took:.4f} sec')
        return outcome
    return wrapper_stopwatch
