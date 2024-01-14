wl = {}
word = input().upper()
while word:
    code = sum(ord(c) - ord('A') + 1 for c in word)
    wl[word] = code
    word = input().upper()

print(*dict(sorted(wl.items(), key=lambda x: (x[1], x[0]))).keys())
