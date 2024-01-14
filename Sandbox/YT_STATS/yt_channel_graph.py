import shelve
from datetime import date

import matplotlib.pyplot as plt

warehouse = shelve.open('channel_stats')
WH = warehouse['names']
i = 8
data = warehouse[WH[i]]
data = sorted(data, key=lambda x: x['date'])

# print(len(PDP), PDP[0], PDP[-1])

"""
PDP = warehouse['PewDiePie']
PDP = sorted(PDP, key=lambda x: x['date'])
with open('PewDP.txt', encoding='utf-8') as f:
    t = f.readlines()[:0:-1]
    for d in t:
        try:
            y, m, n, *tt, vw, lk, cm = d.split()
        except ValueError:
            continue
        title = ' '.join(tt)
        date = eval(' '.join((y, m, n)))
        views = int(vw)
        likes = int(lk)
        comments = int(cm)

        nd = dict(date=date, title=title, views=views, likes=likes,
                  comments=comments)
        PDP.append(nd)

PDP = sorted(PDP, key=lambda x: x['date'])
warehouse['PewDiePie'] = PDP
"""

ax = plt.subplot()
# x = [d['date'][0]*10000 + d['date'][1]*100 + d['date'][2]
# for d in data]
# print(date(*data[0]['date']))
x = [date(*d['date']) for d in data]
# print(x[:50])

views = [d['views'] for d in data]
likes = [d['likes'] for d in data]
comments = [d['comments'] for d in data]
print(views[:10], list(map(len, (views, likes, comments))))

ax = plt.subplot()
ax.plot(x, views)
plt.xlabel('date')
plt.ylabel('views')
plt.title(WH[i] + '\'s views')
plt.savefig(WH[i] + '_views.png')
plt.close()

ax = plt.subplot()
ax.plot(x, likes)
plt.xlabel('date')
plt.ylabel('likes')
plt.title(WH[i] + '\'s likes')
plt.savefig(WH[i] + '_likes.png')
plt.close()

ax = plt.subplot()
ax.plot(x, comments)
plt.xlabel('date')
plt.ylabel('comments')
plt.title(WH[i] + '\'s comments')
plt.savefig(WH[i] + '_comments.png')
plt.close()

warehouse.close()
