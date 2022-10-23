"""
 Используя каждую из цифр множества {1, 2, 3, 4} только один раз,
с помощью четырех арифметических действий (+, −, *, /)
и скобок можно получить различные натуральные числа.

 К примеру,

  8 = (4 * (1 + 3)) / 2
  14 = 4 * (3 + 1 / 2)
  19 = 4 * (2 + 3) − 1
  36 = 3 * 4 * (2 + 1)

 Обратите внимание, что объединять цифры, вроде 12 + 34, не разрешается.

 Используя множество {1, 2, 3, 4}, можно получить тридцать
одно отличное число, среди которых наибольшим является 36.
Помимо этого, до обнаружения первого числа,
которое нельзя выразить данным способом,
были получены все числа от 1 до 28.

 Найдите множество четырех отличных цифр a < b < c < d,
с помощью которых можно получить максимально длинное множество
последовательных натуральных чисел от 1 до n. О
твет дайте объединив числа в строку: abcd.
"""

import fractions
import itertools


def compute():
    ans = max(((a, b, c, d)
               for a in range(1, 10)
               for b in range(a + 1, 10)
               for c in range(b + 1, 10)
               for d in range(c + 1, 10)),
              key=longest_consecutive)
    return "".join(str(x) for x in ans)


def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
        
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
        
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True


def longest_consecutive(abcd):
    a, b, c, d = abcd
    expressible = set()

    # Try all possible orderings of operands and operators
    ops = [0, 0, 0, a, b, c, d]
    # 0 = operator slot, 1 to 9 = literal operand
    
    while True:
        # Try all possibilities for the 3 operators
        for i in range(64):
            stack = []
            j = 0  # Operator index

            stack_under_flow = False
            div_by_zero = False
            for op in ops:
                if 1 <= op <= 9:  # Operand
                    stack.append(fractions.Fraction(op))
                    
                elif op == 0:  # Operator
                    if len(stack) < 2:
                        stack_under_flow = True
                        break
                        
                    right = stack.pop()
                    left = stack.pop()
                    oper = (i >> (j * 2)) & 3
                    if oper == 0:
                        stack.append(left + right)
                    elif oper == 1:
                        stack.append(left - right)
                    elif oper == 2:
                        stack.append(left * right)
                    elif oper == 3:
                        if right.numerator == 0:
                            div_by_zero = True
                            break
                            
                        stack.append(left / right)
                    else:
                        raise AssertionError()
                    
                    j += 1  # Consume an operator
                else:
                    raise AssertionError()

            if stack_under_flow:
                break
                
            if div_by_zero:
                continue
                
            if len(stack) != 1:
                raise AssertionError()

            result = stack.pop()
            if result.denominator == 1:
                expressible.add(result.numerator)

        if not next_permutation(ops):
            break

    # Find largest set of consecutive expressible integers
    # starting from 1
    # Ищем наибольшее множество последовательных выражаемых целых чисел,
    # начинающихся с 1
    return next(i for i in itertools.count(1)
                if (i not in expressible)) - 1


if __name__ == "__main__":
    print(compute())
