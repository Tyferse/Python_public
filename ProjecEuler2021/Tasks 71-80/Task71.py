"""
 Рассмотрим дробь n/d, где n и d являются натуральными числами.
Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.

 Если перечислить множество сокращенных правильных дробей
для d ≤ 8 в порядке возрастания их значений, получим:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
  4/7, 3/5,  5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

 Нетрудно заметить, что дробь 2/5 расположена
непосредственно слева от дроби 3/7.

 Перечислив множество сокращенных правильных дробей
для d ≤ 1 000 000 в порядке возрастания их значений,
найдите числитель дроби, расположенной непосредственно
слева от дроби 3/7.
"""

# We consider each (integer) denominator d from 1 to 1000000
# by brute force. For a given d,
# what is the largest integer n such that n/d < 3/7?
#
# - If d is a multiple of 7, then the integer n' = (d / 7) * 3
#   satisfies n'/d = 3/7. Hence we choose n = n' - 1 = (d / 7) * 3 - 1,
#   so that n/d < 3/7. Since (d / 7) * 3 is already an integer,
#   it is equal to floor(d * 3 / 7),
#   which will unifie with the next1 case.
#   Thus n = floor(d * 3 / 7) - 1.
# - Otherwise d is not a multiple of 7, so choosing n = floor(d * 3 / 7)
#   will automatically satisfy n/d < 3/7, and be the largest possible n
#   due to the definition of the floor function.
#
# When we choose n in this manner, it might not be coprime with d.
# In other words, the simplified form of the fraction n/d
# might have a denominator smaller than d.
#
# Let's process denominators in ascending order.
# Each denominator generates a pair of integers (n, d)
# that conceptually represents a fraction, without simplification.
# Whenever the current value of n/d is strictly larger
# than the previously saved value, we save this current value of (n, d).
#
# If we handle denominators in this way - starting from 1,
# counting up consecutively - then it is guaranteed
# that our final saved pair (n, d) is in lowest terms. This is
# because if (n, d) is not in lowest terms,
# then its reduced form (n', d') would have been saved
# when the smaller denominator d' was processed, and because n/d
# is not larger than n'/d' (they are equal),
# the saved value would not be overwritten.
# Hence in this entire computation
# we can avoid explicitly simplifying any fraction at all.


def compute():
    """
    Мы рассматриваем каждый (целочисленный) знаменатель d
    от 1 до 1000000 методом перебора. Для данного d,
    каково наибольшее целое число n, такое, что n / d < 3/7?
    
    - Если d кратно 7, то целое число n' = (d / 7) * 3
      удовлетворяет n'/d = 3/7. Следовательно,
      мы выбираем n = n' - 1 = (d / 7) * 3 - 1, так что n/d < 3/7.
      Поскольку (d / 7) * 3 уже является целым числом,
      оно равно floor(d * 3/7), что будет соответствовать случаю next1.
      Таким образом n = floor(d * 3 / 7) - 1.
    - В противном случае d не кратно 7, поэтому выбор n = floor(d * 3/7)
      автоматически удовлетворит n / d < 3/7
      и будет максимально возможным n по определению функции floor.
    
    Когда мы выбираем n таким образом,
    оно может не быть взаимно простым с d. Другими словами,
    упрощенная форма дроби n/d может иметь знаменатель, меньший, чем d.
    
    Давайте обработаем знаменатели в порядке возрастания.
    Каждый знаменатель генерирует пару целых чисел (n, d),
    которые концептуально представляют собой дробь без упрощения.
    Всякий раз, когда текущее значение n/d строго больше,
    чем ранее сохраненное значение,
    мы сохраняем это текущее значение (n, d).
    
    Если мы обрабатываем знаменатели таким образом - начиная с 1,
    считая последовательно, - то гарантируется,
    что наша конечная сохраненная пара (n, d)
    находится в наименьшем выражении. Это связано с тем,
    что если (n, d) не находится в наименьшем выражении,
    то его уменьшенная форма (n', d') была бы сохранена
    при обработке меньшего знаменателя d',
    и поскольку n / d не больше n' / d' (они равны),
    то сохраненное значение не будет перезаписано.
    Следовательно, во всем этом вычислении мы можем вообще избежать
    явного упрощения какой-либо дроби.
    """
    LIMIT = 1000000
    maxnumer = 0
    maxdenom = 1
    for d in range(1, LIMIT + 1):
        n = d * 3 // 7
        if d % 7 == 0:
            n -= 1
            
        if n * maxdenom > d * maxnumer:  # n/d > maxdenom/maxnumer
            maxnumer = n
            maxdenom = d
            
    return str(maxnumer)


if __name__ == "__main__":
    print(compute())
