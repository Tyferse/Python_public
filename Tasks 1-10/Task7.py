"""
 Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-е простое число - 13.

 Какое число является 10001-м простым числом?
"""

import math


def primes_sieve(n):
    """Вывод n-ого простого числа при помощи решета Эратосфена."""
    p_n = int(2 * n * math.log(n))
    sieve = [True] * p_n
    count = 0
    for i in range(2, p_n):
        if sieve[i]:  # является простым числом?
            count += 1  # считаем его!
            if count == n:
                return i
            
            for j in range(2 * i, p_n, i):
                sieve[j] = False


print(primes_sieve(10001))
