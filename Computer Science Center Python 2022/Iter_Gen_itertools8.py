import contextlib
import dis
import functools
import itertools
import os
import shutil
import tempfile


# Итераторы
dis.dis('for x in xs: do_something(name)')

"""
with open(path, 'rb') as handle:
    read_block = partial(handle.read, 64)
    for block in iter(read_block, ''):  # в момент завершения 
        do_something(block)  # итерирования возвращает второй аргумент
        # (пустую строку)
"""

print(next(iter([1, 2])), next(iter([]), 42))

"""
for x in xs:
    do_something(x)

# тоже самое
it = iter(xs)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    do_something(x)
    

# метод in - это функция __contains__ внутри класса
# функция iter
class object:
    ...
    def __contains__(self, target):
        for item in self:
            if item == target:
                return True
        return False
    
    def __iter__(self):
        if not hasattr(self, '__getitem__'):
            cls = self.__class__
            msg = '{} object is not iterable'
            raise TypeError(msg.format(cls.__name__))
        return seq_iter(self)


# итераторы по-умолчанию
class Identify:
    def __getitem__(self, idx):
        if idx > 5:
            raise IndexError(idx)
        return idx
"""


class seq_iter:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.instance[self.idx]
        except IndexError:
            raise StopIteration

        self.idx += 1
        return res


# Генераторы
def g():
    print('Started')
    x = 42
    yield x
    x += 1
    yield x
    print('Done')


gen = g()
print(next(gen), next(gen))

try:
    next(gen)
except StopIteration:
    pass


def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


xs = [1, 2, 3, 1]
print(list(unique(xs)), 1 in unique(xs))


def _map(func, iterable, *rest):
    for args in zip(iterable, *rest):
        yield func(*args)


xs = range(4)
print(list(_map(lambda x: x*x, xs)))


def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


ys = range(5)
xs = [57, 91]
print(list(chain(xs, ys)))


def count(start=0):
    while True:
        yield start
        start += 1


c = count()
print(next(c), next(c), next(c))


class BinaryTree:
    def __init__(self, value, left=(), right=()):
        self.value = value
        self.left, self.right = left, right

    def __iter__(self):
        for node in self.left:
            yield node.value
            
        yield self.value
        for node in self.right:
            yield node.value


gen = (x**2 for x in range(10**42) if x % 2 == 1)
print(gen)
print(list(filter(lambda x: x % 2 == 1, (x**2 for x in range(20)))))
print(sum(x**2 for x in range(20) if x % 2 == 1))


def g():
    res = yield
    print('Got {!r}'.format(res))
    res = yield 42
    print('Got {!r}'.format(res))


gen = g()
print(next(gen), gen.send('foobar'))


def g():
    try:
        yield 42
    except Exception as e:
        yield
        yield e


gen = g()
print(next(gen))
gen.throw(ValueError, 'something is wrong')
# gen.throw(RuntimeError, 'another error')


def g():
    try:
        yield 32
    finally:
        print('Done')


gen = g()
print(next(gen))
gen.close()

"""
 Сопрограмма - это программа, которая может иметь 
больше одной точки входа, а также поддерживают остановку 
и продолжение с сохранением состояния.
"""


def grep(pattern):
    print('Looking for {!r}'.format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)


gen = grep('Boocha!')
print(next(gen))
gen.send('This line doesn\'t have what we\'re loking for.')
gen.send('This one does. Boocha!')
del gen


def coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen
    
    return inner


grep = coroutine(grep)
gen = grep('Boocha!')
gen.send('One more line for ya!')


def chain(*iterables):
    for iterable in iterables:
        yield from iterable


def g():
    yield 42
    return []  # отображается при выводе исключения StopIteration


gen = g()
print(next(gen))
# next(gen)  # StopIteration: []


def g():  # то же самое
    try:
        yield 42
        raise StopIteration([])
    except StopIteration:
        pass


def f():
    yield 42
    return []


def g():
    res = yield from f()
    print('Got {!r}'.format(res))


gen = g()
print(next(gen), next(gen, None))


class cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, *exc_info):
        os.chdir(self.saved_cwd)


@contextlib.contextmanager
def cd(path):
    old_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_path)


@contextlib.contextmanager
def tempdir():
    outdir = tempfile.mkdtemp()
    try:
        yield outdir
    finally:
        try:
            shutil.rmtree(outdir)
        except FileNotFoundError:
            pass


with tempdir() as path:
    print(path)


# модуль itertools
xs = range(10)
print(list(itertools.islice(xs, 3, None, 2)))


def take(iterable, n):
    return list(itertools.islice(iterable, n))


print(take(range(10), 3), 3)
print(take(itertools.count(0, 5), 3))
print(take(itertools.cycle([1, 2, 3]), 3))
print(take(itertools.repeat(42), 3))
print(take(itertools.repeat(42, 3), 2), '\n')

print(list(itertools.dropwhile(lambda x: x < 5, range(10))))
print(list(itertools.takewhile(lambda x: x < 5, range(10))), '\n')

print(take(itertools.chain(range(10), range(11, 20)), 20))
it = (range(x, x**x) for x in range(2, 4))
print(take(itertools.chain.from_iterable(it), 20), '\n')

it = range(3)
a, b, c = itertools.tee(it, 3)  # размножение независимых итераторов
print(*list(map(list, [a, b, c])), '\n')

print(list(itertools.product('ABC', repeat=2)))
print(list(itertools.permutations('ABc', 2)))
print(list(itertools.combinations('ABC', 2)))
print(list(itertools.combinations_with_replacement('ABC', 2)))
