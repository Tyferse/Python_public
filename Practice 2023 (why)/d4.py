n, k = map(int, input().split())
kaggles = [True] * n
for _ in range(k):
    li, ri = map(int, input().split())
    for i in range(li - 1, ri):
        kaggles[i] = False

print(''.join(['I' if kg else '.' for kg in kaggles]))
