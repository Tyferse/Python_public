"""
 145 является любопытным числом,
поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

 Найдите сумму всех чисел, каждое из которых
равно сумме факториалов своих цифр.

 Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами,
учитывать их не следует.
"""

from math import factorial


def is_sum_factorials(n):
    """
    Функция возвращает True, если число
    является суммой факториалов его цифр.
    """
    if n < 2:
        return False
    
    number = 0
    for d in str(n):
        number += factorial(int(d))
        
    if number == n:
        return True
    
    return False


# Выводит сумму чисел, которые могут быть представлены
# в виде сумм факториалов их цифр
print(sum(i for i in range(100000) if is_sum_factorials(i)))
