"""
 Простые числа 3, 7, 109 и 673 достаточно замечательны.
Если взять любые два из них и объединить их в произвольном порядке,
в результате всегда получится простое число. Например, взяв 7 и 109,
получатся простые числа 7109 и 1097. Сумма этих четырех простых чисел,
792, представляет собой наименьшую сумму элементов множества
из четырех простых чисел, обладающих данным свойством.

 Найдите наименьшую сумму элементов множества из 5 простых чисел,
для которых объединение любых двух даст новое простое число.
"""

import functools
import math

import eulerlib


def compute():
    """
    Пытаемся найти любое подходящее множество и возвращаем его сумму
    или None, если ничего не найдено.
    Множество подходящее, если оно содержит только простые числа,
    его размер - это target_size, его сумма меньше и равна to sum_limit,
    и каждая пара при конкатенации образует простое число.
    'prefix' - это массив возрастающих индексов в массив 'primes',
    который описывает множество, найденное до сих пор(?).
    Функция слепо предполагает, что каждая пара простых чисел в 'prefix'
    конкатенируется в простое число.
    
    Например, find_set_sum([1, 3, 28], 5, 10000) означает
    "найти сумму любого множества, размера 5,
    состоящего из простых чисел с наименьшими элементами [3, 7, 109],
    имеет в сумме 10000 или меньше,
    и каждая пара при конкатенации формирует простое число."
    """
    PRIME_LIMIT = 100000  # Arbitrary initial cutoff
    primes = eulerlib.primes(PRIME_LIMIT)

    # Tries to find any suitable set and return its sum,
    # or None if none is found.
    # A set is suitable if it contains only primes,
    # its size is target_size, its sum is less than
    # or equal to sum_limit, and each pair concatenates to a prime.
    # 'prefix' is an array of ascending indices into the 'primes' array,
    # which describes the set found so far.
    # The function blindly assumes that each pair of primes in 'prefix'
    # concatenates to a prime.
    #
    # For example, find_set_sum([1, 3, 28], 5, 10000) means
    # "find the sum of any set where the set has size 5,
    # consists of primes with the lowest elements being [3, 7, 109],
    # has sum 10000 or less,
    # and has each pair concatenating to form a prime".
    def find_set_sum(prefix, target_size, sum_limit):
        if len(prefix) == target_size:
            return sum(primes[i] for i in prefix)
        else:
            istart = 0 if (len(prefix) == 0) else (prefix[-1] + 1)
            for i in range(istart, len(primes)):
                if primes[i] > sum_limit:
                    break
                    
                if all((is_concat_prime(i, j) and is_concat_prime(j, i))
                       for j in prefix):
                    prefix.append(i)
                    result = find_set_sum(prefix, target_size,
                                          sum_limit - primes[i])
                    prefix.pop()
                    if result is not None:
                        return result
                    
            return None

    # Tests whether concat(primes[x], primes[y]) is a prime number,
    # with memoization.
    @functools.cache
    def is_concat_prime(x, y):
        """
        Проверяет, является ли concat(primes[x], primes[y])
        простым числом, с мемоизацией.
        """
        return is_prime(int(str(primes[x]) + str(primes[y])))

    # Tests whether the given integer is prime.
    # The implementation performs trial division,
    # first using the list of primes named 'primes',
    # then switching to simple incrementation.
    # This requires the last number in 'primes' (if any)
    # to be an odd number.
    def is_prime(x):
        """
        Проверяет, является ли данное целое число простым.
        Реализация представляет простое деление,
        первым используется список простых чисел под названием 'primes',
        затем переход к простому увеличению.
        Для этого требуется, чтобы последнее число в "primes"
        (если таковое имеется) было нечетным числом.
        """
        if x < 0:
            raise ValueError()
        elif x in (0, 1):
            return False
        else:
            end = int(math.sqrt(x))
            for p in primes:
                if p > end:
                    break
                    
                if x % p == 0:
                    return False
                
            for i in range(primes[-1] + 2, end + 1, 2):
                if x % i == 0:
                    return False
                
            return True

    sum_limit = PRIME_LIMIT
    while True:
        set_sum = find_set_sum([], 5, sum_limit - 1)
        if set_sum is None:  # No smaller sum found
            return str(sum_limit)
        
        sum_limit = set_sum


if __name__ == "__main__":
    print(compute())
