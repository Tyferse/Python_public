import os.path
import re


# Получение текста из файла
"""
filename = input('Введите путь к файлу с текстом \
(пишите два слэша(\\\)): ')
"""

filename = 'games_list1.txt'
f = open(filename, 'r', encoding='utf-8')

# Получение размера файла в байтах
size = os.path.getsize(filename)
i = 0
all_words = {}


def dictintegrator(*dicts: dict) -> dict:
    """
    Функция объединяет словари с парами СТРОКА: ЧИСЛО.
    """
    dn = {}
    for d in dicts:
        for key in d:
            if key in dn:
                dn[key] += d[key]
            else:
                dn[key] = d[key]
                
    return dn


# Чтение файла по одному килобайту
while i <= (size // 1024):
    text = f.read(1024 * 256)
    text = text.lower()
    print('\nЭто ' + str(i) + ' килобайт из '
          + str(size // 1024) + '\n')

    # Очистка текста от знаков препинания
    text = re.sub(r'[^\w\s]', '', text)
    marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
    for w in text:
        if w in marks:
            w = w.replace(w, '')

    # Счёт каждого слова в тексте и добавление его в словарь "список"
    spisok = {}
    text = text.split()
    for w in text:
        n = text.count(w)
        spisok[w] = n

    # Сортировка словаря "список" по значениям
    sorted_spisok = {}
    sorted_keys = sorted(spisok, key=spisok.get, reverse=True)

    for w in sorted_keys:
        sorted_spisok[w] = spisok[w]

    """
    sorted_values = sorted(spisok.values(), reverse=True)
    sorted_spisok = {}
    for i in sorted_values:
        for k in spisok.keys():
            if spisok[k] == i:
                sorted_spisok[k] = spisok[k]
                break
    """

    i += 256
    print(sorted_spisok)
    all_words = dictintegrator(all_words, sorted_spisok)

f.close()

print({key: all_words[key] for key in all_words
       if all_words[key] > 4 and not key.isdigit()})
