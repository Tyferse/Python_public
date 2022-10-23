"""
 Собственными делителями числа являются все его делители,
за исключением самого числа. К примеру,
собственными делителями числа 28 являются 1, 2, 4, 7 и 14.
Т. к. сумма этих делителей равна 28,
будем называть такое число идеальным.

 Интересно, что сумма всех собственных делителей числа 220 равна 284,
а сумма всех собственных делителей числа 284 равна 220,
образуя цепочку их двух чисел. Поэтому числа 220 и 284
называются парой дружественных чисел.

 Менее известны цепочки большей длины.
К примеру, начиная с числа 12496, образуется цепочка из 5 чисел:

  12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

 Т. к. эта цепочка оканчивается тем же числом,
которым она начиналась, ее называют цепочкой дружественных чисел.

 Найдите наименьший член самой длинной цепочки дружественных чисел,
ни один элемент которой не превышает один миллион.
"""

import itertools


LIMIT = 10 ** 6

# divisorsum[n] is the sum of all the proper divisors of n
divisorsum = [0] * (LIMIT + 1)
for i in range(1, LIMIT + 1):
    for j in range(i * 2, LIMIT + 1, i):
        divisorsum[j] += i

# Analyze the amicable chain length for each number in ascending order
maxchainlen = 0
ans = -1
for i in range(LIMIT + 1):
    visited = set()
    cur = i
    for count in itertools.count(1):
        # 'count' is the length of the this amicable chain
        visited.add(cur)
        next1 = divisorsum[cur]
        if next1 == i:
            if count > maxchainlen:
                ans = i
                maxchainlen = count
                
            break
        # Exceeds limit or not a chain (a rho shape instead)
        elif next1 > LIMIT or next1 in visited:
            break
        else:
            cur = next1

print(str(ans))
