"""
 Предназначен, исходя из массива статистики по игре, показывать
полноразмерную статистику за одну студию в Game Dev Tycoon.

 В качестве file можно указать текстовый файл с данными, studio -
название студии.
 massages и categories - неизменые наборы сообщений заголовков
и категорий сортировки (их лучше вообще не трогать для корректной
работы, хотя massages, если рассмотреть исходный код,  можно поменять
на свой без возникновения ошибок).
"""

__version__ = '1.2'  # Версия

file = 'games_list1.txt'  # Файл с базой данных

f = open(file, 'r', encoding='utf-8-sig')

# Создание списка из данных
games = f.readlines()
games = [line.strip() for line in games]
games = [game.split(' ') for game in games]

GAMES = []

# Генерация списка со словарями, в которых отображаются данные из файла
for i, game in enumerate(games):
    GAMES.append({})

    GAMES[i]['number'] = game[0]

    if '_' in game[1]:
        game[1] = game[1].replace('_', ' ')
    GAMES[i]['name'] = game[1]

    if '-' in game[2]:
        game[2] = tuple(game[2].split('-'))
        game[2] = tuple(s.replace('_', ' ') if '_' in s else s
                        for s in game[2])
    elif '_' in game[2]:
        game[2] = game[2].replace('_', ' ')
    GAMES[i]['platforms'] = game[2]

    GAMES[i]['genre'] = game[3]

    if '_' in game[4]:
        game[4] = game[4].replace('_', ' ')
    GAMES[i]['theme'] = game[4]

    GAMES[i]['age'] = game[5]

    GAMES[i]['rating'] = float(game[6])

    GAMES[i]['sales'] = int(game[7])

    GAMES[i]['expenses'] = int(game[8])

    GAMES[i]['revenue'] = int(game[9])

    GAMES[i]['income'] = int(game[10])

    GAMES[i]['realise date'] = tuple(game[11:14])

    GAMES[i]['fans'] = int(game[14])

    if not game[15].isdigit():
        game[15] = game[15].replace('+', '')
    GAMES[i]['top place'] = int(game[15])

studio = 'Ubisoft'  # Название студии в игре

print('Студия "{}" (Game Dev Tycoon)\n'.format(studio))

# Сообщения, которые будут напечатаны перед статистикой
massages = [('\nСамые рейтинговые игры:', '\nСамые провальные игры:'),
            ('\nСамые прадаваемые игры:',
             '\nСамые наименее прадаваемые игры:'),
            '\nСамые дорогие игры:',
            ('\nСамая большая выручка от игры:',
             '\nСамая маленькая выручка от игры:'),
            ('\nСамый большой доход от игры:',
             '\nСамый маленький доход от игры:'),
            ('\nБольше всего фанатов от игры:',
             '\nМеньше всего фанатов от игры:'),
            ('\nНаибольшее место игры в топе:',
             '\nНаименьшее место игры в топе:')]

# Категории сортировки, указанные в списке словарей
__categories = ('rating', 'sales', 'expenses', 'revenue',
                'income', 'fans', 'top place')

