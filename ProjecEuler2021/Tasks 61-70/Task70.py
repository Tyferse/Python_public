"""
 Функция Эйлера, φ(n) [иногда ее называют фи-функцией]
используется для определения количества чисел,
меньших n, которые взаимно просты с n.
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти
и взаимно просты с девятью, φ(9) = 6.

 Число 1 считается взаимно простым для любого положительного числа,
так что φ(1) = 1.

 Интересно, что φ(87109) = 79180, и, как можно заметить,
87109 является перестановкой 79180.

 Найдите такое значение n, 1 < n < 107,
при котором φ(n) является перестановкой n,
а отношение n/φ(n) является минимальным.
"""


def list_totients(n):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:  # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
                
    return result


def compute():
    totients = list_totients(10 ** 7 - 1)
    minnumer = 1
    mindenom = 0
    for (i, tot) in enumerate(totients[2:], 2):
        if i * mindenom < minnumer * tot \
           and sorted(str(i)) == sorted(str(tot)):
            minnumer = i
            mindenom = totients[i]
            
    return str(minnumer)


if __name__ == "__main__":
    print(compute())
