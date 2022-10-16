"""
 Пятиугольные числа вычисляются по формуле: Pn = n(3n−1)/2.
Первые десять пятиугольных чисел:

  1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

 Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8.
Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.

 Найдите пару пятиугольных чисел Pj и Pk,
для которых сумма и разность являются пятиугольными числами
и значение D = |Pk − Pj| минимально,
и дайте значение D в качестве ответа.
"""

import itertools


def compute():
    penta_num = PentagonalNumberHelper()
    min_d = None  # None означает - ещё не найдено,
    # положительное число означает - кандидат найден
    # Для каждого верхнего индекса пятиугольного числа, идём вверх
    for i in itertools.count(2):
        pent_i = penta_num.term(i)
        # Если следующее число на 1 меньше, по крайней мере,
        # настолько же большой величины, как найденная разница,
        # то завершить поиск
        if min_d is not None \
                and pent_i - penta_num.term(i - 1) >= min_d:
            break

        # Для каждого нижнего индекса пятиугольного числа, идём вниз
        for j in range(i - 1, 0, -1):
            pent_j = penta_num.term(j)
            diff = pent_i - pent_j
            # Если разница хотя бы такая же большая,
            # как найденная разница, то прекращаем проверку
            # меньших пятиугольных чисел
            if min_d is not None and diff >= min_d:
                break
                
            elif penta_num.is_term(pent_i + pent_j) \
                    and penta_num.is_term(diff):
                min_d = diff  # Найдена меньшая разница
                
    return str(min_d)


# Обеспечивает запоминание (мемоизацию)
# для генерации и тестирования пятиугольных чисел.
class PentagonalNumberHelper:
    def __init__(self):
        self.term_list = [0]
        self.term_set = set()

    def term(self, x):
        """Возвращает ближайшее пятиугольное число."""
        assert x > 0
        while len(self.term_list) <= x:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
            
        return self.term_list[x]

    def is_term(self, y):
        """Возвращает True, если число является пятиугольным."""
        assert y > 0
        while self.term_list[-1] < y:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
            
        return y in self.term_set


if __name__ == "__main__":
    print(compute())
