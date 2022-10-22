"""
 Рассмотрим дробь n/d, где n и d являются натуральными числами.
Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.

 Если перечислить множество сокращенных правильных дробей
для d ≤ 8 в порядке возрастания их значений, получим:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
  4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

 Нетрудно заметить, что данное множество состоит из 21 элемента.

 Из скольки элементов будет состоять множество
сокращенных правильных дробей для d ≤ 1 000 000?
"""

import itertools


def list_totients(n):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:  # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
                
    return result


def compute():
    totients = list_totients(10 ** 6)
    ans = sum(itertools.islice(totients, 2, None))
    return str(ans)


if __name__ == "__main__":
    print(compute())
