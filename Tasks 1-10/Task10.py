"""
 Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

 Найдите сумму всех простых чисел меньше двух миллионов.
"""


def primes(n):
    """ Returns a list of primes < n"""
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
            
    # Список индексов элементов, которые являются простыми числоми
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


# Выводит сумму простых чисел меньше двух миллионов
print(sum(primes(2000000)))
