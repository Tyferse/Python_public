"""
 Можно найти перестановки куба 41063625 (345^3),
чтобы получить еще два куба: 56623104 (384^3) и 66430125 (405^3).
К слову, 41063625 является наименьшим кубом,
для которого ровно три перестановки также являются кубами

 Найдите наименьший куб, для которого ровно пять перестановок
также являются кубами.
"""

import itertools


def compute():
    num_digits = 0
    data = {}  # str num_class -> (int lowest, int count)
    for i in itertools.count():
        digits = [int(c) for c in str(i ** 3)]
        digits.sort()
        num_class = "".join(str(d) for d in digits)

        if len(num_class) > num_digits:
            # Обрабатываем и удаляем данные для меньшего количества цифр
            # Process and flush data for smaller number of digits
            candidates = [lowest for (lowest, count) in data.values()
                          if count == 5]
            if len(candidates) > 0:
                return str(min(candidates) ** 3)
            
            data = {}
            num_digits = len(num_class)

        lowest, count = data.get(num_class, (i, 0))
        data[num_class] = (lowest, count + 1)


if __name__ == "__main__":
    print(compute())
