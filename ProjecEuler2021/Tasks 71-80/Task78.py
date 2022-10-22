"""
 Пусть p(n) представляет собой число различных способов
которыми можно разделить монеты на несколько столбиков.
К примеру, пять монет можно разделить на несколько столбиков
ровно семью различными способами, таким образом p(5) = 7.

  OOOOO
  OOOO   O
  OOO   OO
  OOO   O   O
  OO   OO   O
  OO   O   O   O
  O   O   O   O   O

 Найдите наименьшее значение n для которого p(n)
делится на один миллион без остатка.
"""

import itertools

MODULUS = 10 ** 6


def compute():
    partitions = [1]
    for i in itertools.count(len(partitions)):
        # We calculate partitions[i] mod 10^6 using a formula
        # based on generalized pentagonal numbers:
        #   partitions(i) =   partitions(i - pentagonal(1))
        #                   + partitions(i - pentagonal(-1))
        #                   - partitions(i - pentagonal(2))
        #                   - partitions(i - pentagonal(-2))
        #                   + partitions(i - pentagonal(3))
        #                   + partitions(i - pentagonal(-3))
        #                   - partitions(i - pentagonal(4))
        #                   - partitions(i - pentagonal(-4))
        #                   + ...,
        #   where pentagonal(j) = (3*n^2 - n) / 2, and
        #   we stop the sum when i - pentagonal(+/-j) < 0.
        # Note that for j > 0,
        # pentagonal(j) < pentagonal(-j) < pentagonal(j+1).
        #
        # (The formula is used without mathematical justification;
        # see https://en.wikipedia.org/wiki/Partition_
        # (number_theory)#Generating_function .)
        """
        Мы вычисляем partitions[i] mod 10^6, используя формулу,
        основанную на обобщенных пятиугольных числах:
          partitions(i) =   partitions(i - pentagonal(1))
                          + partitions(i - pentagonal(-1))
                          - partitions(i - pentagonal(2))
                          - partitions(i - pentagonal(-2))
                          + partitions(i - pentagonal(3))
                          + partitions(i - pentagonal(-3))
                          - partitions(i - pentagonal(4))
                          - partitions(i - pentagonal(-4))
                          + ...,
          где pentagonal(j) = (3*n^2 - n) / 2, и
          мы останавливаем сумму, когда i - pentagonal(+/-j) < 0.
          
        Заметим, что для j > 0,
        pentagonal(j) < pentagonal(-j) < pentagonal(j+1).
        
        (Формула используется без математического обоснования;
        смотрите https://en.wikipedia.org/wiki/
        Partition_(number_theory)#Generating_function .)
        """
        item = 0
        for j in itertools.count(1):
            sign = -1 if j % 2 == 0 else +1
            index = (j * j * 3 - j) // 2
            if index > i:
                break
                
            item += partitions[i - index] * sign
            index += j  # index == (j * j * 3 + j) // 2
            if index > i:
                break
                
            item += partitions[i - index] * sign
            item %= MODULUS

        # Check or memoize the number
        if item == 0:
            return str(i)
        
        partitions.append(item)


if __name__ == "__main__":
    print(compute())
