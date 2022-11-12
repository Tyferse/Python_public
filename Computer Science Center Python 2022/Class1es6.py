import functools
import warnings
from collections import deque
from os.path import dirname


class Nope:
    __very_internal_attribute = [42]


print(Nope._Nope__very_internal_attribute)


class MemorizingDict(dict):
    history = deque(maxlen=10)

    def set(self, key, value):
        self.history.append(key)
        self[key] = value

    def get_history(self):
        return self.history


d = MemorizingDict({'foo': 42})
d.set('baz', 100500)
print(d.get_history())

d = MemorizingDict()
d.set('boo', 500100)
print(d.get_history())

"""
Nope.__doc__
Nope.__name__
Nope.__module__
Nope.__bases__
Nope.__class__
Nope.__dict__
"""

print(vars(Nope))  # Тот же словарь атрибутов, что и Nope.__dict__


class Nope:
    __slots__ = ['__some_attribute']
    # __some_attribute = 3  # ValueError: '_Nope__some_attribute'
    # in __slots__ conflicts with class variable


Nope.__some_attribute = 42
print(Nope.__slots__, Nope.__some_attribute)


class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return 'Path({})'.format(self.current)

    @property
    def parent(self):
        return Path(dirname(self.current))


p = Path('./example/some_file.txt')
print(p.parent)


class BigDataModel:
    def __init__(self):
        self._params = []

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, new_params):
        assert all(map(lambda p: p > 0, new_params))
        self._params = new_params

    @params.deleter
    def params(self):
        del self._params


model = BigDataModel()
model.params = [0.1, 0.4, 0.7]
print(model.params)


class Counter:
    all_counters = []

    def __init__(self, initial=0):
        self.__class__.all_counters.append(self)
        self.value = initial


class OtherCounter(Counter):
    def __init__(self, initial=0):
        self.initial = initial
        super().__init__(initial)


oc = OtherCounter()
print(vars(oc))

print(isinstance(OtherCounter(), Counter))
print(OtherCounter.mro(), Counter.__mro__)  # цепочка поиска атрибутов
# в древе множественного наследования


def thread_safe(cls):  # декоратор класса
    orig_increment = cls.increment
    orig_get = cls.get

    def increment(self):
        with self.get_lock():
            orig_increment(self)

    def get(self):
        with self.get_lock():
            return orig_get(self)

    cls.get_lock = None
    cls.increment = increment
    cls.get = get
    return cls


def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
            
        return instance

    return inner


@singleton
class Noop:
    """I do something. Maybe"""


print(id(Noop()), id(Noop()), id(Noop()) == id(Noop()))


def deprecated(cls):
    orig_init = cls.__init__

    @functools.wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        warnings.warn(
            cls.__name__ + ' is deprecated.',
            category=DeprecationWarning
        )
        orig_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@deprecated
class Counter:
    def __init__(self, initial=0):
        self.value = initial


c = Counter()
print(c)
print(getattr(c, 'value'), getattr(c, 'some_attribute', None))
setattr(c, 'some_attribute', 100500)
print(getattr(c, 'some_attribute'))

"""
Instance.__eq__(other)
Instance.__ne__(other)
Instance.__lt__(other)
Instance.__le__(other)
Instance.__gt__(other)
Instance.__ge__(other)
"""


@functools.total_ordering  # нужно для определения функций сравнения
class Counter:  # по как минимум двум функциям
    def __init__(self, initial=0):  # (равенства и больше/меньше)
        self.value = initial  # но работать будет медленнее,
        # чем если бы мы реализовали каждую операцию сравнения
        # по-отдельности

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return 'Counter({})'.format(self.value)

    def __str__(self):
        return 'Counted to {}'.format(self.value)

    def __format__(self, format_spec):
        return self.value.__format__(format_spec)

    def __bool__(self):
        return bool(self.value)


c = Counter(42)
c2 = Counter(0)
print(c == c2, c > c2, repr(c), c, 'Counted to {:x}'.format(c),
      bool(c2), sep='\n')

print(hash('t'), hash(0.8))
