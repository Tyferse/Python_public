import sys

words = {}
text = sys.stdin.readline()
while text != '\n':
    text = text.split()
    for w in text:
        if w not in words:
            words[w] = 1
        else:
            words[w] += 1
    
    text = sys.stdin.readline()
    # print(repr(text))

print(*dict(sorted(words.items(), key=lambda x: (-x[1], x[0]),
                   )).keys(), sep='\n')