# Вывод статистики и указанных сообщений
for massage, key in zip(massages, __categories):
    # Категория 'expenses' является исключением, потому что из трат
    # выводится только одно сообщение, а не два
    if key != 'expenses' and len(massage) == 2:
        if key == 'rating':
            # Сначала выбирается ключ и печатается первое сообщение
            print(massage[0])

            # Затем словарь сортируется по выбранному признаку
            data = sorted(GAMES, key=lambda x: x[key], reverse=True)

            for n in tuple(
                    (game['name'], game[key]) for game in data)[:10]:
                # Из отсортированного словаря печатаются первые десять
                # игр и их рейтинг
                print(f'{n[0]} - {n[1]}/10')

            print(massage[1])  # Выводиться второе сообщение

            # Словарь сортируется по тому же признаку,
            # но в противоположном направлении
            data = sorted(GAMES, key=lambda x: x[key])

            for n in tuple(
                    (game['name'], game[key]) for game in data)[:10]:
                # Выводятся первые десять игр и их рейтинг
                # в новом отсортированном словаре
                print(f'{n[0]} - {n[1]}/10')

        elif key == 'sales':
            print(massage[0])

            data = sorted(GAMES, key=lambda x: x[key], reverse=True)

            for n in tuple(
                    (game['name'], game[key]) for game in data)[:10]:
                print(f'{n[0]} - {n[1]:,d} копий')

            print(massage[1])

            data = sorted(GAMES, key=lambda x: x[key])

            for n in tuple(
                    (game['name'], game[key]) for game in data)[:10]:
                print(f'{n[0]} - {n[1]:,d} копий')

        elif key in ('income', 'revenue'):
            print(massage[0])

            data = sorted(GAMES, key=lambda x: x[key], reverse=True)

            for n in tuple((game['name'], game[key])
                           for game in data)[:10]:
                print(f'{n[0]} - {n[1]:,d} $')

            print(massage[1])

            data = sorted(GAMES, key=lambda x: x[key])

            for n in tuple((game['name'], game[key])
                           for game in data)[:10]:
                print(f'{n[0]} - {n[1]:,d} $')

        elif key == 'fans':
            print(massage[0])

            data = sorted(GAMES, key=lambda x: x[key], reverse=True)

            for n in tuple((game['name'], game[key])
                           for game in data)[:10]:
                print(f'{n[0]} - {n[1]:,d} фанатов')

            print(massage[1])

            data = sorted(GAMES, key=lambda x: x[key])

            for n in tuple((game['name'], game[key])
                           for game in data)[:10]:
                print(f'{n[0]} - {n[1]:,d} фанатов')

        elif key == 'top place':
            print(massage[0])

            data = sorted(GAMES, key=lambda x: x[key])

            for n in tuple(
                    (game['name'], game[key], game['realise date'])
                    for game in data)[:10]:
                print(f'{n[0]} - {n[1]} место, {" ".join(n[2])}')

            print(massage[1])

            data = sorted(GAMES, key=lambda x: x[key], reverse=True)

            for n in tuple(
                    (game['name'], game[key], game['realise date'])
                    for game in data)[:10]:
                print(f'{n[0]} - {n[1]} место, {" ".join(n[2])}')

    elif key == 'expenses':
        # Категория 'expenses' является исключением, потому что из трат
        # выводится только одно сообщение, а не два
        print(massage)

        data = sorted(GAMES, key=lambda x: x[key], reverse=True)

        for n in tuple((game['name'], game[key]) for game in data)[:10]:
            print(f'{n[0]} - {n[1]:,d} $')
    else:
        # На случай возникновения каких-либо ошибок
        raise AssertionError(massage, 'don\'t match', key, 'correctly.')


print('\n\nПоказатели серий игр.\n')


