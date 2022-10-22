"""
 Как известно, если квадратный корень натурального числа
не является целым числом, то он является иррациональным числом.
Разложение таких квадратных корней на десятичные дроби бесконечно
и не имеет никакой повторяющейся последовательности.

 Квадратный корень из двух равен 1.41421356237309504880...,
а сумма его первых ста цифр в десятичном представлении равна 475.

 Найдите общую сумму первых ста цифр всех
иррациональных квадратных корней среди первых ста натуральных чисел.
"""


def ideal_sqrt(n):
    """
    Возвращает True, если число является идеальным квадратом.
    Return True if number is an ideal square root.
    """
    sqrt = n ** 0.5
    if sqrt % 1 == 0:
        return True
    
    return False


def sqrt2(x):
    """
    Возвращает целое число из квадратного корня числа
    Returns an integer from square root of number.
    """
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
        
    y = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
            
        i //= 2
        
    return y


def compute():
    DIGITS = 100
    MULTIPLIER = 100 ** DIGITS
    ans = sum(
        sum(int(c) for c in
            str(to_fixed((i * MULTIPLIER) ** 0.5))[:DIGITS]
            if c.isdigit())
        for i in range(100)
        if not ideal_sqrt(i)
    )
    
    return str(ans)


def to_fixed(numObj, digits=0):
    """
    возвращает число с плавающей точкой с n цифрами после запятой.
    Returns a floating number with n digits after comma.
    """
    return int(f"{numObj:.{digits}f}")


if __name__ == "__main__":
    print(compute())
