"""
 Заменяя каждую из букв слова "CARE" цифрами 1, 2, 9 и 6,
соответственно, получим квадратное число: 1296 = 362.
Примечательно, что после осуществления такой подстановки
в слове "RACE", также получается квадратное число: 9216 = 962.
Слова "CARE" и "RACE" впредь будем называть парой слов -
квадратных анаграмм. Помимо этого, решим, что ведущие нули не разрешены,
а также что ни одной букве нельзя присвоить цифру,
уже присвоенную другой букве.

 В текстовом файле words.txt (щелкнув правой кнопкой мыши,
выберите 'Save Link/Target As...') размером 16KБ
содержится около двух тысяч распространенных английских слов.
Найдите все пары слов - квадратных анаграмм
(слово-палиндром не считается своей же анаграммой).

 Каким будет наибольшее квадратное число,
полученное из любого слова такой пары?

 Примечание: Все образованные анаграммы должны содержаться
в указанном текстовом файле.
"""

import eulerlib


f = open('p098_words.txt', 'r')

WORDS = tuple(f.read().strip('"').split('","'))


# Strings a and b must be anagrams of each other.
def max_square_pair(a, b, index, assignments, is_digit_used):
    """
    Строки a и b должны быть анаграммами друг друга.
    """
    if index == len(a):
        if a[0] in assignments and assignments[a[0]] == 0 or \
                b[0] in assignments and assignments[b[0]] == 0:
            return 0

        anum = 0
        bnum = 0
        for (x, y) in zip(a, b):
            anum = anum * 10 + assignments[x]
            bnum = bnum * 10 + assignments[y]
            
        if eulerlib.is_square(anum) and eulerlib.is_square(bnum):
            return max(anum, bnum)
        else:
            return 0

    elif a[index] in assignments:
        return max_square_pair(a, b, index + 1, assignments,
                               is_digit_used)

    else:
        result = 0
        for i in range(10):
            if not is_digit_used[i]:
                is_digit_used[i] = True
                assignments[a[index]] = i
                result = max(
                    max_square_pair(a, b, index + 1, assignments,
                                    is_digit_used),
                    result)
                del assignments[a[index]]
                is_digit_used[i] = False
                
        return result


def compute():
    anagrams = {}
    for word in WORDS:
        key = "".join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
            
        anagrams[key].append(word)

    ans = 0
    for (key, words) in anagrams.items():
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                assignments = {}
                ans = max(
                    max_square_pair(words[i], words[j], 0, assignments,
                                    [False] * 10), ans)
                
    return str(ans)


if __name__ == '__main__':
    print(compute())
    