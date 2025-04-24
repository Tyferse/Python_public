from math import log


epsilon = float(input("Введите точность: "))

def sixth(epsilon):
    curr = (2**1 + 1)/(3**1 - 1)
    num, denum = 2, 3
    series_sum = curr
    while curr >= epsilon:
        num *= 2
        denum *= 3
        curr = (num + 1) / (denum - 1)
        series_sum += curr

    print(round(series_sum, round(-log(epsilon, 10))))


def twelfth(epsilon):
    curr = -1/(3**1 * (1 + 1))
    n = -1
    d1 = 3
    d2 = 2
    series_sum = curr
    while curr >= epsilon:
        n *= -1
        d1 *= 3
        d2 += 1
        curr = n / (d1 * d2)
        series_sum += curr

    print(round(series_sum, round(-log(epsilon, 10))))

sixth(epsilon)
