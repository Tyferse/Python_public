"""
 Рассмотрим следующее "магическое" треугольное кольцо,
заполненное числами от 1 до 6, с суммой на каждой линии равной 9.

 Проходя по направлению часовой стрелки,
начав с группы с наименьшим внешним узлом (в данном примере: 4,3,2),
каждое решение можно описать единственным образом.
К примеру, вышеуказанное решение можно описать множеством:
4,3,2; 6,2,1; 5,1,3.

 Существует возможность заполнить кольцо
с четырьмя различными суммами на линиях: 9, 10, 11 и 12.
Всего существует восемь решений.

Сумма	Множество решений
  9	    4,2,3; 5,3,1; 6,1,2
  9	    4,3,2; 6,2,1; 5,1,3
  10	2,3,5; 4,5,1; 6,1,3
  10	2,5,3; 6,3,1; 4,1,5
  11	1,4,6; 3,6,2; 5,2,4
  11	1,6,4; 5,4,2; 3,2,6
  12	1,5,6; 2,6,4; 3,4,5
  12	1,6,5; 3,5,4; 2,4,6

 Объединяя элементы каждой группы, можно образовать 9-тизначную строку.
Максимальное значение такой строки
для треугольного кольца составляет 432621513.

 Используя числа от 1 до 10, в зависимости от расположения,
можно образовать 16-тизначные и 17-тизначные строки.
Каково максимальное значение 16-тизначной строки
для "магического" пятиугольного кольца?
"""

# import itertools


def compute():
    state = list(range(1, 11))
    max1 = None
    while True:
        sum1 = state[0] + state[5] + state[6]
        if state[1] + state[6] + state[7] == sum1 and \
                state[2] + state[7] + state[8] == sum1 and \
                state[3] + state[8] + state[9] == sum1 and \
                state[4] + state[9] + state[5] == sum1:

            minouterindex = 0
            minouter = state[0]
            for i in range(1, 5):
                if state[i] < minouter:
                    minouterindex = i
                    minouter = state[i]

            s = ""
            for i in range(5):
                s += str(state[(minouterindex + i) % 5])
                s += str(state[(minouterindex + i) % 5 + 5])
                s += str(state[(minouterindex + i + 1) % 5 + 5])
            if len(s) == 16 and (max1 is None or s > max1):
                max1 = s

        if not next_permutation(state):
            break

    assert max1 is not None
    return max1


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


if __name__ == "__main__":
    print(compute())
