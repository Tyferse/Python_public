"""
 Меняя первую цифру числа *3 (двузначного числа,
заканчивающегося цифрой 3), оказывается,
что шесть из девяти возможных значений -
13, 23, 43, 53, 73 и 83 - являются простыми числами.

 При замене третьей и четвертой цифры числа 56**3 одинаковыми цифрами,
получаются десять чисел, из которых семь - простые:
56003, 56113, 56333, 56443, 56663, 56773 и 56993.
Число 56**3 является наименьшим числом,
подстановка цифр в которое дает именно семь простых чисел.
Соответственно, число 56003, будучи первым из полученных простых чисел,
является наименьшим простым числом, обладающим указанным свойством.

 Найдите наименьшее простое число,
которое является одним из восьми простых чисел,
полученных заменой части цифр
(необязательно соседних) одинаковыми цифрами.
"""

import eulerlib


def do_mask(digits, mask):
    """Returns a mask from digits."""
    return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]


def add_mask(digits, mask):
    """Adds mask from digits and previous mask."""
    return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]


def to_number(digits):
    """Returns an integer from digits."""
    result = 0
    for d in digits:
        result = result * 10 + d
    return result


def compute():
    primes = eulerlib.primes(1000000)
    for i in primes:
        n = [int(c) for c in str(i)]
        # Создание маски из цифр простого числа
        for mask in range(1 << len(n)):
            digits = do_mask(n, mask)
            count = 0
            # Если является простым числом,
            # добавляется новая маска с подставными цифрами
            for j in range(10):
                if digits[0] != 0 \
                   and eulerlib.is_prime(to_number(digits)):
                    count += 1
                digits = add_mask(digits, mask)

            # Если 8 простых чисел, возвращается наименьшее
            if count == 8:
                digits = do_mask(n, mask)
                for j in range(10):
                    if digits[0] != 0 \
                       and eulerlib.is_prime(to_number(digits)):
                        return str(to_number(digits))
                    
                    digits = add_mask(digits, mask)

    raise AssertionError("Not found")


if __name__ == '__main__':
    print(compute())
