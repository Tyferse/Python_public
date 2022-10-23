"""
 Сравнить два числа, записанных в виде степени,
как, например, 2^11 и 3^7, не так уж трудно,
поскольку любой калькулятор подтвердит, что 2^11 = 2048 < 3^7 = 2187.

 Однако, гораздо сложнее подтвердить,
что 632382^518061 > 519432^525806, поскольку каждое из чисел
содержит более трех миллионов цифр.

 Текстовый файл base_exp.txt (щелкнув правой кнопкой мыши,
выберите 'Save Link/Target As...') размером 22КБ
содержит тысячу строк с парами основание/показатель степени
на каждой строке. Определите номер строки,
в которой записано самое большое по своему значению число.

 Примечание: Первые две строки файла -
числа из примера, приведенного выше.
"""

f = open('p099_base_exp.txt', 'r')

DATA = f.read().split('\n')
DATA = tuple(list(n.split(',')) for n in DATA)
DATA = tuple(tuple(int(i) for i in n) for n in DATA)


def compute():
    ans = None
    max_val = None
    for (i, val) in enumerate(DATA):
        if max_val is None or compare_powers(val, max_val) > 0:
            ans = i + 1
            max_val = val
    return str(ans)


def compare_powers(pairx, pairy):
    """
    Сначала пытаемся выполнить быстрые вычисления с низкой точностью,
    повторяя попытку с возрастающей точностью.
    """
    # First try fast low-precision computations,
    # retrying with increasing precision
    precision = 16
    while precision <= 1024:
        # Use interval arithmetic for approximate comparisons
        xlow = BigFloat(pairx[0]).power(pairx[1], precision, False)
        xhigh = BigFloat(pairx[0]).power(pairx[1], precision, True)
        ylow = BigFloat(pairy[0]).power(pairy[1], precision, False)
        yhigh = BigFloat(pairy[0]).power(pairy[1], precision, True)
        if xhigh.compare_to(ylow) < 0:
            return -1
        elif xlow.compare_to(yhigh) > 0:
            return +1
        else:
            precision *= 2

    # Otherwise do full-precision comparison (slow)
    x = pairx[0] ** pairx[1]
    y = pairy[0] ** pairy[1]
    if x < y:
        return -1
    elif x > y:
        return +1
    else:
        return 0


# Represents a strictly positive number equal to mantissa * 2^exponent
class BigFloat:
    """
    Представляет строго положительные числа,
    равные mantissa * 2^exponent
    """
    def __init__(self, man, exp=0):
        self.mantissa = man
        self.exponent = exp

    # The output's mantissa will have 'precision' or fewer bits
    def multiply(self, other, precision, roundup):
        """
        Мантисса на выходе будет иметь точность 'precision'
        или меньшее количесвто битов.
        """
        man = self.mantissa * other.mantissa
        exp = self.exponent + other.exponent
        excess = man.bit_length() - precision
        if excess > 0:
            if roundup:
                mask = (1 << excess) - 1
                if mask & man != 0:
                    man += 1 << excess
                    
                excess = man.bit_length() - precision
                # In case 'man' is bumped up to the next power of 2
                
            man >>= excess
            exp += excess
            
        return BigFloat(man, exp)

    # Exponentiation by squaring
    def power(self, y, precision, roundup):
        if y < 0 or precision <= 0:
            raise ValueError()
        
        x = self
        z = BigFloat(1, 0)
        while y != 0:
            if y & 1 != 0:
                z = z.multiply(x, precision, roundup)
                
            x = x.multiply(x, precision, roundup)
            y >>= 1
            
        return z

    def compare_to(self, other):
        min_exp = min(self.exponent, other.exponent)
        tempx = self.mantissa << (self.exponent - min_exp)
        tempy = other.mantissa << (other.exponent - min_exp)
        if tempx < tempy:
            return -1
        elif tempx > tempy:
            return +1
        else:
            return 0


if __name__ == '__main__':
    print(compute())
