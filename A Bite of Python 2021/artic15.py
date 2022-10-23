# Ввод-вывод

# Ввод пользователя

def reverse(text):
    return text[::-1]


def is_palindrome1(text):
    return text == reverse(text)


something = input('Введите текст: ')

if is_palindrome1(something):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")

'''
Домашнее задание

 Проверка, является ли текст палиндромом должна также
игнорировать знаки пунктуации, пробелы и регистр букв.
'''


def is_palindrome(text):
    """Проверяет, является ли текст палиндромом?"""

    for s in (',', '.', '!', ':', ';', '-'):
        text = text.replace(s, '')

    text = text.replace(' ', '').lower()

    if text == reverse(text):
        return "Да, это палиндром"
    else:
        return "Нет, это не палиндром"


print(is_palindrome("А роза, упала на лапу Азора!"))

# Файлы

poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python!
'''

f = open('poem.txt', 'w')  # открываем для записи (writing)
f.write(poem)  # записываем текст в файл
f.close()  # закрываем файл

f = open('poem.txt')  # если не указан режим,
# по умолчанию подразумевается режим чтения ('r'eading)

while True:
    line = f.readline()
    if len(line) == 0:  # Нулевая длина обозначает конец файла (EOF)
        break
        
    print(line, end='')

f.close()  # закрываем файл

# Pickle

'''
 Стандартный модуль с именем pickle, при помощи которого 
можно сохранять любой объект Python в файле, 
а затем извлекать его обратно.
Это называется длительным хранением объекта.
'''

import pickle


# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data'

# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)  # помещаем объект в файл
f.close()

del shoplist  # уничтожаем переменную shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)  # загружаем объект из файла
print(storedlist)

'''
 Чтобы сохранить объект в файле, нам нужно сперва открыть файл 
с помощью open в режиме бинарной записи ('wb'), 
после чего вызвать функцию dump из модуля pickle. 
Этот процесс называется «консервацией» («pickling»).

 После этого мы извлекаем объект при помощи функции load 
из модуля pickle, которая возвращает объект.
Этот процесс называется  «расконсервацией» («unpickling»).
'''
