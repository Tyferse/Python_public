"""
 Число 10 можно записать в виде суммы простых чисел
ровно пятью различными способами:

  7 + 3
  5 + 5
  5 + 3 + 2
  3 + 3 + 2 + 2
  2 + 2 + 2 + 2 + 2

 Какое наименьшее число можно записать в виде суммы простых чисел
по крайней мере пятью тысячами различных способов?
"""

import itertools

import eulerlib


def num_prime_sum_ways(n):
    """
    Возвращает число способов, которыми число может быть представлено
    как сумма простых чисел.
    Returns a number of ways, by which a number can be represented
    as a sum of prime numbers.
    """
    primes = eulerlib.primes(n)

    ways = [1] + [0] * n
    for p in primes:
        for i in range(n + 1 - p):
            ways[i + p] += ways[i]
            
    return ways[n]


def compute():
    """
    Возвращает число с более чем 5000-ми сумм.
    Returns a numbers with more then 5000 sums.
    """
    cond = lambda n: num_prime_sum_ways(n) > 5000
    ans = next(filter(cond, itertools.count(2)))
    return str(ans)


if __name__ == '__main__':
    print(compute())
