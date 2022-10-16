"""
 Гугол (10^100) - гигантское число: один со ста нулями;
100^100 почти невообразимо велико: один с двумястами нулями.
Несмотря на их размер, сумма цифр каждого числа равна всего лишь 1.

 Рассматривая натуральные числа вида a^b, где a, b < 100,
какая встретится максимальная сумма цифр числа?
"""


def digit_sum(n):
    """
    Возвращает сумму цифр числа.
    Return a sum of digits in a number.
    """
    sum1 = 0
    for d in str(n):
        sum1 += int(d)

    return sum1


max_sum = 0
for a in range(100):
    for b in range(100):
        ab = digit_sum(a**b)
        if ab > max_sum:
            max_sum = ab

print(max_sum)