def gen_series(num, name, /, indexes: tuple) -> dict:
    """Returns a dictionary of game series in Game Dev Tycoon."""
    
    """
    if GAMES[indexes[0]]['platforms'].isalnum():
        platforms = {(GAMES[indexes[0]]['platforms'])}
    else:
        platforms = set(GAMES[indexes[0]]['platforms'])
    print('_' * 50, platforms)

    for i in indexes[1:]:
        #
        if len(GAMES[i]['platforms']) == 1:
            platforms = platforms | set(GAMES[i]['platforms'])
        else:
            platforms = platforms | set(GAMES[i]['platforms'])
    """
    platforms = []
    for i in indexes:
        if type(GAMES[i]['platforms']) == tuple:
            platforms += [p for p in GAMES[i]['platforms']
                          if p not in platforms]
            
        else:
            if GAMES[i]['platforms'] not in platforms:
                platforms
    # print([GAMES[i]['platforms'] for i in indexes])
    # print('_' * 50, platforms)
    # Формируется шаблон словаря данных об игровой серии
    series = {'number': num, 'name': name, 'platforms': platforms,
              'genre': GAMES[indexes[0]]['genre'],
              'theme': GAMES[indexes[0]]['theme'],
              'age': GAMES[indexes[0]]['age']}

    # Добавляются ключи с числовыми значениями
    series.update(dict.fromkeys(['rating', 'sales', 'expenses',
                                 'revenue', 'income', 'fans'], 0))

    # Числовые значения каждой игры серии суммируются
    for i in indexes:
        series['rating'] += GAMES[i]['rating']
        series['sales'] += GAMES[i]['sales']
        series['expenses'] += GAMES[i]['expenses']
        series['revenue'] += GAMES[i]['revenue']
        series['income'] += GAMES[i]['income']
        series['fans'] += GAMES[i]['fans']

    # Суммарная оценка делится на количество,
    # чтобы получить среднее арифметическое
    series['rating'] /= len(indexes)

    return series


def show_series_stat(series: dict, indexes: iter):
    """Prints a game series statistics in Game Dev Tycoon."""
    # Сначала выводиться навание серии
    print('\nСерия игр {number}: {name}\n'.format(**series))

    # Затем отображаются статичные данные
    for i in indexes:
        print('{name} - дата выхода: {realise date}, '
              'место в рейтинге: {top place}\nплатформы - {platforms}'
              .format(**GAMES[i]))

    # В последнюю очередь отображается статистика по числам
    print('\nСуммарные показатели:\nрейтинг - {rating:.2f}/10, '
          '\nпродажи - {sales:,d} копий,\nзатраты - {expenses:,d}$, '
          '\nвыручка - {revenue:,d}$,\nприбыль - {income:,d}$,'
          '\nфанатов серии - {fans:,d}.'.format(**series))

    print(*series['platforms'], sep=', ')


# Здесь вручную прописываются все игровые серии и вывод информации о них
series1 = gen_series(1, 'SIMS', (0, 40))

show_series_stat(series1, (0, 40))

series2 = gen_series(2, 'Space Outvaders',
                     (2, 16))

show_series_stat(series2, (2, 16))

series3 = gen_series(3, 'Medivalion', (3, 18))

show_series_stat(series3, (3, 18))

series4 = gen_series(4, '10 -faces', (4, 20, 44))

show_series_stat(series4, (4, 20, 44))

series5 = gen_series(5, '198x', (7, 43))

show_series_stat(series5, (7, 43))

series6 = gen_series(6, 'Silent hill', (10, 22, 33))

show_series_stat(series6, (10, 22, 33))

series7 = gen_series(7, 'Citybuilder', (12, 29))

show_series_stat(series7, (12, 29))

series8 = gen_series(8, 'The elder Scrolls', (14, 47))

show_series_stat(series8, (14, 47))

series9 = gen_series(9, 'Call of Duty', (15, 27, 57))

show_series_stat(series9, (15, 27, 57))

series10 = gen_series(10, 'Resident Evil', (17, 32, 49, 58))

show_series_stat(series10, (17, 32, 49, 58))

series11 = gen_series(11, 'Fallout', (24, 31, 50, 56))

show_series_stat(series11, (24, 31, 50, 56))

series12 = gen_series(12, 'NASA Effect', (26, 45))

show_series_stat(series12, (26, 45))

series13 = gen_series(13, 'Mortal Kombat', (28, 41, 53))

show_series_stat(series13, (28, 41, 53))

series14 = gen_series(14, 'Cyberpunk', (30, 51))

show_series_stat(series14, (30, 51))

series15 = gen_series(15, 'Troppico', (36, 55))

show_series_stat(series15, (36, 55))

series16 = gen_series(16, 'Hitman', (37, 46, 54))

show_series_stat(series16, (37, 46, 54))
