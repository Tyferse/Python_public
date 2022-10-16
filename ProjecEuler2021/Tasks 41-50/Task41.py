"""
 Будем считать n-значное число пан-цифровым,
если каждая из цифр от 1 до nиспользуется в нем ровно один раз.
К примеру, 2143 является 4-значным пан-цифровым числом,
а также простым числом.

 Какое существует наибольшее n-значное пан-цифровое простое число?
"""

import eulerlib


def compute():
    # Замечание: Только однозначное панцифровое число 1
    # не является простым.
    # Таким образом мы требуем n >= 2.
    for n in reversed(range(2, 10)):
        arr = list(reversed(range(1, n + 1)))
        while True:
            # Если не оканчивается на непростое число
            if arr[-1] not in NONPRIME_LAST_DIGITS:
                n = int("".join(str(x) for x in arr))
                # Если является простым числом
                if eulerlib.is_prime(n):
                    return str(n)
                
            if not prev_permutation(arr):
                break
                
    raise AssertionError()


NONPRIME_LAST_DIGITS = {0, 2, 4, 5, 6, 8}


def prev_permutation(arr):
    i = len(arr) - 1
    # Пока ка;дая цифра больше или равна предыдущей
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
        
    if i <= 0:
        return False
    
    j = len(arr) - 1
    # Пока символ больше или равен предыдущей цифре
    while arr[j] >= arr[i - 1]:
        j -= 1
        
    # число заменяется обратным, начиная с цифры перед первой найденной
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True


if __name__ == "__main__":
    print(compute())
