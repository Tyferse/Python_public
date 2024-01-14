"""
 Математика: Все главные формулы

 Все операции в модуле имеют следующте обозначения:

  "*" - умножение

  "/" - деление (или дробная черта)

  "+" - сложение

  "-" - вычитание

  "**" - возведение в степень (**.5 (или **0.5) - квадратный корень)

  "=", ">", "<", ">=", "<=" - равенство, больше, меньше,
  больше или равно, меньше или равно

  "а" - переменная с именем а

  "а2" - переменная а с нижним обозначением 2

  "23а" - 23 * а
"""

import math


__version__ = 'alpha 6.0'

symbs1 = [') * ', ' * (', ') + ', ' + (', ') - ', ' - (',
          ' * ', ' + ', ' - ', ') / ', ' / (', ' / ']

symbs2 = ['+', '-', '*', '//', '%']


def vartype(var: str) -> str:
    """
    Returns a string of a type of variable.

    'int' - integer
    12;

    'float' - real / number with floating point
    12.0;

    'var' - one/two alphabetical/alpha-numeric characters
    which are a variable
    n1;

    'numvar' - variable with number in front of characters
    12n1;

    'brac' - expression in parentheses (brackets)
    (n-8);

    'frac' - fraction (has '/' character)
    12/n1;

    'pow' - number / expression with '**' character
    n1**2;

    'exp' - expression with multiple operators and variables
    out of parentheses
    6x + 12y - 9.
    """
    assert var, print(var)  # Должно бы ть введено хоть что-то

    var = str(var)
    if var.startswith(' '):
        # Уничтожение лишних пробелов в начале
        while var[0] == ' ':
            var = var[1:]

    if var.startswith('-'):
        # Уборка минуса
        var = var[1:]

    if var.startswith('(') and not var.endswith(')'):
        # Уборка ненужных скобок
        var = var[1:]

    if not var.startswith('(') and var.endswith(')') \
            and '**(' not in var:
        var = var[:-1]

    if var.isdigit():
        # Если строка является целым числом
        return 'int'
    elif '.' in var and not var[-2:].isalpha():
        # Если сторока содержит цифры и одну точку -
        # это десятичная дробь
        i = var.index('.')
        var = var[0:i] + var[i + 1:]
        if var.isdigit():
            return 'float'
    elif len(var) < 3:
        # Если строка 1-2 символа содержит в начале только буквы -
        # является переменной
        if len(var) == 1 and var.isalpha():
            return 'var'
        elif len(var) == 2 and var[0].isalpha() and var[1].isalnum():
            return 'var'

    if var[-1].isalpha():
        try:
            var = float(var[:-1])
            return 'numvar'
        except ValueError:
            pass
    elif len(var) >= 2:
        if '**' not in var and var[-2].isalpha() and var[-1].isalnum():
            # Если нет степени и последний/ие символы
            # являиются переменной, а остальные символы чилом -
            # переменна с числом
            try:
                var = float(var[:-2])
                return 'numvar'
            except ValueError:
                pass

    # Проверка на наличие символов операций между чисел
    test = [True if symb in var else False for symb in symbs1]
    if any(test) and ')**' not in var:
        # Если нет степени и хотя бы один сивол операции присутствует -
        # является выражением
        return 'exp'

    test2 = [True if symb in var else False for symb in symbs2]
    if var.startswith('(') and var.endswith(')') and ')**' not in var \
            and not any(test) and any(test2):
        # Если окружено круглыми скобками и нет степени -
        # является выражением в скобках
        return 'brac'

    if var.find('/') != -1 or var.find(')/') != -1:
        # Если есть знак деления между числами - является дробью
        return 'frac'

    if var.find(')**') != -1 or var.find('**') != -1:
        # Если если степень - является числом/выражением в степени
        return 'pow'

    if __name__ == '__main__':
        mas = ['(', ')', ')**', *symbs1, *symbs2, '**', '/', ')/']
        for m in mas:
            print(var.find(m), m)

    # Если ничего не возвращает, выбрасывается исключение
    raise ValueError('Got invalid variable: ', var)


