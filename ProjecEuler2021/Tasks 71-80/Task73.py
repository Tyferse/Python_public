"""
 Рассмотрим дробь n/d, где n и d являются натуральными числами.
Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.

 Если перечислить множество сокращенных правильных дробей для d ≤ 8
в порядке возрастания их значений, получим:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
  4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

 Нетрудно заметить, между дробями 1/3 и 1/2 расположены 3 другие дроби.

 Сколько дробей расположено между 1/3 и 1/2 в упорядоченном множестве
сокращенных правильных дробей для d ≤ 12 000?

 Примечание: Верхний предел был недавно изменен.
"""


# The Stern-Brocot tree is an infinite binary search tree
# of all positive rational numbers,
# where each number appears only once and is in lowest terms.
# It is formed by starting with the two sentinels 0/1 and 1/1.
# Iterating infinitely in any order,
# between any two currently adjacent fractions Ln/Ld and Rn/Rd,
# insert a new fraction (Ln+Rn)/(Ld+Rd).
# See MathWorld for a visualization:
# http://mathworld.wolfram.com/Stern-BrocotTree.html
#
# The natural algorithm is as follows:
#   # Counts the number of reduced fractions n/d such that
#   # leftN/leftD < n/d < rightN/rightD and d <= 12000.
#   # leftN/leftD and rightN/rightD must be adjacent
#   # in the Stern-Brocot tree at some point in the generation process.
#   def stern_brocot_count(leftn, leftd, rightn, rightd):
#     d = leftd + rightd
#     if d > 12000:
#       return 0
#     else:
#       n = leftn + rightn
#       return 1 + stern_brocot_count(leftn, leftd, n, d) +
#              stern_brocot_count(n, d, rightn, rightd)

# But instead we use depth-first search on an explicit stack,
# because having a large number of stack frames
# seems to be supported on Linux but not on Windows.
def compute():
    """
    Дерево Стерна-Броко - это бесконечное двоичное дерево
    поиска всех положительных рациональных чисел,
    где каждое число появляется только один раз
    и находится в наименьших терминах.
    Он формируется, начиная с двух стражей 0/1 и 1/1.
    Повторяя бесконечно в любом порядке, между любыми двумя
    соседними в данный момент дробями Ln /Ld и Rn /Rd,
    вставьте новую дробь (Ln+Rn)/(Ld+Rd).
    Смотрите MathWorld для визуализации:
    http://mathworld.wolfram.com/Stern-BrocotTree.html
    
    Естественный алгоритм выглядит следующим образом:
    # Подсчитывает количество сокращенных дробей n/d таким образом, что
    # leftN/leftD < n/d < rightN/rightD и d <= 12000.
    # leftN/leftD и rightN/rightD должны быть смежными
    # в дереве Стерна-Броко в какой-то момент процесса генерации.
    def stern_brocot_count(leftn, leftd, rightn, rightd):
        d = leftd + rightd
        if d > 12000:
            return 0
        else:
            n = leftn + rightn
            return 1 + stern_brocot_count(leftn, leftd, n, d) +
                   stern_brocot_count(n, d, rightn, rightd)
    
    
    Но вместо этого мы используем поиск по глубине в явном стеке,
    потому что наличие большого количества кадров стека,
    по-видимому, поддерживается в Linux, но не в Windows.
    """
    ans = 0
    stack = [(1, 3, 1, 2)]
    while len(stack) > 0:
        leftn, leftd, rightn, rightd = stack.pop()
        d = leftd + rightd
        if d <= 12000:
            n = leftn + rightn
            ans += 1
            stack.append((n, d, rightn, rightd))
            stack.append((leftn, leftd, n, d))
            
    return str(ans)


if __name__ == "__main__":
    print(compute())
