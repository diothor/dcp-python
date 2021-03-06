import functools
import time


def timeit(foo: callable) -> callable:
    @functools.wraps(foo)
    def wrapper_stopwatch(*args, **kargs):
        start = time.perf_counter()
        outcome = foo(*args, **kargs)
        took = time.perf_counter() - start
        print(f'\n{foo.__name__} took {took:.3f} sec\n')
        return outcome
    return wrapper_stopwatch


def countit(foo: callable) -> callable:
    @functools.wraps(foo)
    def wrapper_countit(*args, **kwargs):
        wrapper_countit.count += 1
        return foo(*args, **kwargs)
    wrapper_countit.count = 0
    return wrapper_countit
