"""
 К фигурным (многоугольным) числам относятся треугольные, квадратные,
пятиугольные, шестиугольные, семиугольные и восьмиугольные числа,
которые рассчитываются по следующим формулам:

  Треугольные	 	P3,n = n(n+1)/2	 	1, 3, 6, 10, 15, ...
  Квадратные	 	P4,n = n^2	 	    1, 4, 9, 16, 25, ...
  Пятиугольные	 	P5,n = n(3n−1)/2	1, 5, 12, 22, 35, ...
  Шестиугольные	 	P6,n = n(2n−1)	 	1, 6, 15, 28, 45, ...
  Семиугольные	 	P7,n = n(5n−3)/2	1, 7, 18, 34, 55, ...
  Восьмиугольные	P8,n = n(3n−2)	 	1, 8, 21, 40, 65, ...
  
 Упорядоченное множество из трех четырехзначных чисел: 8128, 2882, 8281,
обладает тремя интересными свойствами

  1. Множество является цикличным: последние две цифры каждого числа
     являются первыми двумя цифрами следующего
     (включая последнее и первое числа).
  2. Каждый тип многоугольника — треугольник (P3,127=8128),
     квадрат (P4,91=8281) и пятиугольник (P5,44=2882) —
     представлены различными числами данного множества.
  3. Это — единственное множество четырехзначных чисел,
     обладающее указанными свойствами.

 Найдите сумму элементов единственного упорядоченного множества
из шести цикличных четырехзначных чисел,
в котором каждый тип многоугольников — треугольник, квадрат,
пятиугольник, шестиугольник, семиугольник и восьмиугольник —
представлены различными числами этого множества.
"""

import itertools


def compute():
    """
    Строим таблицу чисел
    numbers[i][j] - это множество фигурных чисел стороны i
    (3 <= i <= 8), имеющих 4 цифры, начиная с 2 цифр равных j
    """
    # Build table of numbers
    # numbers[i][j] is the set of figure numbers
    # of i sides (3 <= i <= 8), having 4 digits,
    # beginning with the 2 digits equal to j
    numbers = [[set() for _ in range(100)] for _ in range(9)]
    for sides in range(3, 9):
        for n in itertools.count(1):
            num = figure_number(sides, n)
            if num >= 10000:
                break
                
            if num >= 1000:
                numbers[sides][num // 100].add(num)

    # Замечание: sides_used - это множество битов
    # Note: sides_used is a bit set
    def find_solution_sum(begin, current, sides_used, sum1):
        """
        Возвращает сумму элементов в упорядоченном множество
        из 6-ти четырёхзначных чисел.
        Return a sum of elements in ordered set
        from 6 4-digit numbers.
        """
        if sides_used == 0b111111000:
            if current % 100 == begin // 100:
                return sum1
        else:
            for sides in range(4, 9):
                if (sides_used >> sides) & 1 != 0:
                    continue
                    
                for num in numbers[sides][current % 100]:
                    temp = find_solution_sum(begin, num,
                                             sides_used | (1 << sides),
                                             sum1 + num)
                    if temp is not None:
                        return temp
                    
            return None

    # Do search
    for i in range(10, 100):
        for num in numbers[3][i]:
            temp = find_solution_sum(num, num, 1 << 3, num)
            if temp is not None:
                return str(temp)
            
    raise AssertionError("No solution")


def figure_number(sides, n):
    """
    Возвращает сторона-гональное n-ое число
    Returns a sides-gonal n'th number.
    """
    return n * ((sides - 2) * n - (sides - 4)) // 2


if __name__ == "__main__":
    print(compute())
