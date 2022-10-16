"""
 В карточной игре покер ставка состоит из пяти карт
и оценивается от самой младшей до самой старшей в следующем порядке:

  Старшая карта: Карта наибольшего достоинства.

  Одна пара: Две карты одного достоинства.

  Две пары: Две различные пары карт

  Тройка: Три карты одного достоинства.

  Стрейт: Все пять карт по порядку, любые масти.

  Флаш: Все пять карт одной масти.

  Фул-хаус: Три карты одного достоинства и одна пара карт.

  Каре: Четыре карты одного достоинства.

  Стрейт-флаш: Любые пять карт одной масти по порядку.

  Роял-флаш: Десятка, валет, дама, король и туз одной масти.

 Достоинство карт оценивается по порядку:
2, 3, 4, 5, 6, 7, 8, 9, 10, валет, дама, король, туз.

 Если у двух игроков получились ставки одного порядка,
то выигрывает тот, у кого карты старше:
к примеру, две восьмерки выигрывают две пятерки (см. пример 1 ниже).
Если же достоинства карт у игроков одинаковы,
к примеру, у обоих игроков пара дам,
то сравнивают карту наивысшего достоинства (см. пример 4 ниже);
если же и эти карты одинаковы, сравнивают следующие две и т.д.

 Допустим, два игрока сыграли 5 ставок следующим образом:

  Ставка	1-й игрок	 	        2-й игрок	 	      Победитель
  1	 	    5♥ 5♣ 6♠ 7♠ K♦    2♣ 3♠ 8♠ 8♦ T♦   2-й игрок
            Пара пятерок            Пара восьмерок

  2         5♦ 8♣ 9♠ J♠ A♣    2♣ 5♣ 7♦ 8♠ Q♥   1-й игрок
            Старшая карта туз      Старшая карта дама

  3         2♦ 9♣ A♠ A♥ A♣    3♦ 6♦ 7♦ T♦ Q♦   2-й игрок
            Три туза               Флаш, бубны

  4         4♦ 6♣ 9♥ Q♥ Q♣    3♦ 6♦ 7♥ Q♦ Q♠   1-й игрок
            Пара дам                Пара дам
            Старшая карта девятка   Старшая карта семерка

  5         2♥ 2♦ 4♣ 4♦ 4♠    3♣ 3♦ 3♠ 9♠ 9♦   1-й игрок
            Фул-хаус                Фул-хаус
            Три четверки            Три тройки

 Файл poker.txt содержит одну тысячу различных ставок
для игры двух игроков. В каждой строке файла приведены десять карт
(отделенные одним пробелом): первые пять - карты 1-го игрока,
оставшиеся пять - карты 2-го игрока. Можете считать,
что все ставки верны (нет неверных символов или повторов карт),
ставки каждого игрока не следуют в определенном порядке,
и что при каждой ставке есть безусловный победитель.

 Сколько ставок выиграл 1-й игрок?

 Примечание: карты в текстовом файле обозначены
в соответствии с английскими наименованиями достоинств и мастей:
T - десятка, J - валет, Q - дама, K - король, A - туз;
S - пики, C - трефы, H - червы, D - бубны.
"""

f = open('p054_poker.txt', 'r')

HANDS = f.read().split('\n')[:-1]

RANKS = "23456789TJQKA"
SUITS = "SHCD"


# Card is a 2-letter string like "2H" for "two of hearts".
# Returns a pair of integers (rank, suit).
def parse_card(card):
    """
    Карта - это двух буквенная строка, вроде "2H" для "два черви".
    Возвращает пару целых чисел (ранг, масть),
    """
    return RANKS.index(card[0]), SUITS.index(card[1])


# Encodes 5 card ranks into 20 bits in big-endian,
# starting with the most frequent cards, breaking ties by highest rank.
# For example, the set of ranks {5,5,T,8,T} is encoded as
# the sequence [T,T,5,5,8] because pairs come before singles
# and highest pairs come first.
def get_5_frequent_highest_cards(ranks, ranks_hist):
    """
    Кодирует 5 рангов карт в 20 бит в big-endian,
    начиная с наиболее часто используемых карт,
    заканчивая связями (?) высшего разряда.
    Например, множество рангов {5,5,T,8,T} закодировано
    как последовательность [T,T,5,5,8]  потому что пары
    идут перед одиночными картами,
    и более высокие по рангу пары идут первыми.
    """
    result = 0
    count = 0

    for i in reversed(range(len(ranks_hist))):
        for j in reversed(range(len(ranks))):
            if ranks[j] == i:
                for k in range(i):
                    if count >= 5:
                        break
                        
                    result = result << 4 | j
                    count += 1

    if count != 5:
        raise ValueError()
    
    return result


