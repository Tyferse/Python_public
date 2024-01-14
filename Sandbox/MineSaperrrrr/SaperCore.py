import random
import tkinter
import itertools


field_size = None
nmines = None
while not field_size and not nmines:
    field_size = input()
    if len(field_size.split()) != 2:
        print("You are idiot? Try it again.")
        field_size = None
        continue
    
    try:
        field_size = tuple(map(int, field_size.split()))
        nmines = int(input())
        if (nmines > field_size[0] * field_size[1] or nmines < 1) or \
           (field_size[0] < 1 or field_size[1] < 1):
            raise ValueError
        
    except ValueError:
        print("Your number of mines was incorrect! Try again.")
        field_size = None
        nmines = None
        continue

field = []
nm = nmines
cell = 0
j = 0
while nm and j // field_size[0] < field_size[1]:
    cell = int(random.randint(0, field_size[0] * field_size[1])
               < nmines)
    if cell:
        nm -= 1
    
    if j > field_size[0] * field_size[1] \
       and cell and not field[j % field_size[0]]:
        field[j % field_size[0]] = cell
    else:
        field.append(cell)
        
    j += 1
    if not (len(field) % field_size[0]):
        print(field[j % field_size[0] - field_size[0]:j],
              '-', j // field_size[0])
    
    if j == field_size[0] * field_size[1]:
        j = 0
    

for i in range(field_size[0], field_size[0] * field_size[1],
               field_size[0]):
    print(field[i-field_size[0]:i])
