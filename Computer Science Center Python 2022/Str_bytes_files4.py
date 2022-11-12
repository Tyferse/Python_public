import io
import string
import sys
import time


print(list(ord(i) for i in 'qwertyuioasfghjklzxcvbnm'
                           'йцукенгшщзхъфывапролджэячсмитьбю'))

ch = '\N{LATIN SMALL LETTER SHARP S}'
print(ch, ch.upper(), ch.upper().lower())

s1 = 'foo bar'
print(s1.capitalize(), s1.title(), s1.title().swapcase())
print(s1.ljust(16, '-'), s1.rjust(16, '-'), s1.center(16, '-'),
      sep='\n')

s2 = ']>>foo bar<<['
print(s2.lstrip(']>'), s2.rstrip('[<'), s2.strip('[]<>'),
      '\t foo bar \n\r'.strip(), sep='\n')

s3 = 'foo,bar,boo'
print(s3.split(',', 1), s3.rsplit(',', 1),
      s3.partition(','), s3.rpartition(','), sep='\n')

# Сравнение времени выполнения
lt = list('fdhjglsktsmesrn')

start = time.perf_counter()
print(''.join(lt))
print(time.perf_counter() - start)

start = time.perf_counter()
stest = ''
for i in lt:
    stest += i
    
print(stest)
print(time.perf_counter() - start)


print('foobar'.startswith(('foo', 'boo')))

"""
.find('', 0, 3)
.indes('', 0, 3)
.rfind('', 0, 3)  # поиск последнего вхождения
.rindex('', 0, 3)
"""

translation_map = {ord('a'): '*', ord('b'): '?'}
print('abracadabra'.translate(translation_map))

"""
.islower()
.isupper()
.istitle()  
.isspace()
"""

print(ascii('ыtring'))
print('{!s} (str)'.format('I\'m a map'),
      '{!r} (repr)'.format('I\'m a map'),
      '{!a} (ascii)'.format('I\'m a map'),
      sep='\n')

print('{:_^20}'.format('A dooomsday'))
print('int: {0:d}  hex {0:x}  oct {0:o}  bin {0:b}'.format(43))
print('{:+07.1f}'.format(-42.45))
print('{0!r:->14}'.format('foo bar'))

print('{0} {1} {0}'.format('hi', 'origato'))
print('{0}, {who}, {0}'.format('hello', who='Uncle Ben'))
tp = 0, 13, 9.6
print('x = {0[0]}, y = {0[1]}, z = {0[2]:.2f}'.format(tp))
tp = {'x': 0, 'y': 13, 'z': 9.6}
print('z = {0[z]}, y = {0[y]}, x = {0[x]}'. format(tp))

# string
print(string.ascii_letters, string.digits,
      string.punctuation, repr(string.whitespace), sep='\n')

# Байты
print(b'1213\n', rb'2324\n')
print('щпвлзщп 51'.encode('cp1251').decode('utf-8', errors='ignore'))
print('щпвлзщп 51'.encode('cp1251').decode('utf-8', errors='replace'))
print(sys.getdefaultencoding())

print(b'foo' in b'foobar')

# Файлы
"""
open('scs.db', 'r+b', errors='ignore')  # Открыть бинарный файл 
# для чтения и записи
open('rfij.txе', 'x')  # Создать новый текстовый файл 
# в системной кодировке и открыть его для записи

.write('')  # Записать строку
.writelines(['gg', 'wp'])  # Записать последовательность строк

.filend()  # номер файлового дескриптора
.tell()  # смещение в файле (на сколько вы его изменили), текущий индекс

.seek(8)
.tell()  # 8

.flush()  # сброс буфера (в котором временно храниться файл)


 Потоки вывода
 
sys.stdin  # ввод
sys.stdout  # вывод
sys.stderr  # поток ошибок (исключений)
"""

print(*range(10), file=open('example.txt', 'w'), flush=True)

# io
handle = io.StringIO('foo\n\bar')
print(handle.readline())
handle.write('boo')
print(handle.getvalue())

handle = io.BytesIO(b'foobar')
print(handle.read(3))
print(handle.getvalue())
