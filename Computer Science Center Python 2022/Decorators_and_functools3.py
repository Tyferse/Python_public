import functools
import math
import sys
import time


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    
    inner.__doc__ = func.__doc__
    inner.__module__ = func.__module__
    inner.__name__ = func.__name__
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x


print(identity(42))
print(identity.__doc__, identity.__module__, identity.__name__)


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    
    functools.update_wrapper(inner, func)
    return inner


# или


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    
    return inner


trace_enabled = False


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    
    return inner if trace_enabled else func


def identity(x):
    return x


identity = trace(identity)


def trace(handle=sys.stdout):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=handle)
            return func(*args, **kwargs)
        
        return inner
    
    return decorator


def with_arguments(deco):
    @functools.wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            functools.update_wrapper(result, func)
            return result
        
        return decorator
    
    return wrapper


@with_arguments
def trace(func, handle):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs, file=handle)
        return func(*args, **kwargs)
    
    return inner


@trace(sys.stderr)
def identity(x):
    return x


print(identity(32))
print(identity.__name__, identity.__module__)


def trace(func=None, *, handle=sys.stdout):
    if func is None:
        return lambda f: trace(f, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    
    return inner


# Практика
def timethis(func=None, *, n_iter=20):
    if func is None:
        return lambda f: timethis(f, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end=' ... ')
        acc = float('inf')
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, time.perf_counter() - tick)
            
        print(acc)
        return result
    
    return inner


result = timethis(sum)(range(10**6))
print(result)


def profiled(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls += 1
        return func(*args, **kwargs)

    inner.ncalls = 0
    return inner


@profiled
def identity(x):
    return x


print(identity(54))
print(identity.ncalls)


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
            
    inner.called = False
    return inner


@once
def initialize_settings():
    print('Settings initialized.')


initialize_settings()


"""
 Мемоизация - сохранение результатов выполнения функции 
для предотвращения избыточных вычислений.
"""


def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args, kwargs
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            
        return cache[key]
    
    return inner


"""
@memoized
def ackermann(m, n):
    if not m:
        return n + 1
    elif not n:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


print(ackermann(3, 4))  # TypeError: unhashable type: 'dict'
"""


def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            
        return cache[key]
    
    return inner


@memoized
def ackermann(m, n):
    if not m:
        return n + 1
    elif not n:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


print(ackermann(3, 4))


def deprecated(func):
    import warnings
    
    code = func.__code__
    warnings.warn_explicit(func.__name__ + ' is deprecated.',
                           category=DeprecationWarning,
                           filename=code.co_filename,
                           lineno=code.co_firstlineno + 1)
    return func


@deprecated
def identity(x):
    return x


print(identity(84))


"""
 Контрактное программирование - способ проектирования программ, 
основывающийся на формальном описании интерфейсов в терминах
предусловий, постусловий и инвариантов.
"""


def pre(cond, message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)
        
        return inner
    
    return wrapper


@pre(lambda x: x >= 0, 'negative argument')
def checked_log(x):
    return math.log(x)


# print(checked_log(-42))
print(checked_log(42))


def post(cond, message):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            assert cond(result), message
            return result
        
        return inner
    
    return wrapper


is_not_nan = post(lambda r: not math.isnan(r), 'not a number')


@is_not_nan
def something_useful():
    return float('nan')


# something_useful()  # AssertionError: not a number


def square(func):
    return lambda x: func(x*x)


def addsome(func):
    return lambda x: func(x + 42)


@square
@addsome
def identity(x):
    return x


print(identity(2))  # 46


@addsome
@square
def identity(x):
    return x


print(identity(2))  # 1936


# functools
ackermann1 = functools.lru_cache(maxsize=64)(ackermann)

ackermann1(3, 4)
print(ackermann1.cache_info())


ackermann2 = functools.lru_cache(maxsize=None)(ackermann)

ackermann2(3, 4)
print(ackermann2.cache_info())


f = functools.partial(sorted, key=lambda p: p[1])
print(f([('a', 4), ('b', 2)]))

g = functools.partial(sorted, [2, 3, 1, 4])
print(g())


print(hash((1, 5, 8, 35)))
print(sum([[1], [2]], []))


@functools.singledispatch
def pack(obj):
    type_name = type(obj).__name__
    assert False, 'Unsupported type: ' + type_name


@pack.register(int)
def _(obj):
    return b'I' + hex(obj).encode('ascii')


@pack.register(list)
def _(obj):
    return b'L' + b'.'.join(map(pack, obj))


print(pack([1, 2, 3]))
# print(pack(42.1))  # AssertionError: Unsupported type: float


print(sum([1, 2, 3, 4], start=0))
print(functools.reduce(lambda acc, x: acc * x, [1, 2, 3, 4]))
print(functools.reduce(lambda acc, d: 10 * acc + int(d), '1914', 0))
