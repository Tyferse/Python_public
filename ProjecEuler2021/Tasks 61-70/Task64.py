"""
 Любой квадратный корень является периодическим,
если записать его в виде непрерывных дробей в следующей форме:

√N = a0 + 1
        	a1 +
        1
        	 	a2 +
        1
        	 	 	a3 + ...


 К примеру, рассмотрим √23:

√23 = 4 + √23 — 4 = 4 + 1 = 4 + 1
                                1
                              √23—4
 1 +  √23 – 3
        7

 Продолжив это преобразование, мы получим следующее приближение:

√23 = 4 +
1
 	1 +
1
 	 	3 +
1
 	 	 	1 +
1
 	 	 	 	8 + ...

 Этот процесс можно обобщить в следующем виде:

a0 = 4, 1/√23—4 = (√23+4)/7 = 1 + (√23—3)/7
a1 = 1,7/(√23—3)=7(√23+3)/14 = 3 + (√23—3)/2
a2 = 3, 2/(√23—3) = 2(√23+3)/14 = 1 + (√23—4)/7
a3 = 1, 7/(√23—4) = 7(√23+4)/7 = 8 + √23—4
a4 = 8, 1/(√23—4) = (√23+4)/7 = 1 + (√23—3)/7
a5 = 1, 7/(√23—3) = 7(√23+3)/14 = 3 + (√23—3)/2
a6 = 3, 2/(√23—3) = 2(√23+3)/14 = 1 + (√23—4)/7
a7 = 1, 7(√23—4) = 7(√23+4)/7 = 8 + √23—4

 Нетрудно заметить, что последовательность является периодической.
Для краткости введем обозначение √23 = [4;(1,3,1,8)],
чтобы показать что блок (1,3,1,8) бесконечно повторяется.

 Первые десять представлений непрерывных дробей
(иррациональных) квадратных корней:

  √2=[1;(2)], период = 1
  √3=[1;(1,2)], период = 2
  √5=[2;(4)], период = 1
  √6=[2;(2,4)], период = 2
  √7=[2;(1,1,1,4)], период = 4
  √8=[2;(1,4)], период = 2
  √10=[3;(6)], период = 1
  √11=[3;(3,6)], период = 2
  √12= [3;(2,6)], период = 2
  √13=[3;(1,1,1,1,6)], период = 5

 Период является нечетным у ровно четырех непрерывных дробей при N ≤ 13.

 У скольких непрерывных дробей период является нечетным при N ≤ 10000?
"""

import fractions
import math

import eulerlib


def compute():
    ans = sum(1 for i in range(1, 10001) if (not eulerlib.is_square(
        i) and get_sqrt_continued_fraction_period(i) % 2 == 1))
    return str(ans)


# Returns the period of the continued fraction of sqrt(n)
def get_sqrt_continued_fraction_period(n):
    """
    Возвращает период бесконечной дроби sqrt(n)
    """
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        val = (val - QuadraticSurd(val.floor(), 0, 1,
                                   val.d)).reciprocal()
        if val in seen:
            return len(seen) - seen[val]


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
