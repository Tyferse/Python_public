"""
 Точки P(x1,y1) и Q(x2,y2) находятся на целых координатах
и соединены с началом координат O(0,0), образуя треугольник ΔOPQ.

 Существует ровно четырнадцать треугольников с прямым углом,
которые можно получить для целых координат
в пределах от 0 до 2 включительно, т.е. 0 ≤ x1,y1,x2,y2 ≤ 2.

 При данных 0 ≤ x1,y1,x2,y2 ≤ 50,
сколько прямоугольных треугольников можно построить?
"""


# Tests whether the three points {(0,0), (x1,y1), (x2,y2)}
# form a right triangle.
def is_right_triangle(x1, y1, x2, y2):
    """
    Возвращает True, если координаты двух точек
    создают правильный треугольник.
    Returns True if coordinates of two points
    creates a right triangle.
    """
    a = x1 ** 2 + y1 ** 2
    b = x2 ** 2 + y2 ** 2
    c = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return (a + b == c) or (b + c == a) or (c + a == b)


LIMIT = 51
rng = range(LIMIT)

# Сумма прямоугольных треугольников внутри координат
ans = sum(1 for x1 in rng for y1 in rng for x2 in rng for y2 in rng
          # For uniqueness, ensure that (x1,y1)
          # has a larger angle than (x2,y2)
          if y2 * x1 < y1 * x2 and is_right_triangle(x1, y1, x2, y2))

print(ans)
