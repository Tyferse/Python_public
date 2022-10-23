"""
 Примечание: Данная задача является более сложной версией 81-й задачи.

 В  представленной ниже матрице 5 на 5 путь от любого элемента
левого столбца до любого элемента правого столбца,
при передвижении шагами вверх, вниз и вправо,
с минимальной суммой выделен красным жирным шрифтом.
Его сумма равна 994.

  131   673  234- 103- 18-
  201-  96-  342- 965  150
  630   803  746  422  111
  537   699  497  121  956
  805   732  524  37   331

 Найдите сумму наименьшего пути, взяв матрицу 80 на 80
из текстового файла matrix.txt
(щелкнув правой кнопкой мыши, выберите 'Save Link/Target As...')
размером 31KБ, двигаясь шагами (вверх, вниз, вправо)
от левого столбца к правому стобцу.
"""

f = open('p082_matrix.txt', 'r')

grid = f.read().split('\n')[:-1]

grid = [a.split(',') for a in grid][:-1]
GRID = list(list(int(n) for n in lst) for lst in grid)


def compute():
    h = len(GRID)
    w = len(GRID[0])
    INFINITY = 1 << 30

    def get_value(x, y):
        """
        Возвращает значение текущей клетки в матрице
        с координатами x, y.
        Returns a value of current cell in matrix
        with coordinates x, y.
        """
        if x < 0:
            return 0
        elif y < 0 or y >= h or x >= w:
            return INFINITY
        else:
            return distance[y][x]

    # Dynamic programming
    distance = [[0] * w for _ in range(h)]
    for x in range(w):
        for y in range(h):
            distance[y][x] = GRID[y][x] + min(get_value(x - 1, y),
                                              get_value(x, y - 1))
            
        for y in reversed(range(h)):
            distance[y][x] = min(GRID[y][x] + get_value(x, y + 1),
                                 distance[y][x])

    # Minimum of rightmost column
    ans = min(distance[y][-1] for y in range(h))
    return str(ans)


if __name__ == '__main__':
    print(compute())
