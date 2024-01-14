n = int(input())
cities = {}
for _ in range(n):
    country, *cts = input().split()
    for ct in cts:
        cities[ct] = country

k = int(input())
req = [input() for _ in range(k)]
for i in range(k):
    print(cities[req[i]])
