"""
 Стандартная доска игры Монополия выглядит следующим образом:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 	                                  C1
T2	 	                                  U1
H1	 	                                  C2
CH3	 	                                  C3
R4	 	                                  R2
G3	 	                                  D1
CC3	 	                                 CC2
G2	 	                                  D2
G1	 	                                  D3
G2J	 F3	 U2	 F2	 F1	 R3	 E3	 E2	 CH2  E1  FP

 Игрок начинает на клетке GO и складывает выпавшие
на двух шестигранных кубиках числа, чтобы определить количество клеток,
которое он должен пройти по часовой стрелке.
Пользуясь только этим правилом, вероятность посещения каждой клетки
равна 2,5 %. Однако попадание на G2J (Отправляйтесь в тюрьму),
CC (Общественный фонд) и CH (Шанс) меняет распределение.

 В дополнение к G2J и одной карте в CC и в CH,
которые приказывают игроку отправиться в тюрьму,
также если игрок выкидывает три дубля подряд,
он не двигается в свой третий ход, а отправляется сразу в тюрьму.

 В начале игры карты CC и CH перемешиваются.
Когда игрок попадает на клетку CC или CH,
он берет верхнюю карту с соответствующей колоды и,
после выполнения указанных на ней инструкций,
возвращает ее в низ колоды. В каждой колоде 16 карт,
однако для решения этой задачи важны только карты,
связанные с перемещением игрока.
Любые другие инструкции игнорируются и игрок остается на той же клетке.

  Общественный фонд (2/16 карт):
  Пройдите к GO
  Идите в JAIL
  Шанс (10/16 карт):
  Пройдите к GO
  Идите в JAIL
  Идите на C1
  Идите на E3
  Идите на H2
  Идите на R1
  Пройдите к следующей R (железнодорожная станция)
  Пройдите к следующей R
  Пройдите к следующей U (коммунальное предприятие)
  Вернитесь назад на 3 клетки

 Суть этой задачи заключается в вероятности посещения
одной конкретной клетки. То есть, вероятность оказаться на этой клетке
по завершении хода. Поэтому ясно, что за исключением G2J,
чья вероятность посещения равна нулю,
клетка CH будет иметь наименьшую вероятность посещения,
 потому что в 5/8 случаев игроку придется переместиться
 на другую клетку, а нас интересует именно клетка,
 на которой завершится ход игрока. Мы также не будем разделять
попадание в тюрьму как посетитель или как заключенный,
также не берем во внимание правило, что выкинув дубль,
игрок выходит из тюрьмы - предположим, что игроки платят
за выход из тюрьмы на следующий же ход после попадания в нее.

 Начиная с GO и последовательно нумеруя клетки от 00 до 39,
мы можем соединить эти двузначные числа,
чтобы получить соответствующую определенному множеству клеток строку.

 Статистически можно показать, что три наиболее популярных клетки
будут JAIL (6,24%) = Клетка 10, E3 (3,18%) = Клетка 24,
и GO (3,09%) = Клетка 00. Итак, их можно перечислить
как строку из шести цифр: 102400.

 Найдите такую шестизначную строку,
если игроки будут использовать вместо двух шестигранных кубиков
два четырехгранных.
"""

import random


class CardDeck:
    def __init__(self, size):
        self.cards = list(range(size))
        self.index = size

    def next_card(self):
        if self.index == len(self.cards):
            random.shuffle(self.cards)
            self.index = 0
            
        result = self.cards[self.index]
        self.index += 1
        return result


# This is a statistical sampling approximation algorithm
# that simply simulates the game for a fixed number of dice rolls.
# An exact algorithm would involve calculating the eigenvector
# of the largest eigenvalue of the transition matrix
# (which is practical), but averaging over all possible permutations
# of both the Chance and Community Chest decks
# (which is computationally infeasible).
def compute():
    """
    Это алгоритм аппроксимации статистической выборки,
    который просто имитирует игру при фиксированном количестве
    бросков кубиков. Точный алгоритм включал бы
    вычисление собственного вектора наибольшего
    собственного значения матрицы перехода (что практично),
    но усреднение по всем возможным перестановкам как случайной,
    так и общей колоды сундуков (что вычислительно неосуществимо).
    """
    TRIALS = 10 ** 7

    visitcounts = [0] * 40

    chance = CardDeck(16)
    communitychest = CardDeck(16)
    consecutivedoubles = 0
    location = 0

    for i in range(TRIALS):
        # Roll tetrahedral dice
        die0 = random.randint(1, 4)
        die1 = random.randint(1, 4)
        consecutivedoubles = (consecutivedoubles + 1) if (
                    die0 == die1) else 0
        if consecutivedoubles < 3:
            location = (location + die0 + die1) % 40
        else:
            location = 30
            consecutivedoubles = 0

        # Process actions for some locations
        if location in (7, 22, 36):  # Chance
            card = chance.next_card()
            if card == 0:
                location = 0
            elif card == 1:
                location = 10
            elif card == 2:
                location = 11
            elif card == 3:
                location = 24
            elif card == 4:
                location = 39
            elif card == 5:
                location = 5
            elif card in (6, 7):  # Next railway
                location = (location + 5) // 10 % 4 * 10 + 5
            elif card == 8:  # Next utility
                location = 28 if (12 < location < 28) else 12
            elif card == 9:
                location -= 3
            else:
                pass
            
        elif location == 30:  # Go to jail
            location = 10
        else:
            pass

        if location in (2, 17, 33):  # Community chest
            card = communitychest.next_card()
            if card == 0:
                location = 0
            elif card == 1:
                location = 10

        visitcounts[location] += 1

    temp = sorted(enumerate(visitcounts), key=(lambda ic: -ic[1]))
    ans = "".join(f"{i:02}" for (i, c) in temp[: 3])
    return str(ans)


if __name__ == '__main__':
    print(compute())
