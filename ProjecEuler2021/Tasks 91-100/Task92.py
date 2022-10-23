"""
 Последовательность чисел получается путем сложения квадратов цифр
предыдущего числа до тех пор, пока не получится
уже встречавшееся ранее число.

 К примеру,

  44 → 32 → 13 → 10 → 1 → 1
  85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

 Таким образом, любая последовательность,
приводящая к получению 1 или 89, замкнется в бесконечный цикл.
Самое удивительное, что ЛЮБОЕ начальное число
рано или поздно даст 1 или 89.

 Сколько начальных чисел меньше десяти миллионов
приведут к получению 89?
"""


def compute():
    ans = sum(1 for i in range(1, 10000000)
              if get_terminal(i) == 89)
    return str(ans)


TERMINALS = (1, 89)


def get_terminal(n):
    """
    Возвращает сумму квадратов цифр.
    Returns a sum of digits' squares if it's 89, 1.
    """
    while n not in TERMINALS:
        n = square_digit_sum(n)
        
    return n


def square_digit_sum(n):
    """
    Возвращает сумму квадратов по трём цифрам.
    Returns a sum of digits' squares per 3 digits.
    """
    result = 0
    while n > 0:
        result += SQUARE_DIGITS_SUM[n % 1000]
        n //= 1000
        
    return result


SQUARE_DIGITS_SUM = [sum(int(c) ** 2 for c in str(i))
                     for i in range(1000)]

if __name__ == "__main__":
    print(compute())
