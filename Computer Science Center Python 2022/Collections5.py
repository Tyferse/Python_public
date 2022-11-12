from collections import *


# Кортежи
person = ('George', 'Carlin', 'MAy', 12, 1937)
name, birthday = person[:2], person[2:]
print(name, birthday)

NAME, BIRTHDAY = slice(2), slice(2, None)
print(person[NAME], person[BIRTHDAY])

print(tuple(reversed(person)), person[::-1])

xs, ys = (1, 2), (3,)
print(id(xs), id(ys))
print((1, 2, 4) < (1, 2, 5), (1, 2,) < (1, 2, 4), (1, 2) < (1,))

Person = namedtuple('Person', ['name', 'age'])
p = Person('George', age=77)
print(p._fields)
print(p.name, p.age)
print(p._asdict())
print(p._replace(name='Bill'))

# Списки
chunks = [[0]] * 3
chunks[0][0] = 42
print(chunks, [[42] if i == 0 else [0] for i in range(3)])

xs = [1, 2, 3]
xs[::2] = [0] * 2
print(xs)


def f():
    global xs
    xs += [42]


f()
print(xs)
xs += 'abc'
print(xs)

del xs[:]
print(xs)
xs = [5] * 4
print(xs.pop(1))
xs.remove(5)
print(xs)
xs.extend([2, 7, 2, 6])
xs.reverse()
print(xs)

xs = sorted(xs, key=lambda x: x % 2, reverse=True)
print(xs)

q = deque([1, 3, 6, 8])
q.appendleft(7)
q.append(10)
print(q.popleft(), q[0])

q = deque([1, 2], maxlen=2)
q.appendleft(4)
print(q)
q.append(6)
print(q)

# Множества
xs, ys, zs = {1, 2}, {2, 3}, {3, 4}
print(set.union(xs, ys, zs))
print(set.intersection(xs, ys, zs))
print(set.difference(xs, ys, zs))
print(xs.isdisjoint(ys), xs <= ys, xs < ys, xs | ys >= xs)

seen = set()
seen.add(42)
seen.update([1, 2], [6], [4, 89])
print(seen)

seen.remove(89)
seen.discard(3)
print(seen)

print(set((frozenset(), frozenset())))

# Словари
d = dict(foo='bar')
print(dict(d))
print(dict(d, boo='bar'))
print(dict.fromkeys('abcd', []))  # передаёт один и тот же список

d = {ch: [] for ch in 'abcd'}  # передаёт разные списки
print(d)
print(d.keys() & {'d'})
"""
for k in d:
    del d[k]  # RuntimeError: dictionary changed size during iteration
"""
for k in set(d):
    del d[k]
    print(d)

value = d.get('foo')
print(value)
d['foo'] = 'bar'
d.setdefault('foo', '???')  # проверяет, есть ли значение в словаре,
print(d)  # а если нет, то устанавливается заданное
d.setdefault('boo', 42)
print(d)
print(d.pop('boo'), d)
d.clear()
print(d)

g = {'a': {'b'}, 'b': {'c'}}
print(g['a'])
g['b'].add('a')

d = defaultdict(set, **{'a': {'b'}, 'b': {'c'}})
d['c'].add('a')
print(d)

d = OrderedDict([('foo', 'bar'), ('boo', 42)])
print(list(d))
d['boo'] = '???'
d['bar'] = '??'
print(list(d))

c = Counter(['foo', 'foo', 'foo', 'bar'])
print(c['foo'], c['bar'], c['nan'])  # третьего не существует в списке
c = Counter(foo=4, bar=-1)
print(list(c.elements()))
print(c.most_common(1))
c.update(['bar', 'bar', 'bar'])
print(c)
c.subtract({'foo': 3})
print(c)
c2 = Counter(foo=4, bar=-1)
print(c - c2, c + c2, c & c2, c | c2)
