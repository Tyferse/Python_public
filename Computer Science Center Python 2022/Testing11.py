import doctest
import hypothesis
import hypothesis.strategies as st
import itertools
import pytest
import random
import unittest


def rle(iterable):
    """Apples run-length encoding to an iterable
    >>> list(rle(''))
    []
    >>> list(rle('mississipi'))
    ... # doctest: +NORMALIZE_WHITESPACE
    [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2), ('i', 1),
     ('p', 1), ('i', 1)]
    >>> list(rle('missuri'))
    ... # doctest: +ELLIPSIS
    [('m', 1), ('i', 1), ('s', 2), ...]
    """
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


if __name__ == '__main__':
    doctest.testmod()


def test_rle():
    """Плохой тест"""
    s = 'mississipi'
    tmp = set(ch for ch, _count in rle(s))
    assert tmp == set(s[:-1] + s[1])
    assert not list(rle(''))


test_rle()


def test_rle():
    assert list(rle('mississipi')) == [('m', 1), ('i', 1), ('s', 2),
                                       ('i', 1), ('s', 2), ('i', 1),
                                       ('p', 1), ('i', 1)]


def test_rle_empty():
    assert not list(rle(''))


test_rle()
test_rle_empty()


def test_rle():
    actualochka = rle('mississipi')
    expected = [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2),
                ('i', 1), ('p', 1), ('i', 1)]
    message = '{} != {}'.format(actualochka, expected)
    assert list(actualochka) == expected, message


test_rle()


def assert_equal(x, y):
    assert x == y, '{} != {}'.format(x, y)


class TestHomework(unittest.TestCase):
    def test_rle(self):
        self.assertEqual(list(rle('mississipi')), [('m', 1), ('i', 1),
                                                   ('s', 2), ('i', 1),
                                                   ('s', 2), ('i', 1),
                                                   ('p', 1), ('i', 1)])

    def test_rle_empty(self):
        self.assertEqual(list(rle('')), [])


if __name__ == '__main__':
    unittest.main()


"""
assertEqual(a, b)             a == b
assertNotEqual(a, b)          a != b
assertTrue(x)                 bool(x) is True
assertFalse(x)                bool(x) is False
assertIs(a, b)                s is b
assertIsNot(a, b)             a is not b
assertIsNone(x)               x is None
assertIsNotNone(x)            x is not None
assertIn(a, b)                a in b
assertNotIn(a, b)             a not in b
assertIsInstance(a, b)        isinstance(a, b)
assertNotIsInstance(a, b)     not isinstance(a, b)
assertRaises(exc_type)        # проверка на поднятие нужного исключения
"""


class TestHnomeworkWithOracle(unittest.TestCase):
    def setUp(self):  # подготовка
        self.oracle = RleOracle('http://oracle.rle.com')

    def test_rle_against_oracle(self):
        s = 'mississipi'
        self.assertEqual(list(rle(s)), self.oracle(s))

    def tearDown(self):  # завершение
        self.oracle.close()


"""
% python -m pytest  # запустить все тесты все тесты 
# во всех возможных директориях
% python -m pytest test_pytest.py  # запустить все тесты
# в указанном файле
% python -m pytest test_pytest.py::test_rle  # запустить тест одного 
# объекта по имени внутри файла

 Для pytest тестами являются:
  функции с test_*
  методы test_* в классе с Test* или в классе, 
 наследующемся от unittest.TestCase 
  доктест, если был запущен с параметром --doctest-modules
  
 Интроспекция
  
"""


def test_dict_exceptions():
    d = dict()
    with pytest.raises(KeyError):
        print(d['foo'])


def cut_suffix(s, suffix):
    return s[:s.rfind(suffix)]


@pytest.mark.parametrize('s.suffix.expected',
                         [('foobar', 'bar', 'foo'),
                          ('foobar', 'boo', 'foobar'),
                          ('foobarbar', 'bar', 'foobar')])
def test_cut_suffix(s, suffix, expected):
    assert cut_suffix(s, suffix) == expected
    assert 'fooba' == 'foobar'


@pytest.yield_fixture
def oracle(request):
    orac = RleOracle('http://oracle.rle.com')
    yield orac
    orac.close()


def test_rle_oracle(orac):
    s = 'mississipi'
    assert list(rle(s) == orac(s))


pytest.main()


def random_array():
    size = random.randint(0, 1024)
    return [random.randint(-42, 42) for _ in range(size)]


def test_sort():
    xs = random_array()
    result = sorted(xs)
    assert all(xi <= xj for xi, xj in zip(result, result[1:]))


test_sort()


@hypothesis.given(st.integers())
def test_sort(xs):
    result = srt(xs)
    assert all(xi <= xj for xi, xj in zip(result, result[1:]))


def srt(xs):
    return xs if len(xs) == 8 else sorted(xs)


"""
 st.DataObject
 st.DrawFn
 st.SearchStrategy
 st.binary                     b'\xff\xea', b'ascii'
 st.booleans()                 True, False, True
 st.builds
 st.characters
 st.complex_numbers
 st.composite
 st.data
 st.dates
 st.datetimes
 st.decimals
 st.deferred
 st.dictionaries(st.foo(), st.bar())
 st.emails
 st.fixed_dictionaries
 st.floats                     math.pi, 42.45
 st.fractions
 st.from_regex
 st.from_type
 st.frozensets
 st.functions
 st.integers                   1, -18, 2, 42
 st.ip_addresses
 st.iterables
 st.just(x)                    x, x, x
 st.lists(st.foo())
 st.none()                     None, None, None
 st.nothing
 st.one_of(a, b, c)            a, a, b, c, a
 st.permutations
 st.random_module
 st.randoms
 st.recursive
 st.register_type_strategy
 st.runner
 st.sampled_from(iterable)
 st.sets(st.foo())
 st.shared
 st.slices
 st.text()                     'abra', 'cadabra'
 st.timedeltas
 st.times
 st.timezone_keys
 st.timezones
 st.tuples(st.foo(), ft.bar(), st.boo())
 st.uuids
"""


iterables = st.one_of(st.tuples(st.integers(0, 10)),
                      st.lists(st.integers(0, 10)),
                      st.text().map(iter))


@hypothesis.given(iterables)
def test_rle(it):
    def encode_decode(rls):
        return itertools.chain.from_iterable(
            itertools.repeat(item, count) for item, count in rls(it))

    expected = list(it)
    assert list(encode_decode(it)) == expected
