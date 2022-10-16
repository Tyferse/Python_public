"""
 Найдите такое наименьшее натуральное число x,
чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.
"""


def same_digits_nums(arr=None):
    """
    Возвращает наименьший x для 2*x, 3*x, 4*x, 5*x и 6*x
    который содержит те же цифры."""
    if arr is None:
        arr = list(range(2, 7))

    x = 1

    while 1:
        lst = [sorted(set(str(x*i))) for i in arr]
        for s in range(1, len(lst)):
            if lst[s-1] != lst[s]:
                x += 1
                break
        return x


print(same_digits_nums())
