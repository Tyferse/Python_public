p1 = map(float, input().split())
p2 = map(float, input().split())
print(f'{sum((x1 - x2)**2 for x1, x2 in zip(p1, p2))**0.5:.3f}')
