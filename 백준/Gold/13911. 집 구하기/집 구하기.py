import sys
from heapq import heappush, heappop

inp = lambda: map(int, sys.stdin.readline().split())
INF = sys.maxsize

def dijstra(start):
    dis = [INF] * (v + 3)
    dis[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
        dist, now = heappop(queue)
        if dis[now] < dist:
            continue
        for i in maps[now]:
            if i[0] == v + 1 or i[0] == v + 2:
                continue
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    return dis
v, e = inp()
maps = [[] for _ in range(v + 3)]
mp = v + 1
sp = v + 2
for _ in range(e):
    a, b, c = inp()
    maps[a].append((b, c))
    maps[b].append((a, c))

M, x = inp()
ml = list(inp())

S, y = inp()
sl = list(inp())

for i in ml:
    maps[mp].append((i, 0))
    maps[i].append((mp, 0))

for i in sl:
    maps[sp].append((i, 0))
    maps[i].append((sp, 0))
ans = -1

mm = dijstra(mp)
mm[v + 1] = 0
ss = dijstra(sp)
ss[v + 2] = 0
ans = INF
for i in range(1, v + 1):
    if not i in ml and not i in sl:
        if mm[i] <= x and ss[i] <= y:
            ans = min(ans, mm[i] + ss[i])

if ans == INF:
    print(-1)
else:
    print(ans)