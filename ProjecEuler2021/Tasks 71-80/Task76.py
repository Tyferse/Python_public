"""
 Число 5 можно записать в виде суммы ровно шестью различными способами:

  4 + 1
  3 + 2
  3 + 1 + 1
  2 + 2 + 1
  2 + 1 + 1 + 1
  1 + 1 + 1 + 1 + 1

 Сколькими различными способами можно записать число 100
в виде суммы по крайней мере двух натуральных чисел?
"""


def compute():
    LIMIT = 100
    partitions = []
    for i in range(LIMIT + 1):
        partitions.append([None] * (LIMIT + 1))
        for j in reversed(range(LIMIT + 1)):
            if j == i:
                val = 1
            elif j > i:
                val = 0
            elif j == 0:
                val = partitions[i][j + 1]
            else:
                val = partitions[i][j + 1] + partitions[i - j][j]
                
            partitions[i][j] = val

    if partitions[LIMIT][1] is not None:
        ans = partitions[LIMIT][1] - 1
    else:
        ans = partitions[LIMIT][0] - 1
        
    return str(ans)


if __name__ == "__main__":
    print(compute())
