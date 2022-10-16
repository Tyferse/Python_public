"""
 n! означает n × (n − 1) × ... × 3 × 2 × 1

 Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

 Найдите сумму цифр в числе 100!.
"""

import math


# Получение числа
number = math.factorial(100)
number = str(number)

summ = 0

# Сложение всех цифр в числе
for i in range(len(number)):
    summ += int(number[i])

print(summ)
