"""
 В представленной ниже матрице 5 на 5 путь с минимальной суммой
при движении из верхнего левого угла в нижний правый
(шагами только либо направо, либо вниз) выделен красным жирным шрифтом.
Его сумма равна 2427.

  131-  673  234  103  18
  201-  96-  342- 965  150
  630   803  746- 422- 111
  537   699  497  121- 956
  805   732  524  37-  331-

 Найдите сумму наименьшего пути, взяв матрицу 80 на 80
из текстового файла matrix.txt (щелкнув правой кнопкой мыши,
выберите 'Save Link/Target As...') размером 31KБ,
 двигаясь шагами (либо направо, либо вниз)
из верхнего левого угла в нижний правый.
"""

f = open('p081_matrix.txt', 'r')

grid = f.read().split('\n')

grid = [a.split(',') for a in grid][:-1]
grid = list(list(int(n) for n in lst) for lst in grid)


def compute():
    # Dynamic programming
    for i in reversed(range(len(grid))):
        for j in reversed(range(len(grid[i]))):
            if i + 1 < len(grid) and j + 1 < len(grid[i]):
                temp = min(grid[i + 1][j], grid[i][j + 1])
            elif i + 1 < len(grid):
                temp = grid[i + 1][j]
            elif j + 1 < len(grid[i]):
                temp = grid[i][j + 1]
            else:
                temp = 0
                
            grid[i][j] += temp
            
    return str(grid[0][0])


if __name__ == '__main__':
    print(compute())
