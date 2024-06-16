import os
from PIL import Image, EpsImagePlugin


EpsImagePlugin.gs_windows_binary = r"C:\Program Files\gs\gs10.03.0\bin\gswin64c"
for frame in os.listdir('meshframes'):
    im = Image.open('meshframes/' + frame)
    fig = im.convert('RGBA')
    fig.save('madeframes/' + frame.rsplit('.', 1)[0] + '.png', lossless=True)


# вывод номеров пропущенных кадров
nums = set()
for frame in os.listdir('madeframes'):
    n = int(frame.rsplit('_', 1)[1].rsplit('.', 1)[0])
    nums.add(n)


print(sorted(list(set(range(1, 6573)) - nums)))