# Returns the rank of the highest card in the straight,
# or -1 if the set of cards does not form a straight.
# This takes into account the fact that ace can be rank 0
# (i.e. face value 1) or rank 13 (value immediately after king).
def get_straight_high_rank(ranks):
    """
    Возвращает ранг наивысшей карты в стрейте или -1, если набор карт
    не формирует стрейт.
    При этом учитывается тот факт, что туз может иметь ранг 0
    (т.е. номинальное значение 1)
    или ранг 13 (значение сразу после короля).
    """
    for i in reversed(range(3, len(ranks))):
        for j in range(5):
            if ranks[(i - j + 13) % 13] == 0:
                break  # Current offset is not a straight
        else:  # Straight found
            return i
        
    return -1


# Hand is an array of cards. Returns a score for the given hand.
# If handX beats handY then get_score(handX) > get_score(handY),
# and if handX is a draw with handY
# then get_score(handX) = get_score(handY)
# (even if the hands have different cards).
# Note that scores need not be consecutive -
# for example even if scores 1 and 3 exist, there might be no hand
# that produces a score of 2. The comparison property
# is the only guarantee provided by get_score().
def get_score(hand):
    """
    Рука (hand) - это массив карт. Возвращает счёт для данной руки.
    Если handX бьёт handY, то get_score(handX) > get_score(handY),
    и если между handX и handY ничья,
    то get_score(handX) = get_score(handY)
    (даже если руки состояли из разных карты).
    Замечу, что счёту не нужно быть последовательным  -
    например, даже если счёт 1 и 3 существует,
    может не существовать руки, которая создаёт счёт 2.
    Правильное сравнение - это единственное,
    что обеспечивает get_score().
    """
    assert len(hand) == 5

    # rankcounts[i] is the number of cards with the rank of i
    rankcounts = [sum(1 for (rank, _) in hand if rank == i) for i in
                  range(13)]

    # rankcounthist[i] is the number of times a rank count of i occurs.
    # For example if there is exactly one triplet,
    # then rankcounthist[3] = 1.
    rankcounthist = [rankcounts.count(i) for i in range(6)]

    # flushsuit is in the range [0,3]
    # if all cards have that suit; otherwise -1
    min_suit = min(suit for (_, suit) in hand)
    max_suit = max(suit for (_, suit) in hand)
    flushsuit = min_suit if min_suit == max_suit else -1

    best_cards = get_5_frequent_highest_cards(rankcounts, rankcounthist)
    straight_high_rank = get_straight_high_rank(rankcounts)

    # Main idea: Encode the hand type in the top bits,
    # then encode up to 5 cards in big-endian (4 bits each).
    if straight_high_rank != -1 and flushsuit != -1:
        return 8 << 20 | straight_high_rank  # Straight flush
    elif rankcounthist[4] == 1:
        return 7 << 20 | best_cards  # Four of a kind
    elif rankcounthist[3] == 1 and rankcounthist[2] == 1:
        return 6 << 20 | best_cards  # Full house
    elif flushsuit != -1:
        return 5 << 20 | best_cards  # Flush
    elif straight_high_rank != -1:
        return 4 << 20 | straight_high_rank  # Straight
    elif rankcounthist[3] == 1:
        return 3 << 20 | best_cards  # Three of a kind
    elif rankcounthist[2] == 2:
        return 2 << 20 | best_cards  # Two pairs
    elif rankcounthist[2] == 1:
        return 1 << 20 | best_cards  # One pair
    else:
        return 0 << 20 | best_cards  # High card


# Handpair is a space-separated string of 10 cards.
def is_player1_win(handpair):
    """
    Пара рук (handpair) - это строка из 10-ти карт,
    разделённая пробелами.
    """
    # Parse cards and divide among players
    cards = [parse_card(item) for item in handpair.split(" ")]
    if len(cards) != 10:
        return False
    
    player1 = cards[: 5]
    player2 = cards[5:]
    # Compare hand scores
    return get_score(player1) > get_score(player2)


def compute():
    ans = sum(1 for handpair in HANDS if is_player1_win(handpair))
    return str(ans)


if __name__ == '__main__':
    print(compute())
