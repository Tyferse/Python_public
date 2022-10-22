"""
 Рассмотрим квадратные диофантовы уравнения вида:

  x^2 – D*y^2 = 1

 К примеру, для D = 13, минимальное решение x составляет
649^2 – 13×180^2 = 1.

 Можно убедиться в том, что не существует натуральных решений
при D равном квадрату целого числа.

 Найдя наименьшие значения решений x при D = {2, 3, 5, 6, 7},
мы получили следующее:

  3^2 – 2×2^2 = 1
  2^2 – 3×1^2 = 1
  9^2 – 5×4^2 = 1
  5^2 – 6×2^2 = 1
  8^2 – 7×3^2 = 1

 Таким образом, рассматривая минимальные решения x при D ≤ 7,
было получено наибольшее значение x при D = 5.

 Найдите значение D ≤ 1000 для минимальных решений x,
при котором получено наибольшее значение x.
"""

import fractions
import math

import eulerlib


# Based on this insane theorem: Suppose D > 1 is an integer,
# non-perfect-square.
#
# Express sqrt(D) as the continued fraction (a0, a1, ...,
# a_{n-1}, (b0, b1, ..., b_{m-1})),
# where the sequence of b's is the periodic part.
#
# Let p/q (in lowest terms) = (a0, a1, ...,
# a_{n-1}, b0, b1, ..., b_{m-2}).
# (This is a truncation of the continued fraction
# with only one period minus the last term.)
#
# Then the minimum solution (x, y) for Pell's equation is given by:
# - (p, q) if m is even
# - (p^2 + D*q^2, 2pq) if m is odd
def compute():
    """
    Основываясь на этой безумной теореме:
    Предположим D > 1 - это целое число, не идеальный квадрат.
    
    Выражая sqrt(D) как бесконечную дробь (a0, a1, ...,
    a_{n-1}, (b0, b1, ..., b_{m-1})),
    где последовательность из b это периодическая часть.
    
    Пусть p/q (в наименьших выражениях (?)) = (a0, a1, ...,
    a_{n-1}, b0, b1, ..., b_{m-2}).
    (Это усечение непрерывной дроби
    только с одним периодом минус последний член.)
    
    Тогда минимальное решение (x, y) для уравнения Пелла
    задано следующим образом:
     - (p, q), если m четно
     - (p^2 + D*q^2, 2pq), если m нечетно
    """
    t = (n for n in range(2, 1001)
         if (not eulerlib.is_square(n)))
    ans = max(t, key=smallest_solution_x)
    return str(ans)


# Returns the smallest x such that x > 0
# and there exists some y such that x^2 - n*y^2 = 1.
# Requires n to not be a perfect square.
def smallest_solution_x(n):
    """
    Возвращает наименьший x такой, что x > 0
    и существует некоторый y такой, что x^2 - n*y^2 = 1.
    Требуется, чтобы n не был идеальным квадратом.
    """
    contfrac = sqrt_to_continued_fraction(n)
    temp = contfrac[0] + contfrac[1][: -1]

    val = fractions.Fraction(temp[-1], 1)
    for term in reversed(temp[: -1]):
        val = 1 / val + term

    if len(contfrac[1]) % 2 == 0:
        return val.numerator
    else:
        return val.numerator ** 2 + val.denominator ** 2 * n


# Returns the periodic continued fraction of sqrt(n).
# Requires n to not be a perfect square.
# result[0] is the minimal non-periodic prefix,
# and result[1] is the minimal periodic tail.
def sqrt_to_continued_fraction(n):
    """
    Возвращает периодическую бесконечную дробь sqrt(n).
    Требуется, чтобы n не был идеальным квадратом.
    result[0] - это минимальный не периодический префикс,
    и result[1] - это минимальный периодический хвост (?).
    """
    terms = []
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        flr = val.floor()
        terms.append(flr)
        val = (val - QuadraticSurd(flr, 0, 1, val.d)).reciprocal()
        if val in seen:
            break
            
    split = seen[val]
    return terms[: split], terms[split:]


# Represents (a + b * sqrt(d)) / c. d must not be a perfect square.
class QuadraticSurd:
    """
    Представляет (a + b * sqrt(d)) / c.
    d должен быть идеальным квадратом
    """

    def __init__(self, a, b, c, d):
        if c == 0:
            raise ValueError()

        # Simplify
        if c < 0:
            a = -a
            b = -b
            c = -c
            
        gcd = fractions.gcd(fractions.gcd(a, b), c)
        if gcd != 1:
            a //= gcd
            b //= gcd
            c //= gcd

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __sub__(self, other):
        if self.d != other.d:
            raise ValueError()
        
        return QuadraticSurd(
            self.a * other.c - other.a * self.c,
            self.b * other.c - other.b * self.c,
            self.c * other.c,
            self.d)

    def reciprocal(self):
        return QuadraticSurd(
            -self.a * self.c,
            self.b * self.c,
            self.b * self.b * self.d - self.a * self.a,
            self.d)

    def floor(self):
        temp = math.sqrt(self.b * self.b * self.d)
        if self.b < 0:
            temp = -(temp + 1)
            
        temp += self.a
        if temp < 0:
            temp -= self.c - 1
            
        return temp // self.c

    def __eq__(self, other):
        """
        Возвращает True, если одни значения
        равны другим значениям переменных.
        Returns True if one values are equal to
        other values of variables.
        """
        return self.a == other.a and self.b == other.b \
            and self.c == other.c and self.d == other.d

    def __ne__(self, other):
        """
        Возвращает True, если первое значение
        не равно второму значению.
        Returns True if the first value
        don't equal to second value.
        """
        return not (self == other)

    def __hash__(self):
        """
        Возвращает сумму хэшей.
        Returns a sum of hashes.
        """
        return hash(self.a) + hash(self.b) + hash(self.c) + hash(self.d)


if __name__ == "__main__":
    print(compute())
