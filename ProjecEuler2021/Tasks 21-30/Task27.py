"""
 Эйлер опубликовал свою замечательную квадратичную формулу:

  n**2 + n + 41

 Оказалось, что согласно данной формуле можно получить 40 простых чисел,
последовательно подставляя значения 0 ≤ n ≤ 39.
 Однако, при n=40, 40**2 + 40 + 41 = 40*(40 + 1) + 41
делится на 41 без остатка, и, очевидно, при n=41, 41**2 + 41 + 41
делится на 41 без остатка.

 При помощи компьютеров была найдена невероятная формула
n**2 − 79*n + 1601, согласно которой можно получить 80 простых чисел
для последовательных значений n от 0 до 79.
 Произведение коэффициентов −79 и 1601 равно −126479.

 Рассмотрим квадратичную формулу вида:

  n^2 + an + b, где |a| < 1000 и |b| ≤ 1000,

 где |n| является модулем (абсолютным значением) n.

 К примеру, |11| = 11 и |−4| = 4

 Найдите произведение коэффициентов a и b квадратичного выражения,
согласно которому можно получить максимальное количество простых чисел
для последовательных значений n, начиная со значения n=0.
"""

from math import sqrt
import eulerlib
import itertools


def compute():
    ans = max(
        ((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
        key=count_consecutive_primes)
    return str(ans[0] * ans[1])


def count_consecutive_primes(ab):
    a, b = ab
    for i in itertools.count():
        n = i * i + i * a + b
        if not is_prime(n):
            return i


# Возвращает список True и False, по индексу которых располагаются
# простые и не простые числа в зависимости от False или True.
# Для 0 <= i <= n, result[i] является True, если i - простое число,
# False в противном случае.
def list_primality(n):
    # Решето Эратосфена
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(sqrt(n)) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
                
    return result


isprimecache = list_primality(1000)


def is_prime(n):
    if n < 0:
        return False
    elif n < len(isprimecache):
        return isprimecache[n]
    else:
        return eulerlib.is_prime(n)


if __name__ == "__main__":
    print(compute())
