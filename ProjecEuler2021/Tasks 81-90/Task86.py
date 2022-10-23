"""
 Паук S сидит в одном углу комнаты в форме
прямоугольного параллелепипеда размерами 6 на 5 на 3, а муха F
сидит в противоположном углу. Путешествуя по поверхностям комнаты,
кратчайший путь "по прямой" от S до F имеет длину 10
и показан на рисунке ниже.

 Однако, в любом прямоугольном параллелепипеде существует
до трех кандидатов на "кратчайший" путь,
и кратчайший путь не всегда имеет целую длину.

 Рассматривая все комнаты в форме прямоугольного параллелепипеда с
максимальными размерами M на M на M, существует ровно 2060
прямоугольных параллелепипедов, для которых кратчайшее расстояние -
целое число, при M = 100, и это - наименьшее значение M,
при котором количество решений превышает две тысячи:
при M = 99 количество решений равно 1975.

 Найдите наименьшее значение M,
при котором количество решений превышает один миллион.
"""

import fractions
import itertools
import math


def compute():
    """
    solutions[k] - это множество всех решений,
    где наибольшая сторона имеет длину k.
    Решение - это тройка (x, y, z) такая, что 0 < x <= y <= z,
    и в прямоугольной призме с измерениями x * y * z,
    кратчайший путь поверхности от одной вершины
    к противоположной вершине имеет целочисленную длину.
    """
    # solutions[k] is the set of all solutions
    # where the largest side has length k.
    # A solution is a triple (x, y, z) such that 0 < x <= y <= z,
    # and in the rectangular prism with dimensions x * y * z,
    # the shortest surface path from one vertex
    # to the opposite vertex has an integral length.
    solutions = []

    # Assumes that a^2 + b^2 = c^2.
    def find_splits(a, b, c):
        z = b
        for x in range(1, a):
            y = a - x
            if y < x:
                break
            if c * c == min(
                    (x + y) * (x + y) + z * z,
                    (y + z) * (y + z) + x * x,
                    (z + x) * (z + x) + y * y):
                temp = max(x, y, z)
                if temp < limit:
                    # Add canonical solution
                    item = tuple(sorted((x, y, z)))
                    solutions[temp].add(item)
                    print(solutions)

    # cumulativesolutions[m] = len(solutions[0])
    # + len(solutions[1]) + ... + len(solutions[m]).
    cumulativesolutions = [0]

    limit = 1
    while True:
        # Extend the solutions list with blank sets
        while len(solutions) < limit:
            solutions.append(set())

        # Generates all solutions where the largest side
        # has length less than 'limit'.
        # Pythagorean triples theorem:
        # Every primitive Pythagorean triple with a odd
        #   and b even can be expressed as
        #   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2,
        #   where s > t > 0 are coprime odd integers.
        # Now generate all Pythagorean triples,
        # including non-primitive ones.
        """
        Генерирует все решения, где наибольшая сторона
        имеет длину меньше, чем 'limit'.
        Теорема о тройках Пифагора:
        Каждая примитивная тройка Пифагора с нечетным числом a
          и четным числом b может быть выражена как
          a = st, b = (s ^ 2-t ^ 2) /2, c = (s ^ 2 + t ^ 2) /2,
          где s > t > 0 - взаимно простое нечетное целое число.
        Сейчас генерируем все тройки Пифагора, включая не примитивные.
        """
        for s in itertools.count(3, 2):
            for t in range(s - 2, 0, -2):
                if s * s // 2 >= limit * 3:
                    break

                if math.gcd(s, t) == 1:
                    for k in itertools.count(1):
                        a = s * t * k
                        b = (s * s - t * t) // 2 * k
                        c = (s * s + t * t) // 2 * k
                        if a >= limit and b >= limit:
                            break
                            
                        find_splits(a, b, c)
                        find_splits(b, a, c)

        # Compute the number of cumulative solutions up
        # to and including a certain maximum size
        # Вычисляем количество кумулятивных решений
        # до определенного максимального размера включительно
        for i in range(len(cumulativesolutions), limit):
            sum1 = cumulativesolutions[i - 1] \
                   + len(solutions[i])
            cumulativesolutions.append(sum1)
            if sum1 > 1000000:
                return str(i)

        # Raise the limit and keep searching
        limit *= 2


if __name__ == "__main__":
    print(compute())
