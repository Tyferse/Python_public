# Цикл while

running = True
number = 23

while running:
    guess = int(input('Введите целое число : '))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False  # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')

else:
    print('Цикл while закончен.')
    # У цила  может быть оператор

print('Завершение.')

# Цикл for
for i in range(1, 5):
    print(i)
else:
    print('Цикл for закончен')
