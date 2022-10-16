"""
 Первые два последовательные числа,
каждое из которых имеет два отличных друг от друга простых множителя:

  14 = 2 × 7
  15 = 3 × 5

 Первые три последовательные числа,
каждое из которых имеет три отличных друг от друга простых множителя:

  644 = 2² × 7 × 23
  645 = 3 × 5 × 43
  646 = 2 × 17 × 19.

 Найдите первые четыре последовательных числа,
каждое из которых имеет четыре отличных друг от друга простых множителя.
Каким будет первое число?
"""

import itertools
import functools
import math


def compute():
    """
    Возвращает первое число из первых 4-х чисел,
    которые имеют 4 различных простых множителя.
    """
    cond = lambda i: all(
        (count_distinct_prime_factors(i + j) == 4) for j in range(4))
    ans = next(filter(cond, itertools.count()))
    return str(ans)


# Мемоизация
@functools.lru_cache
def count_distinct_prime_factors(n):
    """
    Возвращает число чисел,
    которые имеют 4 различных простых множителя.
    """
    count = 0
    while n > 1:
        count += 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                while True:
                    n //= i
                    if n % i != 0:
                        break
                        
                break
        else:
            break  # n - простое число
            
    return count


if __name__ == "__main__":
    print(compute())
