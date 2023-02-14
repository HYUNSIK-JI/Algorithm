import sys

INF = sys.maxsize

n, m = map(int, input().split())

maps = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    maps[a - 1][b - 1] = 1
    maps[b - 1][a - 1] = 1

for a in range(n):
    for b in range(n):
        if a == b:
            maps[a][b] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])
ans = []

for i in maps:
    ans.append(sum(i))
print(ans.index(min(ans)) + 1)