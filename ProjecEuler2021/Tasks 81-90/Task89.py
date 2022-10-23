"""
 Правила записи чисел римскими цифрами позволяют записывать
одно и то же число несколькими способами (см. FAQ: Римские числа).
Однако, всегда существует "наилучший" способ записи определенного числа.

 К примеру, ниже представлены все разрешенные способы
записи числа шестнадцать:

  IIIIIIIIIIIIIIII
  VIIIIIIIIIII
  VVIIIIII
  XIIIIII
  VVVI
  XVI

 Последнее из них считается наиболее эффективным,
поскольку использует наименьшее число римских цифр.

 В текстовом файле roman.txt (щелкнув правой кнопкой мыши,
выберите 'Save Link/Target As...') размером 11KБ тысяча чисел
записана римскими цифрами правильным,
но не обязательно наилучшим способом,
т.е. они отсортированы в порядке убывания
и подчиняются правилу вычитания пар
(для информации об определяющих правилах данной задачи см. FAQ).

 Найдите число символов, сэкономленных путем перезаписи каждого числа
в его наиболее короткий вид.

 Примечание: Можете считать, что все числа в файле содержат
не более четырех последовательных одинаковых цифр.
"""

f = open('p089_roman.txt', 'r')

TO_SIMPLIFY = f.read().split()

ROMAN_NUMERALS_PREFIXES = [("M", 1000), ("CM", 900), ("D", 500),
                           ("CD", 400), ("C", 100), ("XC", 90),
                           ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),
                           ("V", 5), ("IV", 4), ("I", 1)]

# e.g. (empty), I, II, III, IV, V, VI, VII, VIII, IX
DIGIT_LENGTHS = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]


def parse_roman_numeral(s):
    result = 0
    while len(s) > 0:
        for (prefix, val) in ROMAN_NUMERALS_PREFIXES:
            if s.startswith(prefix):
                result += val
                s = s[len(prefix):]
                break
        else:
            raise Exception("Cannot parse Roman numeral")
        
    return result


def roman_numeral_len(n):
    assert 1 < n < 5000
    result = 0
    if n >= 4000:  # 4000 is MMMM, which doesn't have a two-letter form
        result += 2  # Compensate for this fact
        
    while n > 0:
        result += DIGIT_LENGTHS[n % 10]
        n //= 10
        
    return result


ans = sum(len(s) - roman_numeral_len(parse_roman_numeral(s))
          for s in TO_SIMPLIFY)
print(ans)
