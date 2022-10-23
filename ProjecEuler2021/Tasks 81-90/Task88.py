"""
 Каждое натуральное число N, которое можно записать как в виде суммы,
так и в виде произведения элементов множества,
состоящего из по крайней мере двух натуральных чисел {a1, a2, ... , ak},
называется числом произведения-суммы:
N = a1 + a2 + ... + ak = a1 × a2 × ... × ak />.

 К примеру, 6 = 1 + 2 + 3 = 1 × 2 × 3.

 Для заданного множества размером k мы будем называть
наименьшее число N, обладающее данным свойством,
наименьшим числом произведения-суммы.
Наименьшими числами произведения-суммы множеств размером
k = 2, 3, 4, 5 и 6 являются следующие числа:

  k=2: 4 = 2 × 2 = 2 + 2
  k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
  k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
  k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
  k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

 Отсюда следует, что сумма всех минимальных чисел произведения-суммы
при 2≤k≤6 равна 4+6+8+12 = 30. Обратите внимание на то,
что число 8 учитывалось в сумме лишь один раз.

 Т.к. множеством минимальных чисел произведения-суммы
при 2≤k≤12 является {4, 6, 8, 12, 15, 16}, то их сумма равна 61.

 Какова сумма всех минимальных чисел произведения-суммы
при 2≤k≤12000?
"""


# minSumProduct[k] is the smallest positive integers
# that can be written as both a sum and a product
# of the same collection of k positive integers.
# For example, minSumProduct[3] = 6
# because 6 = 1 + 2 + 3 = 1 * 2 * 3,
# and this is the minimum possible number for 3 terms.
#
# For all k >= 2:
# - minSumProduct[k] > k because 1 + ... + 1 (with k terms) = k,
#   which is the minimum sum of k positive integers,
#   but the product is 1 which is unequal to k,
#   so k is not a valid solution.
# - minSumProduct[k] <= 2k because 1 + ... + 1 + 2 + k
#   (with k terms in total) = (k - 2) + 2 + k = 2k.
#   The product is 2k, which equals the sum.
#   Since this is one achievable solution,
#   the minimum solution must be no larger than this.
# - Aside: minSumProduct[k] is not a prime number.
#   Suppose minSumProduct[k] = p, where p is prime.
#   Then p can only be factorized as p, p * 1, p * 1 * 1, etc.
# So whenever the factorization has more than one term,
# the sum exceeds p, which makes it unequal to the product.
#
# Therefore we need to consider all numbers from 2 to LIMIT*2
# and factorize them in all possible ways
# to find all the relevant solutions.
def compute():
    """
    minSumProduct[k] - это наименьшее из положительных целых чисел,
    которое может быть записано как сумма, так и произведение
    одного и того же набора k положительных целых чисел.
    Например, minSumProduct[3] = 6,
    потому что 6 = 1 + 2 + 3 = 1 * 2 * 3,
    и это минимально возможное число для 3 членов.
    
    Для всех k >= 2:
    - minSumProduct [k] > k, потому что 1 + ... + 1 (с k членами) = k,
      что является минимальной суммой k натуральных чисел,
      но произведение равно 1, что неравно k,
      поэтому k не является допустимым решением.
    - minSumProduct[k] <= 2k, потому что 1 + ... + 1 + 2 + k
      (всего слагаемых k) = (k2) + 2 + k = 2k. Произведение равно 2k,
      что равно сумме. Поскольку это одно из достижимых решений,
      минимальное решение должно быть не больше этого.
    - В сторону: minSumProduct[k] не является простым числом.
      Предполагается minSumProduct[k] = p, где p - простое число.
      Тогда p может быть разложено на множители
      только как p, p * 1, p * 1 * 1 и т.д.
    Таким образом, всякий раз, когда факторизация (разложение)
    имеет более одного члена, сумма превышает p,
    что делает ее неравной произведению.

    Поэтому нам нужно рассмотреть все числа от 2 до LIMIT*2
    и разложить их на множители всеми возможными способами,
    чтобы найти все соответствующие решения.
    """
    LIMIT = 12000
    minsumproduct = [None] * (LIMIT + 1)

    # Calculates all factorizations of the integer n >= 2
    # and updates smaller solutions into minSumProduct.
    # For example, 12 can be factorized as follows -
    # and duplicates are eliminated by finding
    # only non-increasing sequences of factors:
    # - 12 = 12. (1 term)
    # - 12 = 6 * 2 * 1 * 1 * 1 * 1 = 6 + 2 + 1 + 1 + 1 + 1. (6 terms)
    # - 12 = 4 * 3 * 1 * 1 * 1 * 1 * 1 = 4 + 3 + 1 + 1 + 1 + 1 + 1.
    # (7 terms)
    # - 12 = 3 * 2 * 2 * 1 * 1 * 1 * 1 * 1 =
    # 3 + 2 + 2 + 1 + 1 + 1 + 1 + 1. (8 terms)
    def factorize(n, remain, maxfactor, sum1, terms):
        """
        Вычисляет все факторизации целого числа n > = 2
        и обновляет меньшие решения в min SumProduct.
        Например, 12 можно разложить на множители следующим образом -
        и дубликаты устраняются путем нахождения
        только нерастущих последовательностей множителей:
         - 12 = 12. (1 член)
         - 12 = 6 * 2 * 1 * 1 * 1 * 1 = 6 + 2 + 1 + 1 + 1 + 1.
           (6 членов)
         - 12 = 4 * 3 * 1 * 1 * 1 * 1 * 1 = 4 + 3 + 1 + 1 + 1 + 1 + 1.
           (7 членов)
         - 12 = 3 * 2 * 2 * 1 * 1 * 1 * 1 * 1 =
                3 + 2 + 2 + 1 + 1 + 1 + 1 + 1. (8 членов)
        """
        if remain == 1:
            if sum1 > n:  # Without using factors of 1,
                #           the sum1 never exceeds the product
                raise AssertionError()
            
            terms += n - sum1
            if terms <= LIMIT \
                and (minsumproduct[terms] is None
                     or n < minsumproduct[terms]):
                minsumproduct[terms] = n
        else:
            # Note: maxfactor <= remain
            for i in range(2, maxfactor + 1):
                if remain % i == 0:
                    factor = i
                    factorize(n, remain // factor,
                              min(factor, maxfactor),
                              sum1 + factor, terms + 1)

    for i in range(2, LIMIT * 2 + 1):
        factorize(i, i, i, 0, 0)

    # Eliminate duplicates and compute sum1
    ans = sum(set(minsumproduct[2:]))
    return str(ans)


if __name__ == "__main__":
    print(compute())
