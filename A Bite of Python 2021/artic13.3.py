# Программа для создания резервной копии указанных файлов v.3.0

import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать,
# собираются в список.

print('Укажите путь к копируемым файлам (например, \\C:\\User '
      'или в двойных кавычках "\\C:\\Program files", '
      'если в файле есть пробелы),\n'
      'а когда закончите, напишите "---": ')

filer = []
while True:
    fl = input('')
    if fl == '---':
        for f in filer:
            if f.startswith('C:\\'):
                pass
            else:
                filer.remove(f)
                
        break
        
    filer.append(fl)

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup'

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%Y%m%d')

# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' \
             + comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
    print('Каталог успешно создан', today)

# Имя zip-файла
target = today + os.sep + now + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "\"C:\Program Files\\7-Zip\\7z.exe\" \
a -tzip -ssw -mx1 -r0 {0} {1}".format(target, ' '.join(filer))

# Запускаем создание резервной копии
print(zip_command)
print(os.system(zip_command))
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

'''
 Внесём это исправление в нашу программу. 
Коррекция программы при обнаружении ошибок 

bug fixing – устранение «багов», исправление ошибок
'''
