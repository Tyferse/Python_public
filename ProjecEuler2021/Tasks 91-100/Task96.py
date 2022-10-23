"""
 Су Доку (по-японски значит место числа) -
название популярной головоломки. Ее происхождение неизвестно,
однако нужно отдать должное Леонарду Эйлеру,
который придумал идею похожей, но более сложной головоломки
под названием Латинские Квадраты. Целью Су Доку
является заменить пустые места (или нули) в сетке 9 x 9
цифрами таким образом, чтобы в каждой строке,
колонке и квадрате 3 x 3 содержались все цифры от 1 до 9.
Ниже приведен пример типичной исходной головоломки и ее решение.

  0 0 3  0 2 0  6 0 0
  9 0 0  3 0 5  0 0 1
  0 0 1  8 0 6  4 0 0
  0 0 8  1 0 2  9 0 0
  7 0 0  0 0 0  0 0 8
  0 0 6  7 0 8  2 0 0
  0 0 2  6 0 9  5 0 0
  8 0 0  2 0 3  0 0 9
  0 0 5  0 1 0  3 0 0


  4 8 3  9 2 1  6 5 7
  9 6 7  3 4 5  8 2 1
  2 5 1  8 7 6  4 9 3
  5 4 8  1 3 2  9 7 6
  7 2 9  5 6 4  1 3 8
  1 3 6  7 9 8  2 4 5
  3 7 2  6 8 9  5 1 4
  8 1 4  2 5 3  7 6 9
  6 9 5  4 1 7  3 8 2

 Правильно составленная головоломка Су Доку
имеет единственное решение и может быть решена с помощью логики,
однако иногда необходимо применять метод "гадай и проверяй",
чтобы исключить неверные варианты
(существует очень спорное мнение по этому поводу).
Сложность поиска определяет уровень головоломки.
Приведенный выше пример считается легким,
так как его можно решить прямой дедукцией.

 6 КБ текстовый файл sudoku.txt
(щелкнув правой кнопкой мыши, выберите Save Link/Target As...)
содержит пятьдесят разных головоломок Су Доку различной сложности,
но каждая имеет единственное решение
(первая головоломка в файле рассмотрена выше).

 Решив все пятьдесят головоломок, найдите сумму трехзначных чисел,
находящихся в верхнем левом углу каждого решения.
Например, 483 является трехзначным числом,
находящимся в верхнем левом углу приведенного выше решения.
"""

f = open('p096_sudoku.txt', 'r')

PUZZLES = f.read().split('\n')

PUZZLES = [''.join(PUZZLES[i+1:i+10]) for i in range(len(PUZZLES))
           if PUZZLES[i].startswith('Grid')]


# Given a string of 81 digits, this returns
# a list of 81 ints representing the solved sudoku puzzle.
def solve(puzzlestr):
    """
    Дана строка из 81 цифры, возвращает список из 81 целого числа,
    представляющий решённый судоку пазл.
    """
    # Initialize initial state
    assert len(puzzlestr) == 81
    state = [int(c) for c in puzzlestr]
    colfree = [set(range(1, 10)) for _ in range(9)]
    rowfree = [set(range(1, 10)) for _ in range(9)]
    boxfree = [set(range(1, 10)) for _ in range(9)]
    for y in range(9):
        for x in range(9):
            d = state[y * 9 + x]
            if d != 0:
                colfree[x].remove(d)
                rowfree[y].remove(d)
                boxfree[y // 3 * 3 + x // 3].remove(d)

    # Returns True/False to indicate whether a solution was found
    # when given the initial state and coordinates.
    def recurse(i):
        """
        Возвращает True/False, указывающее,
        было ли найдено решение,
        при задании начального состояния и координат.
        """
        if i == 81:
            return True
        elif state[i] != 0:
            return recurse(i + 1)
        else:
            x = i % 9
            y = i // 9
            j = y // 3 * 3 + x // 3
            candidates = colfree[x].intersection(rowfree[y], boxfree[j])
            for d in candidates:
                state[i] = d
                colfree[x].remove(d)
                rowfree[y].remove(d)
                boxfree[j].remove(d)
                if recurse(i + 1):
                    return True
                
                # Otherwise backtrack
                colfree[x].add(d)
                rowfree[y].add(d)
                boxfree[j].add(d)
                
            state[i] = 0
            return False

    # Call the helper function
    if not recurse(0):
        raise AssertionError("Unsolvable")
    
    return state


def compute():
    def extract(sudoku):
        # For example: extract([3, 9, 4, 1, ...]) = 394
        return int("".join(map(str, sudoku[: 3])))

    ans = sum(extract(solve(puz)) for puz in PUZZLES)
    return str(ans)


if __name__ == '__main__':
    print(compute())
