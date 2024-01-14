import pickle


s = pickle.load(open('fast_calendar.data', 'rb'))

try:
    while s:
        a = input('Следующая дата: ')
        if a in s:
            s.remove(a)
            print('OК ' + str(len(s)))
        elif a == ' ':
            raise ValueError('Session was ended.')
        else:
            print('This date exists.')
    else:
        print('The END!!!')
finally:
    pickle.dump(s, open('fast_calendar.data', 'wb'))
