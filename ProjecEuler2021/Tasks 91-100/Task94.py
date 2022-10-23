"""
 Легко показать, что не существует равносторонних треугольников
с целочисленными сторонами и площадью.
Однако, площадь почти равностороннего треугольника
со сторонами 5-5-6 равна 12 квадратным единицам.

 Определим почти равносторонний треугольник
как равнобедренный треугольник, у которого основание
отличается от боковой стороны не более чем на одну единицу.

 Найдите сумму периметров всех почти равносторонних треугольников
с целыми боковыми сторонами и площадью, периметр каждого из которых
не превышает один миллиард (1 000 000 000).
"""

import itertools
import math


# Consider an arbitrary almost equilateral triangle
# with side lengths (c, c, c +/- 1).
# Split it down the middle to get a right triangle,
# and label the new sides.
#     /\               /|
#  c /  \ c         c / | b
#   /    \    -->    /  |
#  --------         -----
#   c +/- 1           a
# Note that a = (c +/- 1) / 2, and a^2 + b^2 = c^2
# (Pythagorean theorem).
#
# We know that c is an integer. The area of the original triangle
# is a*b, which is an integer by definition from the problem statement.
# - If a is an integer, then b is an integer
#   (so that a*b is an integer),
#   thus (a,b,c) is a Pythagorean triple.
# - Otherwise a is an integer plus a half, then b must be even,
#   but a^2 + b^2 is not an integer, which contradicts c
#   being an integer.
#
# Conversely, consider an arbitrary Pythagorean triple (a,b,c).
# If 2a = c +/- 1, then we can form an almost equilateral triangle:
#     /|\
#  c / | \ c
#   /  |  \
#  ---------
#      2a
# For this to happen, the Pythagorean triple must be primitive.
# Because if not, then a = 0 mod k and c = 0 mod k
# for some k > 1, which means 2a = 0 mod k
# which cannot equal c +/- 1 = +/- 1 mod k.
# So we only need to generate primitive triples.
#
# Pythagorean triples theorem:
#   Every primitive Pythagorean triple
#   with a odd and b even can be expressed as
#   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2,
#   where s > t > 0 are coprime odd integers.
def compute():
    """
    Рассмотрим произвольный почти равносторонний треугольник
    с длинами сторон (c, c, c +/- 1). Разделяем его посередине,
    чтобы получился прямоугольный треугольник,
    и обозначьте новые стороны.
       /\               /|
    c /  \ c         c / | b
     /    \    -->    /  |
    --------         -----
    c +/- 1           a
    Заметим, что a = (c +/- 1) / 2, и a^2 + b^2 = c^2
    (Теорема Пифагора)
    
    Мы знаем, что c - это целое число. Площадь исходного треугольника
    равна a*b, что является целым числом по определению
    из постановки задачи.
    - Если a - целое число, то b - целое число
      (так что a*b - целое число),
      таким образом (a,b, c) - это тройка Пифагора.
    - В противном случае a - целое число плюс половина,
      тогда b должно быть четным,
      но a ^ 2 + b ^ 2 не является целым числом,
      что противоречит тому, что c является целым числом.

    И наоборот, рассмотрим произвольную пифагорейскую тройку (a, b, c).
    Если 2a = c + /- 1, то мы можем сформировать
    почти равносторонний треугольник:
        /|\
     c / | \ c
      /  |  \
     ---------
        2a
    Чтобы это произошло, тройка Пифагора должна быть примитивной.
    Потому что если нет, то a = 0 mod k и c = 0 mod k
    для некоторого k > 1, что означает 2 * a = 0 mod k,
    что не может быть равно c + /- 1 = + /- 1 mod k.
    Таким образом, нам нужно только сгенерировать примитивные тройки.

    Теорема о тройках Пифагора:
      Каждая примитивная пифагорейская тройка с нечетным числом a
      и четным числом b может быть выражена как
      a = s * t, b = (s ^ 2-t ^ 2) / 2, c = (s ^ 2 + t ^ 2) / 2,
      где s > t > 0 - взаимно простые нечетные целые числа.
    """
    LIMIT = 10 ** 9
    ans = 0
    # What search range do we need?
    # c = (s^2+t^2)/2. Perimeter = p = 3c +/- 1
    # = 3/2 (s^2+t^2) +/- 1 <= LIMIT.
    # We need to keep the smaller perimeter within limit for
    # the search to be meaningful, so 3/2 (s^2+t^2) - 1 <= LIMIT.
    # With t < s, we have that s^2+t^2 < 2s^2,
    # so 3/2 (s^2+t^2) - 1 < 3s^2 - 1.
    # Therefore it is sufficient to ensure
    # that 3s^2 - 1 <= LIMIT, i.e. s^2 <= (LIMIT+1)/3.
    """
    Какой диапазон поиска нам нужен?
    c = (s^2+t^2)/2.
    Периметр = p = 3c +/- 1 = 3/2 (s^2+t^2) +/- 1 <= LIMIT.
    Нам нужно держать меньший периметр в пределах допустимого,
    чтобы поиск был осмысленным, поэтому 3/2 (s^2+t^2) - 1 <= LIMIT.
    С t < s, мы имеем, что s^2+t^2 < 2s^2,
    поэтому 3/2 (s^2+t^2) - 1 < 3s^2 - 1.
    Поэтому достаточно обеспечить
    3s^2 - 1 <= LIMIT, т. е. s^2 <= (LIMIT+1)/3.
    """
    for s in itertools.count(1, 2):
        if s * s > (LIMIT + 1) // 3:
            break
            
        for t in range(s - 2, 0, -2):
            if math.gcd(s, t) == 1:
                a = s * t
                b = (s * s - t * t) // 2
                c = (s * s + t * t) // 2
                if a * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= LIMIT:
                        ans += p
                        
                if a * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= LIMIT:
                        ans += p
                        
                # Swap the roles of a and b and try the same tests
                # Note that a != b, since otherwise c = a * sqrt(2)
                # would be irrational
                # Меняем ролями a и b и проверяем на тех же тестах
                # Заметим, что a != b,
                # так как в противном случае c = a * sqrt(2)
                # было бы иррациональным
                if b * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= LIMIT:
                        ans += p
                        
                if b * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= LIMIT:
                        ans += p
                        
    return str(ans)


if __name__ == "__main__":
    print(compute())
