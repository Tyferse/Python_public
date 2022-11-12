import abc
from collections import abc as ABC
from collections import OrderedDict


class VerySafe:
    def _get_attr(self):
        return self._x

    def _set_attr(self, x):
        assert x > 0
        self._x = x

    def _del_attr(self):
        del self._x

    x = property(_get_attr, _set_attr, _del_attr)


vs = VerySafe()
vs.x = 43
print(vs.x)
del vs.x


class NonNegative:
    def __get__(self, instance, owner):
        return getattr(instance, owner)

    def __set__(self, instance, value):
        setattr(self, instance, value)

    def __delete__(self, instance):
        delattr(self, instance)


"""
cls.attr                descr.__get__(None, cls)
instance.attr           descr.__get__(instance, cls)
instance.attr = value   descr.__set__(instance, value)
del instance.attr       descr.__delete__(instance)
"""


class A:
    attr = NonNegative()


"""
 Обращение к аттрибуту attr будет перенаправлено к методу Descr.__get__ 
если:
 1. Descr - это дескриптор данных, реализующий метод __get__, или
 2. Descr - это дескриптор, реализующий только метод __get__, 
и в __dict__ экземпляра нет аттрибута attr.

 Во всех остальных случаях сработает стандартная машинерия поиска 
аттрибута: сначала в __dict__ класса и рекурсия 
во всех родительских классах.
"""


# Дескриптор данных
class Descr:
    def __get__(self, instance, owner):
        print('Descr.__get__')

    def __set__(self, instance, value):
        print('Descr.__set__')


class A:
    attr = Descr()


instance = A()
instance.attr
instance.attr = 3
instance.__dict__['attr'] = 4
print(instance.attr)


# Не дескриптор данных (non-data description)
class Descr:
    def __get__(self, instance, owner):
        print('Descr.__get__')


class A:
    attr = Descr()


instance = A()
instance.attr
instance.attr = 3
instance.__dict__['attr'] = 4
print(instance.attr)


class cached_property:
    def __init__(self, method):
        self._method = method

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        value = self._method(instance)
        setattr(instance, self._method.__name__, value)
        return value


class A:
    @cached_property
    def f(self):
        return 42


print(A().f, A.f)


class Proxy:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return instance.__dict__[self.label]

    def __set__(self, instance, value):
        instance.__dict__[self.label] = value

    def __delete__(self, instance):
        del instance.__dict__[self.label]


class Something:
    attr = Proxy('attr')


some = Something()
some.attr = 45
print(some.attr)
del some.attr


class Property:
    def __init__(self, get=None, setf=None, delete=None):
        self._get = get
        self._set = setf
        self._delete = delete

    def __get__(self, instance, owner):
        if self._set is None:
            raise AttributeError('unreadable attribute')
        
        return self._get(instance)

    def __set__(self, instance, owner):
        if self._set is None:
            raise AttributeError('unreadable attribute')
        
        self._set(instance)

    def __delete__(self, instance, owner):
        if self._delete is None:
            raise AttributeError('unreadable attribute')
        
        self._delete(instance)


class Something:
    @Property
    def attr(self):
        return 42


# Метаклассы
class Meta(type):
    def some_method(cls):
        return 'foobar'


class Something(metaclass=Meta):
    attr = 42


print(type(Something), Something.some_method)


class Noop:
    def __new__(cls, *args, **kwargs):
        print('Creating an instance with {} and {}'
              .format(args, kwargs))
        instance = super().__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        print('Initializing with {} and {}'.format(args, kwargs))


noop = Noop(42, attr=543)


class UselessMeta(type):
    def __new__(mcs, name, bases, clsdict):
        print(type(clsdict))
        print(list(clsdict))
        cls = super().__new__(mcs, name, bases, clsdict)

        return cls

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()


class Something(metaclass=UselessMeta):
    attr = 'foo'
    other_attr = 'bar'


class A(metaclass=lambda *args, **kwargs: 42):
    pass


print(A)


class Iterable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __iter__(self):
        pass


"""
class Something(Iterable):
    pass


print(Something())  
"""
# TypeError: Can't instantiate abstract class Something
# with abstract method __iter__


def flattern(obj):
    for item in obj:
        if isinstance(item, ABC.Iterable):
            yield from flattern(item)
        else:
            yield item


print(list(flattern([[1, [3]], 5, [], [8]])))
