"""
 Пусть в коробке лежит двадцать один диск,
среди которых пятнадцать окрашены в синий цвет и остальные шесть -
в красный. Из коробки случайным образом взяли два диска.
Нетрудно показать, что вероятность достать два синих диска
равна P(BB) = (15/21)×(14/20) = 1/2.

 Следующая комбинация из наименьшего возможного количества дисков
ровно 50%-ным шансом случайным образом достать 2 синих диска -
это коробка с 85 синими дисками и 35 красными.

 Найдите такую комбинацию с наименьшим возможным
суммарным количеством дисков, превышающим 10^12 = 1 000 000 000 000,
и определите количество синих дисков, находящихся в коробке.
"""

import math


# Suppose the box has b blue discs and r red discs.
# The probability of taking 2 blue discs is
# [b / (b + r)] * [(b - 1) / (b + r - 1)],
# which we want to be equal to 1/2. Rearrange the equation:
#   [b(b - 1)] / [(b + r)(b + r - 1)] = 1 / 2.
#   2b(b - 1) = (b + r)(b + r - 1).
#   2b^2 - 2b = b^2 + br - b + br + r^2 - r.
#   b^2 - b = r^2 + 2br - r.
#   b^2 - (2r + 1)b + (r - r^2) = 0.
# Apply the quadratic equation to solve for b:
#   b = [(2r + 1) +/- sqrt((2r + 1)^2 - 4(r - r^2))] / 2
#     = r + [1 +/- sqrt(8r^2 + 1)]/2
#     = r + [sqrt(8r^2 + 1) + 1]/2.
#     (Discard the minus solution because it would make b < r)
#
# For b to be an integer, we need sqrt(8r^2 + 1) to be odd,
# and also 8r^2 + 1 be a perfect square.
# Assume 8y^2 + 1 = x^2 for some integer x > 0.
# We can see this is in fact a Pell's equation: x^2 - 8y^2 = 1.
#
# Suppose we have the solution (x0, y0) such that
# x0 > 0 and x0 is as small as possible.
# This is called the fundamental solution,
# and all other solutions be derived from it (proven elsewhere).
# Suppose (x0, y0) and (x1, y1) are solutions. Then we have:
#   x0^2 - 8*y0^2 = 1.
#   (x0 + y0*sqrt(8))(x0 - y0*sqrt(8)) = 1.
#   (x1 + y1*sqrt(8))(x1 - y1*sqrt(8)) = 1.  (Similarly)
# Multiply them together:
#   [(x0 + y0*sqrt(8))(x0 - y0*sqrt(8))][(x1
#   + y1*sqrt(8))(x1 - y1*sqrt(8))] = 1 * 1.
#   [(x0 + y0*sqrt(8))(x1 + y1*sqrt(8))][(x0
#   - y0*sqrt(8))(x1 - y1*sqrt(8))] = 1.
#   [x0*x1 + x0*y1*sqrt(8) + x1*y0*sqrt(8) + 8y0*y1][x0*x1
#   - x0*y1*sqrt(8) - x1*y0*sqrt(8) + 8y0*y1] = 1.
#   [(x0*x1 + 8y0*y1) + (x0*y1 + x1*y0)*sqrt(8)][(x0*x1
#   + 8y0*y1) - (x0*y1 + x1*y0)*sqrt(8)] = 1.
#   (x0*x1 + 8y0*y1)^2 - 8*(x0*y1 + x1*y0)^2 = 1.
# Therefore (x0*x1 + 8y0*y1, x0*y1 + x1*y0) is also a solution.
# By inspection, the fundamental solution is (3, 1).
"""
Предположим, что в коробке есть b синих дисков и r красных дисков.
Вероятность взятия 2 синих дисков равна
[b / (b + r)] * [(b - 1) / (b + r - 1)],
от который мы хотим, чтобы она был равна 1/2. Переставьте уравнение:
  [b(b - 1)] / [(b + r)(b + r - 1)] = 1/2.
  2b(b - 1) = (b + r)(b + r - 1).
  2b^2 - 2b = b ^ 2 + br - b + br + r^2 - r.
  b^2 - b = r^2 + 2br - r.
  b^2 - (2r + 1)b + (r - r^2) = 0.
Примените квадратное уравнение для решения для b:
  b = [(2r + 1) +/- sqrt((2r + 1)^2 - 4(r - r^2))] / 2
    = r + [1 +/- sqrt(8r^2 + 1)]/2
    = r + [sqrt(8r^2 + 1) + 1]/2.
    (Отбросьте минусовое решение, потому что это сделало бы b < r)

Чтобы b было целым числом, нам нужно,
чтобы sqrt (8r ^ 2 + 1) был нечетным,
а также 8r ^ 2 + 1 был идеальным квадратом.
Предположим, что 8y ^ 2 + 1 = x ^ 2 для некоторого целого числа x > 0.
Мы видим, что на самом деле это уравнение Пелла: x ^ 2 - 8y ^ 2 = 1.

Предположим, у нас есть решение (x0, y0) такое, что x0 > 0
и x0 как можно меньше. Это называется фундаментальным решением,
и все остальные решения должны быть выведены из него
(доказано в другом месте).
Предположим, что (x0, y0) и (x1, y1) являются решениями.
Тогда мы имеем:
  x0^2 - 8*y0^2 = 1.
  (x0 + y0*sqrt(8))(x0 - y0*sqrt(8)) = 1.
  (x1 + y1*sqrt(8))(x1 - y1*sqrt(8)) = 1.  (Similarly)
Умножаем их вместе:
  [(x0 + y0*sqrt(8))(x0 - y0*sqrt(8))] *
  [(x1 + y1*sqrt(8))(x1 - y1*sqrt(8))] = 1 * 1.
  [(x0 + y0*sqrt(8))(x1 + y1*sqrt(8))] *
  [(x0 - y0*sqrt(8))(x1 - y1*sqrt(8))] = 1.
  [x0*x1 + x0*y1*sqrt(8) + x1*y0*sqrt(8) + 8y0*y1] *
  [x0*x1 - x0*y1*sqrt(8) - x1*y0*sqrt(8) + 8y0*y1] = 1.
  [(x0*x1 + 8y0*y1) + (x0*y1 + x1*y0)*sqrt(8)] *
  [(x0*x1 + 8y0*y1) - (x0*y1 + x1*y0)*sqrt(8)] = 1.
  (x0*x1 + 8y0*y1)^2 - 8*(x0*y1 + x1*y0)^2 = 1.
Следовательно, (x0* x1 + 8y0*y1, x0*y1 + x1*y0) также является решением.
При проверке фундаментальным решением является (3, 1).
"""


# Fundamental solution
x0 = 3
y0 = 1

# Current solution
x = x0
y = y0  # An alias for the number of red discs
while True:
    # Check if this solution is acceptable
    sqrt = math.sqrt(y ** 2 * 8 + 1)
    if sqrt % 2 == 1:  # Is odd
        blue = (sqrt + 1) // 2 + y
        if blue + y > 10 ** 12:
            print(int(blue))
            break

    # Create the next bigger solution
    nextx = x * x0 + y * y0 * 8
    nexty = x * y0 + y * x0
    x = nextx
    y = nexty
