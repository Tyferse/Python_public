k = int(input())

teams = []
for i in range(k):
    n = int(input())
    teams.append({})
    for _ in range(n):
        student, tasks = input().split()
        teams[i][student] = int(tasks)

print('ДА' if all(any(i > 1 for i in teams[i].values())
                  for i in range(k)) else 'НЕТ')
