"""
 Для проведения операций с банковскими счетами онлайн
распространен метод безопасности, заключающийся в том,
что пользователя просят указать три случайные символа его кода доступа.
К примеру, если код доступа пользователя 531278,
у него могут попросить ввести 2-й, 3-й и 5-й символы,
и ожидаемым ответом будет 317.

 В текстовом файле keylog.txt содержится 50 удачных попыток авторизации.

 Учитывая, что три символа кода всегда запрашивают по их порядку в коде,
проанализируйте файл с целью определения наиболее короткого
секретного кода доступа неизвестной длины.
"""

import itertools


f = open('p079_keylog.txt', 'r')

SUBSEQS = f.read().split('\n')[:-1]


def is_subsequence(shortstr, longstr):
    """
    Возвращает True, если shortstr равен longstr.
    Returns True if shortstr is equal to longstr.
    """
    i = 0
    for c in longstr:
        if c == shortstr[i]:
            i += 1
            if i == len(shortstr):
                return True
            
    return False


def is_consistent(guess):
    """
    Возвращает True, если все подпоследовательности
    равны этой подпоследовательности.
    Returns True if all subsequances
    are equal to this subsequence.
    """
    return all(is_subsequence(s, guess) for s in SUBSEQS)


def compute():
    # Only guess characters that appear in the attempts
    charsused = sorted(set().union(*SUBSEQS))
    base = len(charsused)

    # Try ascending lengths
    for length in itertools.count(base):
        indices = [0] * length
        while True:
            guess = "".join(charsused[d] for d in indices)
            if is_consistent(guess):
                return guess

            # Increment indices
            i = 0
            while i < length and indices[i] == base - 1:
                indices[i] = 0
                i += 1
                
            if i == length:
                break
                
            indices[i] += 1


if __name__ == '__main__':
    print(compute())
    