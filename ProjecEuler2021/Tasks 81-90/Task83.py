"""
 Примечание: Данная задача является намного более сложной версией
81-й задачи.

 В представленной ниже матрице 5 на 5 путь с минимальной суммой
из верхнего левого угла в нижний правый, при передвижении шагами вверх,
вниз, вправо или влево, выделен красным жирным шрифтом.
Его сумма равна 2297.

  131-  673  234- 103- 18-
  201-  96-  342- 965  150-
  630   803  746  422- 111-
  537   699  497  121- 956
  805   732  524  37-  331-

 Найдите сумму наименьшего пути, взяв матрицу 80 на 80
из текстового файла matrix.txt (щелкнув правой кнопкой мыши,
выберите 'Save Link/Target As...') размером 31KБ,
передвигаясь шагами в любых направлениях (вверх, вниз, вправо, влево)
из верхнего левого угла в нижний правый.
"""

f = open('p083_matrix.txt', 'r')

grid = f.read().split('\n')

grid = [a.split(',') for a in grid][:-1]
GRID = list(list(int(n) for n in lst) for lst in grid)


def compute():
    h = len(GRID)
    w = len(GRID[0])
    INFINITY = 1 << 30
    distance = [[INFINITY] * w for i in range(h)]

    def get_distance(x, y):
        if x < 0 or x >= w or y < 0 or y >= h:
            return INFINITY
        else:
            return distance[y][x]

    # Bellman-Ford algorithm with early exit
    distance[0][0] = GRID[0][0]
    changed = True
    while changed:  # Note: The worst-case number of iterations is w*h
        changed = False
        for y in range(h):
            for x in range(w):
                temp = GRID[y][x] + min(
                    get_distance(x - 1, y),
                    get_distance(x + 1, y),
                    get_distance(x, y - 1),
                    get_distance(x, y + 1))
                if temp < distance[y][x]:
                    distance[y][x] = temp
                    changed = True
                    
    return str(distance[h - 1][w - 1])


if __name__ == '__main__':
    print(compute())

