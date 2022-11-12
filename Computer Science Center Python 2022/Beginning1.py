import main


print(dir(main))
main.print_hi('Python')
print(main.__name__, main.__file__, sep='\n')

print(type(main), type(main.print_hi), type(type))

to_be = False
print(to_be or not to_be)

print('even' if 42 % 2 == 0 else 'odd')
