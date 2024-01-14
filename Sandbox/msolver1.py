import math


pi = math.pi
a = int(input('Введите 1, если нужно найти sin, '
              '2 - cos, 3 - tg, 4 - ctg: '))
b = int(input('Ввод значений в градусах - 1,\n 2 - в радианах: '))
if b == 1:
    znach = 'градусах (целые числа): '
else:
    znach = '''радианах, используя шаблон \n
    pi / или * число \n (pi - число пи; / и * - деление и умножение;
    \n число - ваше число, на которое нужно разделить или умножить.)
    \n Ну или просто введите число (автоматически умноженное на pi): '''
    
c = input('Введите значение в ' + znach)
if b == 1:  # Если введены градусы
    dgrs = int(c) * (pi / 180)
    if a == 1:
        print('sin ' + c + ' = '
              + str(round(math.degrees(math.sin(dgrs)))))
    elif a == 2:
        print('cos ' + c + ' = ' +
              str(round(math.degrees(math.cos(dgrs)))))
    elif a == 3:
        if int(c) % 180 != 90:
            print('tg ' + c + ' = '
                  + str(round(math.degrees(math.tan(dgrs)))))
        else:
            print('tg ' + c + ' = infinity')
    elif a == 4:
        if int(c) % 180 != 0:
            print('ctg ' + c + ' = ' +
                  str(1 / math.degrees(math.tan(dgrs))))
        else:
            print('ctg ' + c + ' = infinity')
else:  # если введены радианы
    # Преобразуем строку в число
    if c.find('pi') != -1:
        ans = 1
        i = 0
        j = 0
        while '/' in c[i:] or '*' in c[i:]:
            if ('/' not in c[i:] or (' * ' in c[i:]
                and c[i:].index('*') < c[i:].index('/'))) \
               and c[i:].count(' ') > 2:
                i = c[i:].index('* ') + 2
                j = c[i + 1:].index(' ') + 1
                ans *= int(c[i:i + j])
            
            if ('*' not in c[i:]
                or (' / ' in c[i:]
                and c[i:].index('/') < c[i:].index('*'))) \
               and c[i:].count(' ') > 2:
                i = c[i:].index('/ ') + 2
                j = c[i + 1:].index(' ') + 1
                ans /= int(c[i: i + j])
            
            if c[i:].count(' ') == 2:
                i = c[i:].rindex(' ') + 1
                ans *= int(c[i:]) if c[i - 2] == '*' else 1 / int(c[i:])
                break
        
        c = ans
    else:
        c = int(c)
    
    if a == 1:
        print('sin ' + str(c) + ' = '
              + str(round(math.degrees(math.sin(c * pi)))))
    elif a == 2:
        print('cos ' + str(c) + ' = ' +
              str(round(math.degrees(math.cos(c * pi)))))
    elif a == 3:
        if (2 * c) % 3 != 1 or (2 * c) % 4 != 3:
            print('tg ' + str(c) + ' = '
                  + str(round(math.degrees(math.tan(c * pi)))))
        else:
            print('tg ' + str(c) + ' = infinity')
    elif a == 4:
        if c - math.trunc(c) == 0:
            print('ctg ' + str(c) + ' = ' +
                  str(1 / math.degrees(math.tan(c * pi))))
        else:
            print('ctg ' + str(c) + ' = infinity')
