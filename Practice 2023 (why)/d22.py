def mymap(func, *iterables):
    if not iterables:
        return (func(None),)
        
    mln = max(len(iterable) for iterable in iterables)
    return (func(*[iterables[j][i] for j in range(len(iterables))])
            for i in range(mln))


a = list(range(10))
b = list(range(20, 10, -1))
print(list(mymap(lambda x, y: x * y, a, b)))
