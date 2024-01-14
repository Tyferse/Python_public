n = input()
is_even = [1 if int(c) % 2 == 0 else 0 for c in n]
print(sum(is_even))