print(vartype('n**(2/n)'), 34 // 5)


def varoper(var: str, oper: str, num: str,
            count=True, flround=None) -> str or float or int:
    """
    Got variable, operation and number, that will operate
    with variable.

    Returns converted variable, if it's possible,
    otherwise returns template of expression.

    oper - takes only 7 operations: '+', '-', '*', '/', '//', '%', '**'
    (addition, subtraction, multiplication, division, floored division,
    remainder of division, exponentiation)

    count - if True, all results only with numbers will be evaluated
    (eval() function).

    flround - all numbers with floating point will be rounded to value
    with current number from comma (round() function).
    """

    assert oper in ('+', '-', '*', '/', '%', '//', '**'), \
        'Operation ' + oper + ' doesn\'t supported '
    # Поддерживаются только указанные операции

    var = str(var)
    num = str(num)
    type1 = vartype(var)  # Определение типов операндов
    type2 = vartype(num)
    s1 = s2 = False  # Определение отрицательных переменных
    if var.startswith('-'):
        if var[1] == '(' and var.endswith(')'):
            s1 = True
        elif var == 'exp':
            pass
        else:
            s1 = True

    if num.startswith('-'):
        if num[1] == '(' and num.endswith(')'):
            s2 = True
        elif num == 'exp':
            pass
        else:
            s2 = True

    # Создание списков типов по группам
    varl = ('var', 'numvar', 'brac', 'frac', 'pow')
    digl = ('int', 'float')
    allty = list(digl) + list(varl)

    if count:
        # Здесь выполняются все типовые операции над любыми числами,
        # при определённых условиях
        if s1 or s2:
            # and var not in ('frac', 'pow')
            # and num not in ('frac', 'pow')
            # Взаимодействие между операндами,
            # если хотя бы один из них является отрицательным
            # и они не являются дробью или числом в степени
            if not s1 and s2:
                # Если первый полозительный, а второй отрицательный
                if oper == '-':
                    return varoper(var, '+', num[1:])
                elif oper == '+':
                    return varoper(var, '-', num[1:])
                elif oper in ('*', '/', '//', '%'):
                    m = varoper(var, oper, num[1:])
                    if m.startswith('-'):
                        return m[1:]

                    return f'-{m}'
                elif oper == '**':
                    # Если степень отрицательная,
                    # то вывод представляется,
                    # как единица делённая на число
                    # в положительной степени (а**-1 = 1/а**1)
                    m = varoper(var, '**', num[1:])
                    q = varoper('1', '/', m)
                    return q

            elif s1 and not s2:
                # Если первый отрицательный, а второй положительный
                if oper in ('-', '*', '/', '//', '%'):
                    if oper == '-':
                        m = varoper(var[1:], '+', num)
                        m = '-' + str(m)
                    else:
                        m = varoper(var[1:], oper, num)

                    if vartype(str(m)) != 'exp' \
                            or (m[0] == '(' and m[-1] == ')'):
                        if str(m).startswith('-'):
                            return str(m)[1:]

                        return '-' + str(m)

                elif oper == '+':
                    m = varoper(num, '-', var[1:])
                    return m
                elif oper == '**':
                    if num in digl:
                        m = eval(num + '%2')
                        q = varoper(var[1:], '**', num)
                        if m == 0:
                            return q
                        elif q.startswith('-'):
                            return q[1:]

                        return '-' + q

                    return varoper('(' + var + ')', oper, num)

            elif s1 and s2:
                # Если оба отрицательные
                if oper == '-':
                    m = varoper(num, '-', var[1:])
                    return m
                elif oper == '+':
                    m = varoper(var[1:], oper, num[1:])
                    return varoper('-1', '*', m)
                elif oper in ('*', '/', '//', '%'):
                    # Минус на минус даёт плюс
                    m = varoper(var[1:], oper, num[1:])
                    return m
                elif oper == '**':
                    if num in digl:
                        m = eval(num + '%2')
                        q = varoper(var[1:], '**', num[1:])
                        r = varoper('1', '/', q)
                        if m == 0:
                            return r
                        elif r.startswith('-'):
                            return r[1:]

                        return '-' + r

                    m = varoper(var, '**', num[1:])
                    q = varoper('1', '/', m)
                    return q

        if var == num:
            # Если оба равны
            if oper == '+':
                return varoper('2', '*', num)
            elif oper in ('-', '%'):
                return 0
            elif oper == '*':
                return varoper(var, '**', '2')
            elif oper in ('/', '//'):
                return 1

        if num in ('0', '0.0', '-0', '-0.0'):
            # Если второй операнд - ноль
            if oper in ('+', '-'):
                return var
            elif oper == '*':
                return 0
            elif oper in ('/', '//', '%'):
                raise ZeroDivisionError
            elif oper == '**':
                return 1

        elif num == '1' or num == '1.0':
            # Если второй операнд - единица
            if oper in ('*', '/', '//', '**'):
                return var

        elif var == '1' or var == '1.0':
            # Если первый операнд - единица
            if oper == '*':
                return num
            elif oper == '**':
                return 1

        elif var in ('0', '0.0', '-0', '-0.0'):
            # Если первый операнд - ноль
            if oper in ('+', '-'):
                if oper == '+':
                    return num
                elif oper == '-':
                    return varoper('-1', '*', num)

            elif oper in ('*', '/', '//', '%', '**'):
                if oper == '**' and num != '0' and num != '0.0':
                    return 0

                return 0

    if type1 in allty and (type2 == 'brac' or type2 == 'exp'):
        if type2 == 'exp':
            # Если вторым операндом является выражение,
            # а первым - любой другой тип
            if num.startswith('(') and num.endswith(')'):
                if oper in ('//', '%', '**'):
                    return f'{var}{oper}{num}'

            if oper in ('//', '%', '**'):
                return f'{var}{oper}({num})'

        elif type2 == 'brac':
            # Если вторым операндом является выражение в скобках,
            # а первым - любой другой тип
            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                if var.startswith('(') and var.endswith(')'):
                    return f'{var}{oper}{num}'

                return f'({var}){oper}{num}'

    elif type2 in allty:
        if type1 == 'exp':
            # Первым операндом является выражение,
            # а вторым любой другой тип
            if var.startswith('(') and var.endswith(')'):

                if oper in ('//', '%', '**'):
                    return f'{var}{oper}{num}'

            if oper in ('//', '%', '**'):
                return f'({var}){oper}{num}'

        elif type1 == 'brac':
            # Первым операндом является выражение в скобках,
            # а вторым любой другой тип
            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                if num in digl:
                    return f'{var}{oper}{num}'

                return f'{var}{oper}({num})'

    if type1 == 'int' or type1 == 'float':
        if type2 == 'int' or type2 == 'float':
            # С числами всё просто считается
            if count:
                return eval(var + oper + num)

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return var + oper + num

        elif type2 == 'var':
            # При умножении на переменную возвращается
            # переменная с числом
            if oper == '*':
                return str(var) + num

            if oper in ('+', '-'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return var + oper + num

        elif type2 == 'numvar':
            # При взаимодействии с переменной с числом
            # с начала идут действия с числовой частью,
            # если это не слижение или вычитание
            if num[-2].isalpha():
                i = -2
            elif num[-1].isalpha():
                i = -1

            if oper in ('*', '/', '%', '//') and count:
                m = eval(str(var) + oper + num[:i])
                if m == 1 and oper == '*':
                    return num[i:]
                elif oper == '*':
                    return f'{m}{num[i:]}'

                return f'{m}{oper}{num[i:]}'
            elif oper == '**' and count:
                m = eval(str(var) + oper + num[:i])
                return f"{m}**{num[i:]}"

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'{var}{oper}{num}'

        elif type2 == 'frac':
            numul = num.split('/', 1)
            typen1 = vartype(numul[0])
            typen2 = vartype(numul[1])
            if oper == '*':
                # При умножении сначала идёт умножение на числитель,
                # потом деление на знаменатель
                if typen1 in digl and typen2 in varl:
                    if count:
                        m = eval(var + oper + numul[0])
                    else:
                        m = var + oper + numul[0]

                    return f'({m})/{numul[1]}'
                elif typen2 in digl and typen1 in varl:
                    if count:
                        if float(var) > float(numul[1]):
                            m = eval(var + '/' + numul[1])
                            return f'{m} * {numul[0]}'
                        else:
                            m = eval(numul[1] + '/' + var)
                            return f'{numul[0]}/{m}'

                    m = var + '/' + numul[1]
                    return f'({m}) * {numul[0]}'
            elif oper == '/':
                # ПРи делении дробь заменяется обратной
                # и происходит то же, что и с умножением
                if ')/(' in num \
                        or (('/' in num or ')/' in num or '/(' in num)
                            and typen1 in varl and typen2 in varl):
                    num = '/'.join(numul[::-1])
                    return f'{var} * {num}'
                elif ')/' in num:
                    if typen2 in digl:
                        if count:
                            m = eval(var + '*' + numul[1])
                            return f'{m}/{numul[0]}'

                        m = var + '*' + numul[1]
                        return f'({m})/{numul[0]}'
                elif '/(' in num:
                    if typen1 in digl:
                        if count:
                            m = eval(var + '/' + numul[0])
                            return f'{m} * {numul[1]}'

                        m = var + '/' + numul[0]
                        return f'({m}) * {numul[1]}'
                elif '/' in num:
                    if typen2 in digl and typen1 in digl and count:
                        return eval(f'{var} / ({num})')
                    elif typen2 in digl and typen1 in varl:
                        if count:
                            m = eval(var + '*' + numul[1])
                            return f'{m}/{numul[0]}'

                        m = var + '*' + numul[1]
                        return f'({m})/{numul[0]}'
                    elif typen2 in varl and typen1 in digl:
                        if count:
                            m = eval(var + '/' + numul[0])
                            return f'{m} * {numul[1]}'

                        m = var + '/' + numul[0]
                        return f'({m}) * {numul[1]}'
            elif oper == '**':
                # Если второй операнд является числам в степени числа,
                # выполняется простое вычисление
                if typen1 in digl and typen2 in digl and count:
                    m = eval(num)
                    return f'{var}**{m}'

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '**', '//', '%'):
                return f'{var}{oper}({num})'

        elif type2 == 'pow':
            nump = num.split('**', 1)
            typen = vartype(nump[0])
            typep = vartype(nump[1])
            # Выполняются типичные действия с числами в степени
            # в некоторых случаях
            if nump[0] == '1' or nump[0] == '1.0':
                m = varoper(var, oper, '1')
                return m
            elif (nump[0] == '0' or nump[0] == '0.0') \
                    and nump[1] != '0' and nump[1] != '0.0':
                m = varoper(var, oper, '0')
                return m
            elif nump[1] == '1.0' or nump[1] == '1' and count:
                m = varoper(var, oper, nump[0])
                return m
            elif nump[1] == '0.0' or nump[1] == '0':
                m = varoper(var, oper, '1')
                return m

            if typen == 'numvar' and count:
                # Если переменная в степени совмещена с числом,
                # то с начала выполняются операции над числами
                if nump[0][-2].isalpha():
                    j = -2
                elif nump[0][-1].isalpha():
                    j = -1

                if oper in ('*', '/'):
                    m = eval(var + oper + nump[0][:j])
                    q = varoper(m, oper, nump[0][j:] + '**' + nump[1])
                    return q

            if typen in digl and typep in digl and count:
                # Если число в степени числа, выполняется вычисление
                m = eval(num)
                return eval(var + oper + m)

            elif typen in digl and typep in varl and count:
                # Если степень не является числом,
                # при умножении/делениии чисел
                # с одинаковым основанием степени суммируются/отнимаются
                if var == nump[0]:
                    if oper == '*':
                        return f'{var}**({nump[1]}+1)'
                    elif oper == '/':
                        return f'{var}**(1-{nump[1]})'

            elif oper == '*' and typen == 'var' and count:
                # При умножении числа на переменную степени,
                # выводиться переменная в сепени с числом
                return str(var) + num

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'{var}{oper}({num})'

    elif type1 == 'var':
        if type2 in ('int', 'float'):
            if oper == '*':
                # При умножении числа на переменную
                # выводится переменная с числом
                return num + str(var)
            elif oper in ('/', '//', '%', '**'):
                return f'{var}{oper}{num}'
            elif oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'

        elif type2 == 'var':
            if oper in ('/', '//', '%', '**'):
                return f'{var}{oper}{num}'
            elif oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'

        elif type2 == 'numvar':
            if num[-2].isalpha():
                i = -2
            elif num[-1].isalpha():
                i = -1

            if var == num[i:] and count:
                # Если переменные в операндах одинаковые
                if oper == '+':
                    n = str(float(num[:i]) + 1)
                    if n == 0:
                        return 0

                    return n + var
                elif oper == '-' and count:
                    n = str(1 - float(num[:i]))
                    if n == 0:
                        return 0

                    return n + var
                elif oper == '*':
                    return num[:i] + var + '**2'
                elif oper == '/':
                    return '1/' + num[:i]

            if oper in ('/', '//', '%', '**'):
                return f'{var}{oper}{num}'
            elif oper in ('+', '-'):
                return f'{var} {oper} {num}'
            elif oper == '*':
                return f'{num} * {var}'

        elif type2 == 'frac':
            numul = num.split('/', 1)
            typen1 = vartype(numul[0])
            typen2 = vartype(numul[1])
            # Если числитель и/или знаменатель
            # являются выражениями в скобках,
            # то они преобразуются в обычные выражения
            if typen1 == 'brac':
                s = numul[0][1:len(numul[0])]
                numul[0] = ''
                for c in s:
                    if c not in symbs2:
                        numul[0] += c
                    else:
                        numul[0] += f' {c} '
            elif typen2 == 'brac':
                s = numul[1][1:len(numul[1])]
                numul[1] = ''
                for c in s:
                    if c not in symbs2:
                        numul[1] += c
                    else:
                        numul[1] += f' {c} '

            if typen1 in varl and typen2 in varl:
                # Если и числитель, и знаменатель являются переменными,
                # то происходит взаимодействие с начала с числителем,
                # потом с знаменателем
                if numul[0] == numul[1]:
                    n = varoper(var, oper, '1')
                    return n
                elif numul[0] == var:
                    if oper == '*':
                        return varoper(var, '*', numul[0]) + '/' \
                               + numul[1]
                    elif oper == '/':
                        # Если Числитель равен первому операнду,
                        # то при делении они сокращаются
                        return numul[1]

                elif numul[1] == var:
                    if oper == '*':
                        # Если первый операнд равен знаменателю,
                        # то при умножении они сокращаются
                        return numul[0]
                    elif oper == '/':
                        return varoper(var, '*', numul[1]) + '/' \
                               + numul[0]

            elif typen1 in digl and typen2 in varl:
                if var == numul[1]:
                    if oper == '*':
                        return numul[0]
                    elif oper == '/':
                        return f'({var}**2)/{numul[0]}'

            elif typen1 in varl and typen2 in digl:
                if var == numul[0]:
                    if oper == '*':
                        return f'{var}**2/{numul[1]}'
                    elif oper == '/':
                        return numul[1]

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'{var}{oper}({num})'

        if type2 == 'pow':
            nump = num.split('**', 1)
            typen = vartype(nump[0])
            typep = vartype(nump[1])
            if typen in digl and typep in digl and count:
                # Если второй операнд - это число в степени числа,
                # то взаимодействае с ними такое же, что и с числами
                m = eval(num)
                if oper in ('+', '-'):
                    return f'{var} {oper} {m}'
                elif oper == '*':
                    return m + var
                elif oper in ('/', '//', '%', '**'):
                    return f'{var}{oper}{m}'

            elif typen in varl and typep in digl and count:
                if nump[0] == var:
                    if oper == '*':
                        m = float(nump[1]) + 1
                        if m == 0:
                            return 1
                        elif m == 1:
                            return var

                        return var + '**' + str(m)
                    elif oper == '/':
                        m = 1 - float(nump[1])
                        if m == 0:
                            return 1
                        elif m == 1:
                            return var

                        return var + '**' + str(m)

            elif typen in varl and typep in varl:
                if nump[0] == var:
                    if oper == '*':
                        m = varoper(nump[1], '+', '1')
                        return f'{var}**({m})'
                    elif oper == '/':
                        m = varoper('1', '-', nump[1])
                        return f'{var}**({m})'

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'{var}{oper}({num})'

    elif type1 == 'numvar':
        if var[-2].isalpha():
            i = -2
        elif var[-1].isalpha():
            i = -1

        varn = var[:i]
        varv = var[i:]
        if type2 == 'int' or type2 == 'float':
            if oper in ('//', '%') and count:
                m = eval(varn + oper + num)
                # Если число с переменной равно одному или нулю
                if m == 0:
                    return 0
                elif m == 1:
                    return varv

            elif oper == '/' and count:
                # Если делитель больше делимого, возвращается дробь,
                # если делимое больше делителя,
                # возвращается переменная с числом
                s = False
                if float(varn) > float(num):
                    m = eval(varn + oper + num)
                else:
                    m = eval(num + oper + varn)
                    s = True

                if m == 1:
                    return varv
                elif m == 0:
                    return 0
                elif s:
                    return f'{varv}/{m}'

                return f'{m}{varv}'
            elif oper == '*' and count:
                m = eval(varn + oper + num)
                if m == 1:
                    return varv
                elif m == 0:
                    return 0

                return f'{m}{varv}'
            elif oper == '**' and count:
                m = eval(varn + oper + num)
                if m == 1:
                    return varv + '**' + num
                elif m == 0:
                    return 0

                return f'{m}{varv}**{num}'

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'{var}{oper}{num}'

        elif type2 == 'var':
            if varv == num and count:
                if oper in ('+', '-'):
                    m = eval(varn + oper + '1')
                    if m == 1:
                        return varv
                    elif m == 0:
                        return 0

                    return f'{m}{varv}'
                elif oper == '*':
                    return f'{var}**2'
                elif oper in ('/', '//'):
                    return varn
                elif oper == '%':
                    return 0

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%'):
                return f'{var}{oper}{num}'
            elif oper == '**':
                return f'({var})**{num}'

        elif type2 == 'numvar':
            if num[-2].isalpha():
                j = -2
            elif num[-1].isalpha():
                j = -1

            numn = num[:j]
            numv = num[j:]
            if varv == numv:
                # Если переменные в операндах совпадают
                if oper in ('+', '-') and count:
                    m = eval(varn + oper + numn)
                    if m == 1:
                        return varv
                    elif m == 0:
                        return 0

                    return f'{m}{varv}'
                elif oper == '*' and count:
                    m = eval(varn + '*' + numn)
                    if m == 1:
                        return varv + '**2'
                    elif m == 0:
                        return 0

                    return f'{m}{varv}**2'
                elif oper in ('/', '//'):
                    if count:
                        m = eval(varn + oper + numn)
                    else:
                        m = varn + oper + numn

                    return m
                elif oper == '%' and count:
                    return 0

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%'):
                return f'{var}{oper}{num}'
            elif oper == '**':
                return f'({var})**{num}'

        elif type2 == 'frac':
            numul = num.split('/', 1)
            numn1 = numul[0]
            numn2 = numul[1]
            typen1 = vartype(numn1)
            typen2 = vartype(numn2)
            if typen1 in digl and typen2 in digl and count:
                if oper == '*':
                    m = eval(num)
                    q = eval(varn + oper + m)
                    if q == 1 or q == 1.0:
                        return varv
                    elif q == 0 or q == 0.0:
                        return 0

                    return f'{q}{varv}'
                elif oper == '/':
                    m = eval(varn + '*' + numn2)
                    q = eval(m + '/' + numn1)
                    if q == 1:
                        return varv
                    elif m == 0:
                        return 0

                    return f'{q}{varv}'
                elif oper in ('//', '%', '**'):
                    m = varoper(var, oper, str(eval(num)))
                    return m

            elif typen1 in digl and typen2 in varl and count:
                if var == numn2:
                    if oper == '*':
                        return numn1

                if oper == '*':
                    m = varoper(var, '*', numn1)
                    q = varoper(m, '/', numn2)
                    return q
                elif oper == '/':
                    m = varoper(var, '*', numn2)
                    q = varoper(m, '/', numn1)
                    return q

            elif typen1 in varl and typen2 in digl and count:
                if var == numn1:
                    if oper == '*':
                        m = varoper(var, '*', numn1)
                        return f'{m}/{numn2}'
                    elif oper == '/':
                        return numn2

                if oper == '*':
                    m = varoper(var, '/', numn2)
                    q = varoper(m, '*', numn1)
                    return q
                elif oper == '/':
                    m = varoper(var, '*', numn2)
                    q = varoper(m, '/', numn1)
                    return q

            elif typen1 in varl and typen2 in varl and count:
                if numn1 == numn2:
                    m = varoper(var, oper, '1')
                    return m
                elif var == numn1:
                    if oper == '/':
                        return numn2

                elif var == numn2:
                    if oper == '*':
                        return numn1

                if oper == '*':
                    m = varoper(var, '*', numn1)
                    q = varoper(m, '/', numn2)
                    return q
                elif oper == '/':
                    m = varoper(var, '*', numn2)
                    q = varoper(m, '/', numn1)
                    return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%'):
                return f'{var}{oper}({num})'
            elif oper == '**':
                return f'({var})**({num})'

        elif type2 == 'pow':
            numpw = num.split('**', 1)
            numn = numpw[0]
            nump = numpw[1]
            typen = vartype(numn)
            typep = vartype(nump)
            # Некоторые типичные операции с числами в степени
            if typen in digl and typep in digl and count:
                if eval(num) == 1:
                    return var
                elif eval(num) == 0:
                    return 1
                elif oper in ('*', '/'):
                    m = eval(varn + oper + num)
                    if m == 1:
                        return varv
                    elif m == 0:
                        return 0

                    return str(m) + varv
                elif oper == '//':
                    m = eval(num)
                    q = eval(varn + '//' + m)
                    if q == 1:
                        return varv
                    elif q == 0:
                        return 0

                elif oper == '%':
                    m = eval(varn + '%' + num)
                    if m == 1:
                        return varv
                    elif m == 0:
                        return 0

                elif oper == '**':
                    m = eval(num)
                    q = eval(varn + '**' + m)
                    return f'{q}{varv}**{m}'

            elif typen in digl and typep in varl:
                # Ещё одни шаблонные операции с числами в степени
                if numn == '1' or numn == '1.0':
                    m = varoper(var, oper, '1')
                    return m
                elif numn == '0' or numn == '0.0':
                    m = varoper(var, oper, '0')
                    return m

            elif typen in varl and typep in digl and count:
                # Последние типичные операции с числами в степени
                # в паре случаев
                if float(nump) == 1.0:
                    m = varoper(var, oper, numn)
                    return m
                elif float(nump) == 0.0:
                    m = varoper(var, oper, '1')
                    return m

                if numn == varv:
                    if oper == '*':
                        m = varoper('1', '+', nump)
                        if m == 1:
                            return var
                        elif m == 0:
                            return 0

                        return f'{varn}{varv}**{m}'
                    elif oper == '/':
                        if float(nump) > 1:
                            m = eval('1 - ' + nump)
                            if m == 1:
                                return f'{varn}/{numn}'
                            elif m == 0:
                                return varn

                            return f'{varn}/{numn}**{m}'
                        elif float(nump) < 1:
                            m = eval('1 + ' + nump)
                            if m == 1:
                                return f'{varn}/{numn}'
                            elif m == 0:
                                return varn

                            return f'{varn}{varv}**{m}'
                        elif float(nump) == 1:
                            return varn

            elif typen in varl and typen in varl:
                if numn == varv:
                    if oper == '*':
                        m = varoper(nump, '+', '1')
                        return f'({var})**({m})'
                    elif oper == '/':
                        m = varoper('1', '-', nump)
                        return f'({var})**({m})'

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'({var}){oper}({num})'

    if type1 == 'exp':
        cmn = ('+', '-')
        spc = ('*', '/')
        expl = var.split()

        # Проверка на принадлежность всех операций одному типу
        iscmn = any([True if s in cmn else False for s in expl[1::2]])
        isspc = all([True if s in spc else False for s in expl[1::2]])

        changed = False
        # Создаются списки основных операций

        assert len(expl) >= 2, var + ' might not an expression.'

        for n in expl:
            # Первый обход списка членов выражения
            if n in list(cmn) + list(spc) + ['//', '%']:
                # Если является операцией, пропускается
                continue

            if num == n and not changed:
                # Если второй операнд соответствует элементу выражения
                i = expl.index(n)
                if iscmn and oper in cmn:
                    # И опрерация, и все символы операций в выражении
                    # являются  или сложением, или вычитанием
                    if 0 < i < len(expl) - 1 and len(expl) >= 5:
                        # Если элемент находиться
                        # в центральной части выражения,
                        # то учитываются знаки вокруг него
                        if oper == '+':
                            expl[i] = str(varoper('2', '*', n))
                            changed = True  # Если произошло изменение,
                            #                 выполнение завершилось
                        elif oper == '-':
                            if expl[i + 1] == '-':
                                expl[i + 2] = '-' + expl[i + 2]
                                del expl[i - 1:i + 2]
                            elif expl[i + 1] == '+':
                                del expl[i - 1:i + 1]

                            changed = True

                    elif 0 == i:
                        # Если элемент находиться в первой позиции,
                        # то учитывается знак после него
                        if oper == '+':
                            expl[i] = str(varoper('2', '*', n))
                            changed = True
                        elif oper == '-':
                            if expl[i + 1] == '-':
                                del expl[i:i + 2]
                                expl[0] = '-' + expl[0]
                            else:
                                del expl[i:i + 2]

                            changed = True

                    elif i == len(expl) - 1:
                        # Если элемент находиться в конце,
                        # учитывается знак перед ним
                        if expl[i - 1] == oper:
                            expl[i] = str(varoper('2', '*', n))
                        elif oper != expl[i - 1]:
                            del expl[i - 1:]

                        changed = True

                elif isspc and oper in spc:
                    # И операция, и все операции в выражении
                    # являются умножением или делением
                    if 0 < i < len(expl) - 1:
                        if expl[i - 1] == '*' and expl[i + 1] == '*':
                            if oper == '/':
                                del expl[i - 1:i + 1]
                            elif oper == '*':
                                expl[i] = str(varoper(n, '**', '2'))

                            changed = True
                        elif expl[i - 1] == '*' and expl[i + 1] == '/':
                            if oper == '*':
                                expl[i] = str(varoper(n, '**', '2'))
                            elif oper == '/':
                                del expl[i - 1:i + 1]

                            changed = True
                        elif expl[i - 1] == '/' and expl[i + 1] == '*':
                            if oper == '*':
                                del expl[i:i + 2]
                            elif oper == '/':
                                expl[i] = str(varoper(n, '**', '2'))

                            changed = True
                        elif expl[i - 1] == '/' and expl[i + 1] == '/':
                            if oper == '*':
                                expl[i - 2] = str(varoper(expl[i - 2],
                                                          oper, num))
                            elif oper == '/':
                                expl[i] = str(varoper(n, '**', '2'))

                            changed = True

                    elif expl[i - 1] in spc and i == len(expl) - 1:
                        if oper == '*' and expl[i - 1] == '*':
                            expl[i] = str(varoper(n, '**', '2'))
                        elif oper == '*' and expl[i - 1] == '/':
                            del expl[i - 1:]
                        elif oper == '/' and expl[i - 1] == '*':
                            del expl[i - 1:]
                        elif oper == '/' and expl[i - 1] == '/':
                            expl[i] = str(varoper(n, '**', '2'))

                        changed = True
                    elif i == 0:
                        if oper == '*' and expl[i + 1] == '*':
                            expl[i] = str(varoper(n, '**', '2'))
                        elif oper == '*' and expl[i + 1] == '/':
                            expl[i] = varoper(n, '**', '2')
                        elif oper == '/' and expl[i + 1] == '*':
                            del expl[i:i + 2]
                        elif oper == '/' and expl[i + 1] == '/':
                            del expl[i:i + 2]

                        changed = True

        for n in expl:
            # Второй обход списка членов выражения
            if n in list(cmn) + list(spc) + ['//', '%']:
                continue

            if ((vartype(n) in digl + ('numvar', 'frac', 'pow')
                 and type2 in digl + ('numvar', 'frac', 'pow'))
                or (vartype(n) in varl and type2 in varl)) \
                    and not changed:
                # Если и элемент, и второй операнд
                # принадлежат к одним и тем же типам
                i = expl.index(n)
                if iscmn and oper in cmn:
                    if len(expl) >= 5:
                        if 0 < i < len(expl) - 1 \
                                and (expl[i - 1] in cmn
                                     and expl[i + 1] in cmn):
                            if oper == expl[i - 1]:
                                expl[i] = str(varoper(n, '+', num))
                            elif oper != expl[i - 1]:
                                if oper == '-':
                                    expl[i] = str(varoper(n, oper, num))
                                else:
                                    expl[i] = str(varoper(num,
                                                          expl[i - 1],
                                                          expl[i]))
                                    expl[i - 1] = '+'

                            changed = True

                    elif i == 0:
                        expl[i] = str(varoper(num, oper, n))
                        changed = True
                    elif i == len(expl) - 1:
                        if expl[-2] == oper:
                            expl[i] = str(varoper(n, '+', num))
                        elif expl[-2] != oper:
                            if oper == '-':
                                expl[i] = str(varoper(num, '-', n))
                            elif oper == '+':
                                expl[i] = str(varoper(n, '-', num))

                        changed = True

                elif isspc and oper in spc:
                    if 0 < i < len(expl) - 1:
                        if expl[i + 1] == '*' and expl[i - 1] == '*':
                            if oper == '*':
                                expl[i] = str(varoper(n, oper, num))
                            elif oper == '/':
                                expl[i] = '(' + \
                                          str(varoper(n,
                                                      oper, num)) + ')'

                            changed = True
                        elif expl[i - 1] == '*' and expl[i + 1] == '/':
                            expl[i] = str(varoper(n, oper, num))
                            changed = True
                        elif expl[i - 1] == '/' and expl[i + 1] == '*':
                            if oper == '*':
                                expl[i - 1] = str(varoper(num,
                                                          '/', n)) \
                                              + ' /'
                                del expl[i:i + 1]
                            elif oper == '/':
                                expl[i] = str(varoper(n, '*', num))

                            changed = True
                        elif expl[i - 1] == '/' and expl[i + 1] == '/':
                            if oper == '*':
                                expl[i - 2] = str(varoper(expl[i - 2],
                                                          '*', num))
                            elif oper == '/':
                                expl[i] = str(varoper(n, '*', num))

                            changed = True

                    elif i == len(expl) - 1:
                        if expl[i - 1] == '*':
                            expl[i] = str(varoper(n, oper, num))
                        elif expl[i - 1] == '/':
                            if oper == '*':
                                expl[i - 2] = str(varoper(num, '/', n))
                                del expl[i - 1:]
                            elif oper == '/':
                                expl[i] = str(varoper(n, '*', num))

                        changed = True
                    elif i == 0:
                        expl[i] = varoper(n, oper, num)
                        changed = True

        if type2 == 'exp':
            # Если второй операнд является выражением
            expl2 = num.split()
            iscmn2 = any([True if s in cmn else False
                          for s in expl2[1::2]])
            isspc2 = all([True if s in spc else False
                          for s in expl2[1::2]])

            print(expl2, 21)

            if (iscmn2 and oper in cmn) or (isspc2 and oper in spc):
                # Если все операции являются операциями
                # сложения и вычитания или умножения и деления
                m = var
                for n in expl2:
                    if n in list(cmn) + list(spc) + ['//', '%']:
                        continue

                    m = varoper(m, oper, n)
                    print(m, 2)
                return m
            elif iscmn2 and oper in spc:
                return f'({var}){oper}({num})'
            elif isspc2 and oper in cmn:
                return f'{var} {oper} {num}'

        if changed:
            print(expl, '!')
            return ' '.join(expl)  # Если произошло изменение,
            #                        элементы выражения объединяютя

        if type2 == 'brac' or type2 == 'exp':
            # Если вторым операндом является выражение
            if oper == '*':
                if isspc and num.startswith('(') and num.endswith(')'):
                    return f'{var} {oper} {num}'

                return f'({var}) {oper} ({num})'
            elif oper == '+' and iscmn:
                return f'{var} {oper} {num}'
            elif oper == '-':
                return f'{var} {oper} ({num})'

            elif oper in ('/', '//', '%', '**'):
                if type2 == 'exp':
                    if num.startswith('(') and num.endswith(')'):
                        return f'({var}){oper}{num}'

                    return f'({var}){oper}({num})'
                elif type2 == 'brac':
                    return f'({var}){oper}{num}'

        elif num != 'brac' and num != 'exp':
            # Если второй операнд не является выражением
            if oper in ('+', '-'):
                return f'{var} {oper} {num}'
            elif oper in spc:
                if isspc:
                    return f'{var} {oper} {num}'

                return f'({var}) {oper} {num}'
            elif oper in ('//', '%', '**'):
                return f'({var}){oper}({num})'

    elif type1 == 'frac':
        fr = var.split('/', 1)
        # Избавление от круглых скобок
        for i, n in enumerate(fr):
            if fr[i].startswith('(') and fr[i].endswith(')'):
                fr[i] = fr[i][1:len(fr[i]) - 1]
            elif n.startswith('('):
                fr[i] = fr[i][1:]
            elif n.endswith(')'):
                fr[i] = fr[i][:len(fr[i]) - 1]

        n1 = fr[0]
        d1 = fr[1]
        # Проверка на случай ошибок
        try:
            typen1 = vartype(n1)
            if not typen1:
                n1 = '(' + n1 + ')'
                typen1 = vartype(n1)
        except Exception:
            print(n1)
            raise

        try:
            typed1 = vartype(d1)
            if not typed1:
                d1 = '(' + d1 + ')'
                typed1 = vartype(d1)
        except Exception:
            print(d1)
            raise

        # Стандартные операции при числителе/знаменателе
        # равном единице/нулю
        if d1 == '0' or d1 == '0.0':
            raise ZeroDivisionError
        elif d1 == '1' or d1 == '1.0':
            m = varoper(n1, oper, num)
            return m
        elif n1 == '0' or n1 == '0.0':
            m = varoper('0', oper, num)
            return m
        elif n1 == d1:
            m = varoper('1', oper, num)
            return m

        if type2 == 'int' or type2 == 'float':
            if typen1 in digl and typed1 in digl and count:
                m = eval('(' + var + ')' + oper + num)
                return m
            elif typen1 in digl and typed1 in varl and count:
                if oper == '**':
                    # При возведении дроби в степень,
                    # в эту степень возводятся и числитель,
                    # и знаменатель по отдельности
                    m = varoper(d1, oper, num)
                    q = eval(n1 + oper + num)
                    r = varoper(q, '/', m)
                    return r
                elif oper == '*':
                    m = eval(n1 + '*' + str(num))
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = eval(n1 + '/' + str(num))
                    q = varoper(m, '/', d1)
                    return q

            elif typen1 in varl and typed1 in digl and count:
                if oper == '**':
                    m = varoper(n1, oper, num)
                    q = eval(d1 + oper + num)
                    r = varoper(m, '/', str(q))
                    return r
                elif oper == '*':
                    m = eval(num + '/' + d1)
                    q = varoper(n1, '*', m)
                    return q
                elif oper == '/':
                    m = eval(d1 + '*' + num)
                    q = varoper(n1, '/', m)
                    return q

            elif typen1 in varl and typed1 in varl and count:
                if oper == '**':
                    m = varoper(n1, oper, num)
                    q = varoper(d1, oper, num)
                    r = varoper(m, '/', q)
                    return r
                elif oper == '*':
                    m = varoper(n1, '*', num)
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = eval(d1 + '*' + num)
                    q = varoper(n1, '/', m)
                    return q

            if oper in ('+', '-'):
                return f'{var} {oper} {num}'
            elif oper in ('*', '/', '//', '%', '**'):
                return f'({var}){oper}({num})'

        elif type2 == 'var':
            if typen1 in digl and typed1 in digl and count:
                m = eval(var)
                if oper == '*':
                    return m + num
                elif oper in ('+', '-'):
                    return f'{m} {oper} {num}'
                elif oper in ('/', '//', '%', '**'):
                    return f'{m}{oper}{num}'

            elif typen1 in digl and typed1 in varl and count:
                if oper == '**':
                    m = n1 + '**' + num
                    q = varoper(d1, oper, num)
                    r = varoper(m, '/', q)
                    return r
                elif oper == '*':
                    m = varoper(num, '/', d1)
                    q = varoper(n1, '*', m)
                    return q
                elif oper == '/':
                    m = varoper(d1, '*', num)
                    q = varoper(n1, '/', m)
                    return q

            elif typen1 in varl and typed1 in digl:
                if oper == '**':
                    m = varoper(n1, oper, num)
                    q = d1 + '**' + num
                    r = varoper(m, '/', q)
                    return r
                elif oper == '*':
                    m = varoper(num, '*', n1)
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = varoper(n1, '/', num)
                    q = varoper(m, '/', d1)
                    return q

            elif typen1 in varl and typed1 in varl and count:
                if oper == '**':
                    m = varoper(n1, oper, num)
                    q = varoper(d1, oper, num)
                    r = varoper(m, '/', q)
                    return r
                elif oper == '*':
                    m = varoper(n1, '*', num)
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = varoper(d1, '*', num)
                    q = varoper(n1, '/', m)
                    return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'({var}){oper}{num}'

        elif type2 == 'numvar':
            if typen1 in digl and typed1 in digl and count:
                if oper in ('+', '-'):
                    m = eval(var)
                    return f'{m} {oper} {num}'
                elif oper in ('//', '%', '**'):
                    m = eval(var)
                    return f'({m}){oper}{num}'
                elif oper == '*':
                    m = varoper(n1, oper, num)
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = varoper(d1, '*', num)
                    q = varoper(n1, oper, m)
                    return q

            elif typen1 in digl and typed1 in varl and count:
                if oper == '*':
                    m = varoper(n1, '*', num)
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = varoper(d1, '*', num)
                    q = varoper(n1, '/', m)
                    return q

            elif typen1 in varl and typed1 in digl and count:
                if d1 == '1' or d1 == '1.0':
                    #
                    m = varoper(n1, oper, num)
                    return m

                if oper == '*':
                    m = varoper(n1, oper, num)
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = varoper(d1, '*', num)
                    q = varoper(n1, oper, m)
                    return q

            elif typen1 in varl and typed1 in varl and count:
                if oper == '*':
                    m = varoper(n1, oper, num)
                    q = varoper(m, '/', d1)
                    return q
                elif oper == '/':
                    m = varoper(d1, '*', num)
                    q = varoper(n1, oper, m)
                    return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'({var}){oper}{num}'

        elif type2 == 'frac':
            fr2 = num.split('/', 1)
            n2 = fr2[0]
            d2 = fr2[1]
            typen2 = vartype(n2)
            typed2 = vartype(d2)
            # Стандартные операции броби с дробью
            # при определённыех значениях числителя/знаменателя
            if d2 == '0' or d2 == '0.0':
                raise ZeroDivisionError
            elif d2 == '1' or d2 == '1.0':
                m = varoper(var, oper, n2)
                return m
            elif n2 == '0' or n2 == '0.0':
                m = varoper(var, oper, '0')
                return m
            elif n2 == d2:
                m = varoper(var, oper, '1')
                return m

            if typen1 in digl and typed1 in digl and count:
                if typen2 in digl and typed2 in digl:
                    m = eval(var)
                    q = eval(num)
                    r = eval(m + oper + q)
                    return r
                elif typen2 in digl and typed2 in varl:
                    if oper == '*':
                        m = eval(n1 + oper + n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = eval(d1 + '*' + n2)
                        q = varoper(n1, '*', d2)
                        r = varoper(q, '/', m)
                        return r

                elif typen2 in varl and typed2 in digl:
                    if d2 == '1' or d2 == '1.0':
                        m = varoper(var, oper, n2)
                        return m

                    if d1 == d2:
                        # Если совпадают знаменатели,
                        if oper in ('+', '-'):
                            # то при сложении или вычитании
                            # складываются числители и заносятся
                            # под один общий знаменатель
                            m = varoper(n1, oper, n2)
                            r = varoper(m, '/', d1)
                            return r
                        elif oper == '/':
                            m = varoper(n1, oper, n2)
                            return m

                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = eval(d1 + '*' + d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = eval(n1 + '*' + d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, oper, q)
                        return r

                elif typen2 in varl and typed2 in varl:
                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = varoper(n1, '*', d2)
                        q = varoper(n2, '*', d1)
                        r = varoper(m, '/', q)
                        return r

                if oper in ('+', '-'):
                    m = eval(var)
                    return f'{m} {oper} {num}'
                elif oper in ('//', '%', '**'):
                    m = eval(var)
                    return f'{m}{oper}({num})'

            elif typen1 in digl and typed1 in varl and count:
                if typen2 in digl and typed2 in digl:
                    if oper in ('+', '-'):
                        m = eval(num)
                        return f'{var} {oper} {m}'
                    elif oper in ('//', '%', '**'):
                        m = eval(num)
                        return f'({var}){oper}{m}'
                    elif oper == '*':
                        m = eval(n1 + oper + n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = eval(n1 + '*' + d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, oper, q)
                        return r
                elif typen2 in digl and typed2 in varl:
                    if d1 == d2:
                        if oper in ('+', '-'):
                            m = eval(n1 + oper + n2)
                            q = varoper(m, '/', d1)
                            return q
                        elif oper == '/':
                            m = eval(n1 + '/' + n2)
                            return m
                    if oper == '*':
                        m = eval(n1 + oper + n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = eval(n1 + oper + n2)
                        q = varoper(m, '*', d2)
                        r = varoper(q, '/', d1)
                        return r

                elif typen2 in varl and typed2 in digl:
                    if d1 == d2:
                        if oper in ('+', '-'):
                            m = eval(n1 + oper + n2)
                            q = varoper(m, '/', d1)
                            return q
                        elif oper == '/':
                            m = eval(n1 + '/' + n2)
                            return m

                    elif d2 == '1' or d2 == '1.0':
                        m = varoper(var, oper, n2)
                        return m

                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = eval(n1 + '*' + d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, '/', q)
                        return r

                elif typen2 in varl and typed2 in varl:
                    if d1 == d2:
                        if oper in ('+', '-'):
                            m = varoper(n1, oper, n2)
                            q = varoper(m, '/', d1)
                            return q
                        elif oper == '/':
                            m = varoper(n1, '/', n2)
                            return m

                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = varoper(n1, '*', d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, '/', q)
                        return r

            elif typen1 in varl and typed1 in digl and count:
                if typen2 in digl and typed2 in digl:
                    if oper in ('+', '-'):
                        m = eval(num)
                        return f'{var} {oper} {m}'
                    elif oper in ('//', '%', '**'):
                        m = eval(num)
                        return f'({var}){oper}{m}'
                    elif oper in ('*', '/'):
                        m = eval(num)
                        q = varoper(var, oper, m)
                        return q

                elif typen2 in digl and typed2 in varl:
                    if oper == '*':
                        m = varoper(n1, '*', n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = eval(n1 + '*' + d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, '/', q)
                        return r

                elif typen2 in varl and typed2 in digl:
                    if d1 == d2:
                        if oper in ('+', '-'):
                            m = varoper(n1, oper, n2)
                            q = varoper(m, '/', d1)
                            return q
                        elif oper == '/':
                            m = varoper(n1, '/', n2)
                            return m
                    elif d2 == '1' or d2 == '1.0':
                        m = varoper(var, oper, n2)
                        return m

                    if oper == '*':
                        print(var, num)
                        m = varoper(n1, oper, n2)
                        q = eval(d1 + oper + d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = eval(d2 + oper + d1)
                        q = varoper(n1, oper, n2)
                        r = varoper(m, '*', q)
                        return r

                elif typen2 in varl and typed2 in varl:
                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = varoper(n1, '*', d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, '/', q)
                        return r

            elif typen1 in varl and typed1 in varl and count:
                if typen2 in digl and typed2 in digl:
                    if oper in ('+', '-'):
                        m = eval(num)
                        return f'{var} {oper} {m}'
                    elif oper in ('//', '%', '**'):
                        m = eval(num)
                        return f'({var}){oper}{m}'
                    elif oper == '*':
                        # Выполняются типичные операции,
                        # если второй операнд при вычислении
                        # возвращает единицу или ноль
                        if eval(num) == 1.0:
                            return var
                        elif eval(num) == 0.0:
                            return 0

                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        if eval(num) == 1.0:
                            return var

                        m = varoper(n1, '*', d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, oper, q)
                        return r

                elif typen2 in digl and typed2 in varl:
                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = varoper(n1, '*', d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, oper, q)
                        return r

                elif typen2 in varl and typed2 in digl:
                    if d2 == '1' or d2 == '1.0':
                        m = varoper(var, oper, n2)
                        return m

                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = varoper(n1, '*', d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, oper, q)
                        return r

                elif typen2 in varl and typed2 in varl:
                    if d1 == d2:
                        if oper in ('+', '-'):
                            m = varoper(n1, oper, n2)
                            q = varoper(m, '/', d1)
                            return q
                        elif oper == '/':
                            m = varoper(n1, '/', n2)
                            return m
                    if oper == '*':
                        m = varoper(n1, oper, n2)
                        q = varoper(d1, oper, d2)
                        r = varoper(m, '/', q)
                        return r
                    elif oper == '/':
                        m = varoper(n1, '*', d2)
                        q = varoper(d1, '*', n2)
                        r = varoper(m, oper, q)
                        return r

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'({var}){oper}({num})'

        elif type2 == 'pow':
            pw = num.split('**', 1)
            numn = pw[0]
            nump = pw[1]
            typen = vartype(numn)
            typep = vartype(nump)
            # Типичные операции при определёных значениях степени
            if (nump == '1.0' or nump == '1') and count:
                m = varoper(var, oper, numn)
                return m
            elif (nump == '0' or nump == '0.0') and count:
                m = varoper(var, oper, '1')
                return m

            if typen1 in digl and typed1 in digl and count:
                m = eval(var)
                q = varoper(m, oper, num)
                return q
            elif typen1 in digl and typed1 in varl and count:
                if typen in digl and typep in digl:
                    m = eval(num)
                    q = varoper(var, oper, m)
                    return q
                elif typen in digl and typep in varl:
                    if n1 == nump:
                        if oper == '*':
                            nump = varoper('1', '+', nump)
                            q = varoper(numn + '**' + nump, '/', d1)
                            return q
                        elif oper == '/':
                            nump = varoper('1', '-', nump)
                            q = varoper(numn + '**' + nump, '/', d1)
                            return q

                    if oper == '*':
                        m = varoper(n1, oper, num)
                        q = varoper(m, '/', d1)
                        return q
                    elif oper == '/':
                        m = varoper(d1, '*', num)
                        q = varoper(n1, '/', m)
                        return q

                elif typen in varl and (typep in digl or typep in varl):
                    if d1 == numn:
                        # Если основания равны
                        if oper == '*':
                            q = varoper(num, '/', d1)
                            r = varoper(n1, '*', q)
                            return r
                        elif oper == '/':
                            q = varoper(d1, '*', num)
                            r = varoper(n1, '/', q)
                            return r

                    if oper == '*':
                        m = varoper(n1, oper, num)
                        q = varoper(m, '/', d1)
                        return q
                    elif oper == '/':
                        m = varoper(d1, '*', num)
                        q = varoper(n1, '/', m)
                        return q

            elif typen1 in varl and typed1 in digl and count:
                if typen in digl and typep in digl:
                    m = eval(num)
                    if oper == '*':
                        q = varoper(m, '/', d1)
                        r = varoper(n1, oper, str(q))
                        return r
                    elif oper == '/':
                        q = eval(d1 + '*' + m)
                        r = varoper(n1, oper, q)
                        return r

                    if oper == '*':
                        m = varoper(n1, oper, num)
                        q = varoper(m, '/', d1)
                        return q
                    elif oper == '/':
                        m = varoper(d1, '*', num)
                        q = varoper(n1, '/', m)
                        return q

                elif typen in digl and typep in varl:
                    if d1 == numn:
                        if oper == '*':
                            m = varoper(num, '/', d1)
                            q = varoper(n1, oper, m)
                            return q
                        elif oper == '/':
                            m = varoper(d1, '*', num)
                            q = varoper(n1, oper, m)
                            return q

                    if oper == '*':
                        m = varoper(n1, oper, num)
                        q = varoper(m, '/', d1)
                        return q
                    elif oper == '/':
                        m = varoper(d1, '*', num)
                        q = varoper(n1, '/', m)
                        return q

                elif typen in varl and (typep in digl or typep in varl):
                    if n1 == numn:
                        if oper == '*':
                            m = varoper(n1, oper, num)
                            q = varoper(m, '/', d1)
                            return q
                        elif oper == '/':
                            m = varoper(n1, oper, num)
                            q = varoper(m, '/', d1)
                            return q

                    if oper == '*':
                        m = varoper(n1, oper, num)
                        q = varoper(m, '/', d1)
                        return q
                    elif oper == '/':
                        m = varoper(d1, '*', num)
                        q = varoper(n1, '/', m)
                        return q

            elif typen1 in varl and typed1 in varl and count:
                if typen in digl and typep in digl:
                    m = eval(num)
                    q = varoper(var, oper, m)
                    return q
                elif typen in digl and typep in varl:
                    if oper == '*':
                        m = varoper(n1, oper, num)
                        q = varoper(m, '/', d1)
                        return q
                    elif oper == '/':
                        m = varoper(d1, '*', num)
                        q = varoper(n1, '/', m)
                        return q

                elif typen in varl and (typep in digl or typep in varl):
                    if n1 == numn:
                        if oper == '*':
                            m = varoper(n1, oper, num)
                            q = varoper(m, '/', d1)
                            return q
                        elif oper == '/':
                            m = varoper(n1, oper, num)
                            q = varoper(m, '/', d1)
                            return q

                    elif d1 == numn:
                        if oper == '*':
                            m = varoper(num, '/', d1)
                            q = varoper(n1, oper, m)
                            return q
                        elif oper == '/':
                            m = varoper(d1, '*', num)
                            q = varoper(n1, oper, m)
                            return q

                    if oper == '*':
                        m = varoper(n1, oper, num)
                        q = varoper(m, '/', d1)
                        return q
                    elif oper == '/':
                        m = varoper(d1, '*', num)
                        q = varoper(n1, '/', m)
                        return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f'({var}){oper}({num})'

    elif type1 == 'pow':
        pw = var.split('**', 1)
        # Избавление от круглых скобок
        for i, n in enumerate(pw):
            if pw[i].startswith('(') and pw[i].endswith(')'):
                pw[i] = pw[i][1:len(pw[i]) - 1]
            elif n.startswith('('):
                pw[i] = pw[i][1:]
            elif n.endswith(')'):
                pw[i] = pw[i][:len(pw[i]) - 1]

        varn = pw[0]
        varp = pw[1]
        # Проверка в случае ошибок
        try:
            typen1 = vartype(varn)
            if not typen1:
                varn = '(' + varn + ')'
                typen1 = vartype(varn)
        except Exception:
            varn = '(' + varn + ')'
            typen1 = vartype(varn)

        try:
            typep1 = vartype(varp)
            if not typep1:
                varp = '(' + varp + ')'
                typep1 = vartype(varp)
        except Exception:
            varp = '(' + varp + ')'
            typep1 = vartype(varp)

        # Стандартные операции при определённых значениях
        # основания или степени
        if (varp == '1.0' or varp == '1') and count:
            m = varoper(varn, oper, num)
            return m
        elif varp == '0' or varp == '0.0':
            m = varoper('1', oper, num)
            return m
        elif varn == '1' or varn == '1.0':
            m = varoper(var, oper, '1')
            return m
        elif varn == '0' or varn == '0.0' \
                and (varp != '0' and varp != '0.0'):
            m = varoper(var, oper, '0')
            return m

        if typen1 == 'numvar' and count:
            # Если первый операнд является переменной в степени с числом
            if varn[-2:].isalpha():
                j = -2
            elif varn[-1].isalpha():
                j = -1

            if type2 in digl:
                if oper in ('*', '/'):
                    m = eval(varn[:j] + oper + num)
                    q = varoper(str(m), '*', varn[j:] + '**' + varp)
                    return q
                elif oper == '**':
                    m = eval(varn[:j] + oper + num)
                    q = varoper(varn[j:] + '**' + varp, oper, num)
                    r = varoper(str(m), '*', q)
                    return r
            elif type2 in varl:
                if oper in ('*', '/'):
                    m = varoper(varn[j:] + '**' + varp, oper, num)
                    print(varn[j:] + '**' + varp, num)
                    q = varoper(varn[:j], '*', m)
                    return q

        if type2 == 'int' or type2 == 'float':
            if typen1 in digl and typep1 in digl and count:
                m = eval(var)
                return eval(str(m) + oper + num)
            elif typen1 in digl and typep1 in varl and count:
                if varn == num:
                    # Если одинаковые основания
                    if oper == '*':
                        # При умножении чисел с одинаковым основанием,
                        # их степени складываются
                        m = varoper(varp, '+', '1')
                        q = varoper(varn, '**', m)
                        return q
                    elif oper == '/':
                        # При делении чисел с одинаковым основанием,
                        # их степени вычитаются
                        m = varoper(varp, '-', '1')
                        q = varoper(varn, '**', m)
                        return q

            if oper == '**' and count:
                # При возведении числа в степени в степень,
                # эти степени умножаются
                m = varoper(varp, '*', num)
                q = varoper(varn, '**', str(m))
                return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f"({var}){oper}{num}"

        elif type2 == 'var':
            if typen1 in digl and typep1 in digl and count:
                m = eval(var)
                q = varoper(m, oper, num)
                return q
            elif typen1 in varl and (typep1 in digl or typep1 in varl) \
                    and count:
                if varn == num:
                    if oper == '*':
                        m = varoper(varp, '+', '1')
                        q = varoper(varn, '**', m)
                        if '**(' in q and q != 'exp':
                            # Если степень является выражением,
                            # а всё число со степенью не является
                            # частью выражения, то пробелы удаляются
                            # (подразумевается, что это действие
                            # превратит степень в выражение в скобках
                            # ('brac'))
                            q = q.replace(' ', '')

                        return q
                    elif oper == '/':
                        m = varoper(varp, '-', '1')
                        q = varoper(varn, '**', m)
                        if '**(' in q and q != 'exp':
                            q = q.replace(' ', '')

                        return q

            if oper == '**':
                m = varoper(varp, '*', num)
                q = varoper(varn, '**', m)
                if '**(' in q and q != 'exp':
                    q = q.replace(' ', '')

                return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f"({var}){oper}{num}"

        elif type2 == 'numvar':
            if num[-2].isalpha():
                i = -2
            elif num[-1].isalpha():
                i = -1

            numn = num[:i]
            numv = num[i:]
            if typen1 in digl and typep1 in digl and count:
                m = eval(var)
                return varoper(m, oper, num)
            elif typen1 in digl and typep1 in varl and count:
                if numn == varn:
                    if oper == '*':
                        m = varoper(varp, '+', '1')
                        q = varoper(varn + '**' + m, oper, numv)
                        if '**(' in q and q != 'exp':
                            q = q.replace(' ', '')

                        return q
                    elif oper == '/':
                        m = varoper(varp, '-', '1')
                        q = varoper(varn + '**' + m, oper, numv)
                        if '**(' in q and q != 'exp':
                            q = q.replace(' ', '')

                        return q

                if oper == '**':
                    m = varoper(varp, '*', num)
                    q = varoper(varn, '**', m)
                    if '**(' in q:
                        q = q.replace(' ', '')
                    return q

            elif typen1 in varl and (typep1 in digl or typep1 in varl) \
                    and count:
                if numv == varn:
                    # Если переменная от второго операнда
                    # соответствует основанию
                    if oper == '*':
                        m = varoper(varp, '+', '1')
                        return f'{numn}{numv}**{m}'
                    elif oper == '/':
                        m = varoper(varp, '-', '1')
                        return f'({numv}**{m})/{numn}'

                elif varn == num:
                    if oper == '*':
                        m = varoper(varp, '+', '1')
                        q = varoper(num, oper, m)
                        if '**(' in q and q != 'exp':
                            q = q.replace(' ', '')

                        return q
                    elif oper == '/':
                        m = varoper(varp, '-', '1')
                        q = varoper(num, oper, m)
                        if '**(' in q and q != 'exp':
                            q = q.replace(' ', '')

                        return q

                if oper == '**':
                    m = varoper(varp, '*', num)
                    q = varoper(varn, '**', m)
                    if '**(' in q and q != 'exp':
                        q = q.replace(' ', '')

                    return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f"({var}){oper}{num}"

        elif type2 == 'frac':
            fr2 = num.split('/', 1)
            n2 = fr2[0]
            d2 = fr2[1]
            typen2 = vartype(n2)
            typed2 = vartype(d2)
            if d2 == '0' or d2 == '0.0' and count:
                raise ZeroDivisionError
            elif d2 == '1' or d2 == '1.0' and count:
                m = varoper(var, oper, n2)
                return m
            elif n2 == '0' or n2 == '0.0' and count:
                m = varoper(var, oper, '0')
                return m
            elif n2 == d2 and count:
                m = varoper(var, oper, '1')
                return m

            if typen1 in digl and typep1 in digl and count:
                if typen2 in digl and typed2 in digl:
                    m = eval(var)
                    q = eval(num)
                    return eval(m + oper + q)
                elif typen2 in digl and typed2 in varl:
                    m = eval(var)
                    if oper == '*':
                        q = eval(m + oper + n2)
                        r = varoper(q, '/', d2)
                        return r
                    elif oper == '/':
                        q = eval(m + oper + n2)
                        r = varoper(q, '*', d2)
                        return r

                elif typen2 in varl and typed2 in digl:
                    m = eval(var)
                    if oper == '*':
                        q = eval(str(m) + '/' + d2)
                        r = varoper(str(q), oper, n2)
                        return r
                    elif oper == '/':
                        q = eval(str(m) + '*' + d2)
                        r = varoper(q, oper, n2)
                        return r

                elif typen2 in varl and typed2 in varl:
                    if oper == '*':
                        m = varoper(var, '*', n2)
                        q = varoper(m, '/', d2)
                        return q
                    elif oper == '/':
                        m = varoper(var, '*', d2)
                        q = varoper(m, '/', n2)
                        return q

            elif typen1 in digl and typep1 in varl and count:
                if typen2 in digl and typed2 in digl:
                    k = eval(num)
                    if oper in ('*', '/'):
                        m = varoper(var, oper, k)
                        return m

                elif typen2 in digl and typed2 in varl:
                    if oper == '*':
                        m = varoper(var, '*', n2)
                        q = varoper(m, '/', d2)
                        return q
                    elif oper == '/':
                        m = varoper(var, '/', n2)
                        q = varoper(m, '*', d2)
                        return q

                elif typen2 in varl and typed2 in digl:
                    if oper == '*':
                        m = varoper(var, '/', d2)
                        q = varoper(m, '*', n2)
                        return q
                    elif oper == '/':
                        m = varoper(var, '*', d2)
                        q = varoper(m, '/', n2)
                        return q

                elif typen2 in varl and typed2 in varl:
                    if oper == '*':
                        m = varoper(var, '*', n2)
                        q = varoper(m, '/', d2)
                        return q
                    elif oper == '/':
                        m = varoper(var, '*', d2)
                        q = varoper(m, '/', n2)
                        return q

            elif typen1 in varl and (typep1 in digl or typep1 in varl) \
                    and count:
                if typen2 in digl and typed2 in digl:
                    m = eval(num)
                    if oper in ('*', '/'):
                        m = varoper(var, oper, m)
                        return m

                elif typen2 in digl and typed2 in varl:
                    if oper == '*':
                        m = varoper(var, '/', d2)
                        q = varoper(m, '*', n2)
                        return q
                    elif oper == '/':
                        m = varoper(var, '*', d2)
                        q = varoper(m, '/', n2)
                        return q

                elif typen2 in varl and typed2 in digl:
                    if oper == '*':
                        m = varoper(var, '*', n2)
                        q = varoper(m, '/', d2)
                        return q
                    elif oper == '/':
                        m = varoper(var, '/', n2)
                        q = varoper(m, '*', d2)
                        return q

                elif typen2 in varl and typed2 in varl:
                    if oper == '*':
                        m = varoper(var, '*', n2)
                        q = varoper(m, '/', d2)
                        return q
                    elif oper == '/':
                        m = varoper(var, '*', d2)
                        q = varoper(m, '/', n2)
                        return q

            if oper == '**' and count:
                m = varoper(varp, '*', num)
                q = varoper(varn, '**', m)
                return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f"({var}){oper}({num})"

        elif type2 == 'pow':
            pw = num.split('**', 1)
            numn = pw[0]
            nump = pw[1]
            typen2 = vartype(numn)
            typep2 = vartype(nump)
            # Типичные взаимодействия с числом в степени
            # при определённых значениях основания/степени
            if nump == '1.0' or nump == '1' and count:
                m = varoper(var, oper, numn)
                return m
            elif nump == '0' or nump == '0.0':
                m = varoper(var, oper, '1')
                return m
            elif numn == '1' or numn == '1.0':
                m = varoper(var, oper, '1')
                return m
            elif numn == '0' or numn == '0.0' \
                    and (nump != '0' and nump != '0.0'):
                m = varoper(var, oper, '0')
                return m

            if typen2 == 'numvar' and count:
                # Если второй операнд является
                # переменной в степени с числом
                if numn[-2].isalpha():
                    j = -2
                elif numn[-1].isalpha():
                    j = -1

                if oper == '*':
                    m = varoper(var, oper, numn[j:] + '**' + nump)
                    q = varoper(numn[:j], oper, m)
                    return q
                elif oper == '/':
                    m = varoper(var, oper, numn[:j])
                    q = varoper(m, oper, numn[j:] + '**' + nump)
                    return q

            if typen1 in digl and typep1 in digl and count:
                k = eval(var)
                if typen2 in digl and typep2 in digl:
                    m = eval(num)
                    return eval(k + oper + m)

                elif typen2 in digl and typep2 in varl:
                    if varn == numn:
                        if oper == '*':
                            m = varoper(varp, '+', nump)
                            q = varoper(varn, '**', m)
                            return q
                        elif oper == '/':
                            m = varoper(varp, '-', nump)
                            q = varoper(varn, '**', m)
                            return q

                    if oper in ('+', '-', '*'):
                        return f'{k} {oper} {num}'
                    elif oper in ('/', '//', '%', '**'):
                        return f"{k}{oper}({num})"

                if typen2 in varl \
                        and (typep2 in digl or typep2 in varl) \
                        and count:
                    if oper == '*':
                        m = varoper(k, oper, num)
                        return m

                    if oper in ('+', '-'):
                        return f'{k} {oper} {num}'
                    elif oper in ('/', '//', '%', '**'):
                        return f"{k}{oper}({num})"

            elif typen1 in digl and typep1 in varl and count:
                if typen2 in digl \
                        and (typep2 in digl or typep2 in varl):
                    if varn == numn:
                        # Если основания совпадают
                        if oper == '*':
                            m = varoper(varp, '+', nump)
                            q = varoper(varn, '**', m)
                            return q
                        elif oper == '/':
                            m = varoper(varp, '-', nump)
                            q = varoper(varn, '**', m)
                            return q

            elif typen1 in varl and (typep1 in digl or typep1 in varl) \
                    and count:
                if typen2 in digl and typep2 in digl:
                    m = eval(num)
                    q = varoper(var, oper, m)
                    return q

                elif typen2 in varl \
                        and (typep2 in digl or typep2 in varl):
                    if varn == numn:
                        if oper == '*':
                            m = varoper(varp, '+', nump)
                            q = varoper(varn, '**', m)
                            return q
                        elif oper == '/':
                            m = varoper(varp, '-', nump)
                            q = varoper(varn, '**', m)
                            return q

            if oper == '**':
                m = varoper(varp, '*', num)
                q = varoper(varn, '**', m)
                return q

            if oper in ('+', '-', '*'):
                return f'{var} {oper} {num}'
            elif oper in ('/', '//', '%', '**'):
                return f"({var}){oper}({num})"


print(varoper('n**n - 5', '/', 'n**n'))


class MainMath:
    """
    Формулы сокращенного умножения,

    Квадратное уравнение и формула разложения квадратного трехчлена
    на множители,

    Арифметическая прогрессия,

    Геометрическая прогрессия.
    """

    ans = None
    old = None

    def __init__(self):
        pass

    @staticmethod
    def res():
        if MainMath.ans and MainMath.old:
            return MainMath.old + ' = ' + MainMath.ans

    @classmethod
    def sqrsum(cls, *args, sign='+', reverse=False):
        """
        Квадрат суммы.

        (a +/- b)**2 = a**2 +/- 2a * b + b**2

        Принимает два аргумента в виде строк и возвращает
        преобразованное выражение. Например, sqrsum('3', 'b')
        возвращает "9 + 6b + b**2".

        Если аргумент reverse равен True,
        и в качестве аргумента передано выражение, возвращается
        квадрат суммы. Например,
        sqrsum('4a**2 + 4a * b + b**2', reverse=True)
        вернёт "(2.0a + b)**2".
        """

        assert 0 < len(args) < 3, 'Must be given 1, 2 arguments, got ' \
                                  + str(len(args)) + ' instead'
        # Должно быть 1 или 2 аргумента
        assert sign in ('+', '-'), 'Sign between argument must be ' \
                                   '\'+\' or \'-\', got' + str(sign) + \
                                   'instead'

        if not reverse:
            # Если функция не обратная
            a, b = args
            ab = ['2']

            cls.old = '(%s %s %s)**2' % (a, sign, b)
            # Сохраняет введённое (старое) выражение

            for n in (a, b):
                # Генерация среднего числа
                ab.extend(('*', n))

            listing = [a, b]  # Список для сохранения
            #                   изменений аргументов

            for i in range(2):
                # Преобразование двух крайних переменных
                n = listing[i]
                listing[i] = varoper(listing[i], '**', '2')
                if not listing[i]:
                    # Если аргумент не изменился,
                    # возбуждается исключение
                    raise ValueError(' object ', n, ' wasn\'t changed')

            listing += ab
            a, b, *ab = listing  # Собирание аргументов
            ab = ' '.join(ab)

            """
            if __name__ == '__main__':
                print(listing)
            """

            if sign == '+':
                # От знака определяется выражение
                cls.ans = '%s + %s + %s' % (a, ab, b)
            else:
                cls.ans = '%s - %s + %s' % (a, ab, b)

            return cls.ans

        else:
            assert len(args) == 1, 'Must be given only 1 expression, \
                                    got' + str(len(args)) + 'instead'
            # Ожидается один аргумент, который является выражением

            exp = args[0]
            cls.old = exp  # Сохраняется старое значение
            exp = exp.split(' + ')
            if len(exp) == 2 and '-' in exp[0]:
                # Если есть знак "-"
                sign = '-'
                exp = exp[0].split() + [exp[1]]
            elif len(exp) == 3:
                # Если выражение содержит два знака "+"
                exp = [exp[0]] + exp[1].split() + [exp[-1]]
            else:
                # Во всех остальных случаях дано неправильное выражение
                raise ArithmeticError('Given invalid expression '
                                      + args[0])

            a, b = exp[0], exp[-1]
            listing = [a, b]  # Список из крайних аргументов

            for i, n in enumerate(listing):
                # Возведение в корень
                listing[i] = varoper(n, '**', '0.5')
                if not listing[i]:
                    # Если что-то пошло не так
                    raise ValueError(' argument ', n, ' wasn\'t \
                                                      changed')

            if exp[1] == '-':
                # Если стоит знак "-"
                ab = exp[2:-1]
            else:
                ab = exp[1:-1]

            if __name__ == '__main__':
                # Тест
                print(a, b, ab)

            if len(ab) == 1:
                # Если средний аргумент состоит из одного элемента
                print(ab[0])
                raise ValueError
            elif 3 <= len(ab) <= 5:
                # Если средний аргумент содержит 5 элементов
                if ab[:2] == ['2', '*']:
                    # Деление на 2
                    ab = ab[2:]
                elif len(ab) == 3:
                    # Деление на 2 первого множителя
                    m = varoper(ab[0], '/', '2')
                    ab = [m] + ab[1:]
                elif len(ab) == 2:
                    # Если элементов 2, возбуждается исключение
                    print(ab)
                    raise ValueError
            else:
                # Если что-то не так, выражение возможно
                # не являтся суммой квадратов
                raise ArithmeticError('Expression might be not '
                                      'a square of sum because of',
                                      ''.join(ab))

            listing += ab
            a, b, *ab = listing

            if [a, b] != ab[::2]:
                # Если аргументы не совпадвют,
                # возможно выражение не является суммой квадратов
                print(listing)
                raise ArithmeticError('Expression might be not '
                                      'a square of sum because', a,
                                      'and/or', b, 'don\'t match',
                                      ab[::2])

            cls.ans = f'({a} {sign} {b})**2'
            return cls.ans

    @classmethod
    def difsqrs(cls, *args, reverse=False):
        """
        Разность квадратов.

        a**2 - b**2 = (a+b)(a-b)

        Принимает два аргумента, которые возведены во вторую степень,
        и преобразует их в произведение суммы и разности.

        Если reverse=True, то в касестве аргумента принимается
        произведение суммы и разности, а возвращается
        разность квадратов.
        """

        if not reverse:
            assert len(args) == 2, 'Must be given 2 arguments, got ' \
                                   + str(len(args)) + ' instead'
            # Должно быть два аргумента

            a, b = args
            cls.old = f'{a} - {b}'  # Сохранение старого значения

            # Сокращение степени в два раза
            a = varoper(a, '**', '0.5')
            b = varoper(b, '**', '0.5')

            # Построение произведения суммы на разность
            cls.ans = f'({a}+{b}) * ({a}-{b})'

            return cls.ans
        elif reverse:
            assert len(args) == 1, 'Must be given only 1 argument, ' \
                                   'got ' + str(len(args)) + ' instead'
            # Должен быть один аргумент

            sm, df = args[0].split(' * ')
            cls.old = f'{sm} * {df}'  #

            # Разделение на аргументы
            sm.replace('(', '')
            sm.replace(')', '')
            a1, b1 = sm.split('+')

            df.replace('(', '')
            df.replace(')', '')
            a2, b2 = df.split('-')

            if a1 == a2 and b1 == b2:
                # Если обе пары соответствуют, то всё в порядке
                a = varoper(a1, '**', '2')
                b = varoper(b1, '**', '2')
            else:
                # Иначе выражение может не являться разностью квадратов
                raise ArithmeticError('Expression might not '
                                      'a difference of squares because',
                                      a1, 'don\'t match', a2,
                                      '\nand/or', b1,
                                      'don\'t match', b2)

            cls.ans = f'{a} - {b}'  # Сборка шаблона

            return cls.ans

    @classmethod
    def sumcubes(cls, *args, sign='+', reverse=False):
        """
        Сумма кубов

        a**3 +/- b**3 = (a+/-b) * (a**2 -/+ a * b + b**2)

        Принимает два аргумента, которые возведены в третью степень,
        и преобразует их в произведение суммы/разности
        и неполного квадрата разности/суммы.

        sign - знак между аргументами.

        reverse - ссли True, то принимает в качестве аргумента выражение
        и возвращает сумму/разность кубов.
        """

        if not reverse:
            assert len(args) == 2, 'Must be given 2 arguments, got ' \
                                   + str(len(args)) + ' instead'
            # Должно быть два аргумента

            a, b = args
            cls.old = f'{a} {sign} {b}'  # Сохранение старого значения
            # Создание нужных аргументов
            a1 = varoper(a, '**', str(1 / 3))
            b1 = varoper(b, '**', str(1 / 3))
            a2 = varoper(a, '**', str(2 / 3))
            b2 = varoper(b, '**', str(2 / 3))
            ab = varoper(a1, '*', b1)

            # Создание шаблона на основе знака
            if sign == '+':
                cls.ans = f'({a1} + {b1}) * ({a2} - {ab} + {b2})'
            elif sign == '-':
                cls.ans = f'({a1} - {b1}) * ({a2} + {ab} + {b2})'

            return cls.ans
        else:
            assert len(args) == 1, 'Must be given only 1 argument, ' \
                                   'got ' + str(len(args)) + ' instead'
            # Должен быть один аргумент

            cls.old = args[0]
            sum1, exp = args[0].split(' * ', 1)
            # Проверка на соответствие знаков
            if sum1.find('+') != -1 and exp.find(' - ') != -1:
                sign = '+'
            elif sum1.find('-') != -1 and exp.find(' - ') == -1 \
                    and exp.find(' + ') != -1:
                sign = '-'
            else:
                # Иначе выражение может не являться суммой кубов
                raise ValueError('Might entered invalid expresssion',
                                 sum1)

            a, b = sum1.split(sign, 1)
            a = a[1:]
            b = b[:-1]

            # Неполный квадрат раделяется на аргументы
            exp = exp.replace(' + ', ' ')
            exp = exp.replace(' - ', ' ')
            a2, *ab, b2 = exp.split()
            a1, b1 = ' '.join(ab).split(' * ')
            if a != a1 or b != b1:
                # Проверка на соответствие частей произведения
                # аргументам суммы
                raise ValueError('Argument', a, 'don\'t matches', a1,
                                 'or', b, 'don\'t matches', b1)

            testa = varoper(a2, '**', '0.5')
            testb = varoper(b2, '**', '0.5')
            if testa != a1 or testb != b1:
                # Проверка на соответствие аргументов выражения
                # аргументам суммы
                raise ValueError('Argument', a1, 'don\'t matches',
                                 testa, 'or', b1, 'don\'t matches',
                                 testb)

            a3 = varoper(a, '**', '3')
            b3 = varoper(b, '**', '3')
            cls.ans = f'{a3} {sign} {b3}'

            return cls.ans

    @classmethod
    def cubesum(cls, *args, sign='+', reverse=False):
        """
        Куб суммы

        (a+/-b)**3 = a**3 +/- 3 * a**2 * b + 3 * a * b**2 +/- b**3

        :param args: принимает два аргумента куба суммы/разности.
        :param sign: знак между аргументами.
        reverse: если равен True, то в качестве аргумента
        принимает выражение.

        Возвращает выражение или куб суммы/разности в зависимости от
        параметра reverse.
        """

        if not reverse:
            assert len(args) == 2, 'Must be given 2 arguments, got ' \
                                   + str(len(args)) + ' instead'
            # Должно быть два аргумента

            a, b = args
            # Сохранение старого значения
            cls.old = f'({a}{sign}{b})**3'
            # Построение членов выражения
            a3 = varoper(a, '**', '3')
            b3 = varoper(b, '**', '3')
            a2b3 = ' '.join(['3 *', varoper(a, '**', '2'), '*', b])
            ab23 = ' '.join(['3 *', a, '*', varoper(b, '**', '2')])

            if sign == '+':
                # Создание шаблона в зависимости от знака
                cls.ans = f'{a3} + {a2b3} + {ab23} + {b3}'
            elif sign == '-':
                cls.ans = f'{a3} - {a2b3} + {ab23} - {b3}'

            return cls.ans
        else:
            assert len(args) == 1, 'Must be given only 1 argument, ' \
                                   'got ' + str(len(args)) + ' instead'
            # Должен быть один аргумент

            cls.old = args[0]  # Сохранение старого значения
            exp = args[0].split(' + ')
            if len(exp) == 2:
                # Если длина равна двум, подразумевается,
                # что все остальные знаки - это минусы
                exp = exp[0].split(' - ') + exp[1].split(' - ')
                if len(exp) != 4:
                    raise ArithmeticError('Expression might not a cube '
                                          'of sum because of a signs',
                                          cls.old)

                sign = '-'
            elif len(exp) == 4:
                sign = '+'
            else:
                # Если есть несовпадение в знаках
                raise ArithmeticError('Expression might not a cube '
                                      'of sum because of a signs',
                                      cls.old)

            a2b3 = exp[1].split(' * ')
            ab23 = exp[2].split(' * ')
            # Создание аргументов
            a = varoper(varoper(ab23[1], '**', '2'), '**', '0.5')
            b = varoper(varoper(a2b3[2], '**', '2'), '**', '0.5')

            """
            testa3 = varoper(exp[0], '**', str(1/3))
            testb3 = varoper(exp[3], '**', str(1/3))
            testa2 = varoper(a2b3[1], '**', '0.5')
            testb2 = varoper(ab23[2], '**', '0.5')
            
            if a != testa3 or a != testa2:
                # Если первый аргумент не совпадает
                # с двумя проверками, то возможно выражение
                # не является кубом суммы
                raise ValueError('Argument', a, 'don\'t matches either',
                                 testa3, 'or', testa2)
            elif b != testb3 or a != testb2:
                # Если второй аргумент не совпадает
                # с двумя проверками, то возможно выражение
                # не является кубом суммы
                raise ValueError('Argument', b, 'don\'t matches either',
                                 testb3, 'or', testb2)
            """

            cls.ans = f'({a}{sign}{b})**3'

            return cls.ans

    @classmethod
    def quadeq(cls, equation, find: str or list = None) \
            -> str or list:
        """
        Квадратное уравнение

        a * x**2 + b * x + c = 0

        D = b**2 - 4 * a * c

        x1, x2 = (-b +/- D**0.5)/(2 * a)        (D > 0)

        x0 = -b/(2 * a)                         (D = 0)

        a * x**2 + b * x + c = a * (x - x1) * (x - x2)

        a * x**2 + b * x + c = a * (x - x0)**2  (D = 0)

        Теорема Виета

        x1 + x2 = -b/a                   (D > 0, a != 0)

        x1 * x2 = c/a                    (D > 0, a != 0)

        equation: принимает квадратное уравнение с переменной "x"
        во всех случаях.

        find: указывается то, что нужно найти по заранее прописанным
        значениям. "D" - дискриминант; "x1, x2"/"x1"/"x2"/"x0" -
        корень/корни уравнения (отсутствуют, если дискриминант
        меньше нуля); "revert" - сворачивает в произведение
        (если дискриминант не меньше нуля); "eq" - указывать только
        в том случае, если в параметре equation - разложение
        на множители (произведение с переменной x), в итоге возвращает
        уравнение; "x1 + x2" - сумма корней по теореме Виета;
        "x1 * x2" - произведение корней по теореме Виета.

        Возвращает то, что указано в аргументе find.
        """
        assert find, 'You must write one of 9 indicators ' \
                     'to get some result'
        # бязательно нужно ввести то, что нужно найти

        cls.old = equation
        eq = equation.replace(' + ', '   ')
        eq = eq.replace(' - ', '    -')
        if 'x**2 ' in equation and 'x ' in equation:
            # Если всё в порядке, присваивание осуществляется
            # трём аргументам
            x2, x, *c = eq.split('   ')
            eq = [x2, x] + c
        elif 'x**2 ' in equation or 'x ' in equation:
            # Если длины недостаточно, подразумевается,
            # что указано две переменные
            x2, *x = eq.split('   ')
            eq = [x2] + x
        else:
            # Иначе имеется в виду только одна переменная
            x2 = eq.split('   ')
            eq = [x2]

        if len(eq) == 1:
            #
            if x2.find('x**2') != -1:
                if len(x2) > 7:
                    a = x2[:-7]
                elif x2 == 'x**2':
                    a = '1'
                elif x2 == '-x**2':
                    a = '-1'

                b = c = '0'
            elif x2.find('x') != -1:
                if len(x2) > 4:
                    b = x2[:-4]
                elif x2 == 'x':
                    b = '1'
                elif x2 == '-x':
                    b = '-1'

                a = c = '0'
            else:
                c = x2
                a = b = '0'

        elif len(eq) == 2:
            #
            if x2.find('x**2') != -1:
                if len(x2) > 7 and ' * ' in x2:
                    a = x2[:-7]
                elif x2 == 'x**2':
                    a = '1'
                elif x2 == '-x**2':
                    a = '-1'

            elif x2.find('x') != -1:
                if len(x2) > 4 and ' * ' in x2:
                    b = x2[:-4]
                elif x2 == 'x':
                    b = '1'
                elif x2 == '-x':
                    b = '-1'

                a = '0'

            if type(x) == list:
                #
                if len(x) == 1:
                    x = x[0]
                elif len(x) > 1:
                    x = ' + '.join(x)
                    x = x.replace(' +  -', ' - ')

            if x.find('x') != -1:
                if len(x) > 4 and ' * ' in x:
                    b = x[:-4]
                elif x == 'x':
                    b = '1'
                elif x == '-x':
                    b = '-1'

                c = '0'
            else:
                c = x
                b = '0'

        elif len(eq) == 3:
            pass
        elif len(eq) > 3:
            pass

        if x.find(' *  x') != 1:
            b = x[:-4]
        elif x == 'x':
            b = '1'
        elif x == '-x':
            b = '-1'
        elif x.find('x') == -1 and len(eq.split('   ')) == 2:
            c = x

        try:
            if len(c) == 1:
                c = c[0]
            elif len(c) == 0:
                c = '0'
            else:
                c = ' + '.join(c)
                c = c.replace(' +  -', ' - ')

        except NameError:
            c = '0'

        def D(a, b, c, /):
            """
            Дискриминант квадратного уравнения

            D = b**2 - 4 * a * c

            Принимает коэффициенты квадратного уравнения
            и возвращает дискриминант.
            """

            b2 = varoper(b, '**', '2')   # Создание первого аргумента
            ac = varoper(a, '*', c)      # Создание второго аргумента
            ac4 = varoper('-4', '*', ac)
            ans = varoper(b2, '+', ac4)  # Формирование ответа

            return ans

        if find == 'D':
            return D(a, b, c)


ins = MainMath
ins.sqrsum('a**1.5', '5a**0.5', sign='-')
print(ins.res())
ins.sqrsum('4a**2 + 4a * b + b**2', reverse=True)
print(ins.res())
ins.difsqrs('4m**2', '16n**4')
print(ins.res())
ins.difsqrs('(n**0.5+m**0.5) * (n**0.5-m**0.5)', reverse=True)
print(ins.res())
ins.sumcubes('8a**3', '27b**3', sign='-')
print(ins.res())
ins.sumcubes('(a**1.5+b**1.5) * (a**3 - a**1.5 * b**1.5 + b**3)',
             reverse=True)
print(ins.res())
ins.cubesum('a', '3b**2')
print(ins.res())
ins.cubesum('125a**3 - 3 * 25a**2 * 6b + 3 * 5a * 36b**2 - 216b**3',
            reverse=True)
print(ins.res())

print(ins.quadeq('x**2 + 5 * x', find='D'))
