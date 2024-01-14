import sys
from collections import defaultdict as ddict

data = sys.stdin.readline()
db = ddict(lambda: ddict(int))
while data != '\n':
    customer, product, count = data.split()
    db[customer][product] += int(count)
    
    data = sys.stdin.readline()

for customer in db:
    db[customer] = dict(sorted(db[customer].items()))

db = dict(sorted(db.items()))
for customer in db:
    print(customer, ':', sep='')
    for product in db[customer]:
        print(product, db[customer][product])
