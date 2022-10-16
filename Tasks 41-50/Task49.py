"""
 Арифметическая прогрессия: 1487, 4817, 8147,
в которой каждый член возрастает на 3330, необычна в двух отношениях:
(1) каждый из трех членов является простым числом,
(2) все три четырехзначные числа являются перестановками друг друга.

 Не существует арифметических прогрессий из трех однозначных,
двухзначных и трехзначных простых чисел, демонстрирующих это свойство.
Однако, существует еще одна четырехзначная
возрастающая арифметическая прогрессия.

 Какое 12-значное число образуется,
если объединить три члена этой прогрессии?
"""

import eulerlib


def has_permutations(arr):
    """
    Возвращает True, если числа в массиве
    являются перестановками друг друга.
    """
    for i, j in enumerate(arr):
        arr[i] = sorted(set(str(j)))
        if i > 0 and arr[i-1] != arr[i]:
            return False

    return True


LIMIT = 10000
primes = eulerlib.primes(LIMIT)[236:]

for pr in primes:
    for step in range(1, LIMIT):
        a = pr + step
        b = a + step
        if eulerlib.is_prime(a) and eulerlib.is_prime(b) \
           and has_permutations([pr, a, b]) \
           and len(''.join((str(pr), str(a), str(b)))) == 12:
            print(int(''.join((str(pr), str(a), str(b)))))
