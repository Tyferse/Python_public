import calendar
import random

year = int(input('Введите год: '))
months = ['', 'январь', "февраль", "март", "апрель", "май", "июнь",
          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

holidays = [0] * 366
with open('holiday_list.txt', encoding='utf-8') as t:
    for i in range(366):
        s = t.readline().rstrip().split(', ')
        if s[0][:2].isdigit():
            # print(s[0][:2], s[0][3:])
            holidays[i] = [s[0][3:]] + s[1:]
        elif s[0][0].isdigit():
            holidays[i] = [s[0][2:]] + s[1:]
        else:
            holidays[i] = s

i = 0
for month in range(1, 13):
    k = 366 if calendar.monthrange(year, 2)[1] > 28 else 365
    for day in range(1, calendar.monthrange(year, month)[1]+1):
        if len(holidays[i]) > 1:
            print(day, months[month], '-', random.choice(holidays[i]))
        else:
            print(day, months[month], '-', holidays[i][0])
        i += 1
        if k == 365 and month == 2 and day == 28:
            i += 1
