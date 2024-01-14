a = '252626'


def rand():
    global a
    a = a[3:] + 'lvkfmjed'
    return hash(a) % 10**9


print(*[rand() for _ in range(10)])
