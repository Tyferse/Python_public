def check_pin(pin_code):
    a, b, c = map(int, pin_code.split('-'))
    
    if a == 1:
        return 'Некорректен'
    elif a > 3:
        for d in range(2, round(a**.5) + 1):
            if a % d == 0:
                return 'Некорректен'
    
    if str(b) != str(b)[::-1]:
        return 'Некорректен'
    
    while c > 1:
        if c % 2 == 0:
            c = c // 2
        else:
            return 'Некорректен'
    
    return 'Корректен'


print(check_pin('17-282-8'))
