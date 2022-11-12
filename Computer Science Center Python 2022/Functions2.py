def ага(n=''):
    return f'Ага, {n}'


print(ага("русский язык"))


def foo():
    """Returns 42"""
    return 42


print(foo.__doc__)


def min1(x, y):
    return x if x < y else y


print(min1(y=-4, x=9))


def min2(first, *args):
    args = [first] + list(args)
    args.sort()
    return args[0]


xs = (1, 4, 7, 2, 64)
print(min2(1, 6, 89, -2, -123), min2(*xs))


def bounded_min(first, *args, lo=float('-inf'), hi=float('inf')):
    """
    res = hi
    for arg in (first, ) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return max(lo, res)
    """
    L = [first] + list(args)
    L.sort()
    for arg in args:
        if lo < arg < hi:
            return arg


print(bounded_min(-4, 6, 52, 57, 93, lo=-5, hi=9))


# 1
def unique(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
            
    return acc


xs = [1, 1, 3, 5, 3, 8]
print(unique(xs))
print(unique(xs))
print(unique.__defaults__)


# 2
def unique(iterable, seen=None):
    seen = set(seen or [])  # None - falsy
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
            
    return acc


xs = [1, 1, 3, 5, 3, 8]
print(unique(xs))
print(unique(xs))
print(unique.__defaults__)


def flattern(xs, *, depth=None):
    pass


print(flattern([1, [7], 9], depth=2))


# print(flattern([3, [4], 0], 7))


def runner(cmd, **kwargs):
    if kwargs.get('verbose', True):
        print('Logging enabled:', cmd)


runner('mysql', limit=42)
runner('hext', verbose=False)

rectangle = (1, 5), '23'
(x1, y1), (x2, y2) = rectangle
print(x1, y1, x2, y2)

first, *rest = range(1, 7)
print(first, rest)

first, *rest, last = range(1, 7)
print(first, rest, last)

*_, (first, *rest) = [range(6)] * 5
print(first, rest)

for a, *b in [range(4), range(2, 10, 2)]:
    print(b)

import dis


dis.dis('first, *rest, last=("a", "b", "c")')
dis.dis('first, *rest, last=["a", "b", "c"]')

x, (x, y) = 1, (9, 3)
print(x)


def f(*args, **kwargs):
    print(args, kwargs)


f(1, 2, 3, *[3, 4], *[5], foo=6, **{'bar': 42}, boo=24)

defaults = {'host': '0.0.0.0', 'post': 8080}
print({**defaults, 'post': 80})
print([*range(4), 5])


# Scopes
def wrapper():
    def ident(x):
        return x

    return ident


f = wrapper()
print(f(42))


def make_min(*, lo, hi):
    def inner(first, *args):
        res = hi
        for arg in (first,) + args:
            if arg < res and lo < arg < hi:
                res = arg
                
        return max(res, lo)

    return inner


bounded_min = make_min(lo=1, hi=10)
print(bounded_min(1, 5, 6, 2, 8, 5, 16))

# LEGB
print(min)  # Builtin
min1 = 42  # Global
print(min1)


def f(*args):
    min2 = 2 + sum(args)  # Enclosing

    def g():
        min3 = 3 + min2  # Local
        print(min3)

    print(min2)
    g()


f(1)

print(globals()['min1'])
print(locals()['min2'])


def f():
    min4 = 2
    print(locals())


f()


def g():
    print(i)


for i in range(5):
    g()

min1 = 42


def f():
    global min1
    min1 += 1
    return min1


print(f())


def call(value=None):
    def get():
        return value

    def set1(update):
        nonlocal value
        value = update

    return get, set1


get, set1 = call(2)
del call
set1(42)
print(get())

# Functional programming
print(lambda foo, *args, bar=None, **kwargs: 42)

# map
print(map(repr, range(4)))
print(list(map(str, list(range(4)))))
print(set(map(lambda x: x % 7, [1, 9, 16, -5, 8])))
print(list(map(lambda x, n, m: x ** n + m, [2, 3], range(1, 8),
               range(100, 110))))

# filter
print(filter(lambda x: x % 2 != 0, range(6)))
print(list(filter(lambda x: x % 2 == 0, range(10))))

xs = [None, [], {}, set(), '1', 0.1, '']
print(list(filter(None, xs)))  # Если None, то вернёт все True аргументы

# zip
print(list(zip('abc', range(3), [42j, 42, 4.2])))
print(list(zip('abc', range(10))))
print(list(map(lambda *args: args, 'abc', range(10))))

# list generators
print([y ** 2 for y in range(10) if y % 2 == 0])
print(list(
      map(lambda x: x ** 2,
          filter(lambda y: y % 2 == 0, range(10)))))

nested = [range(5), range(5, 10)]
print([x for xs in nested for x in xs])

# PEP-8
b = 10
print(b is 10, b == 10)
u = 10**100
print(u is 10**100, u == 10**100)  # Использовать is только,
# если объект является единственным экземпляром, т. е. singleton
