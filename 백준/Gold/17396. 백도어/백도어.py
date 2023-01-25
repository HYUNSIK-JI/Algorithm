import sys
from heapq import heappush, heappop

INF = sys.maxsize
inp = lambda: map(int, sys.stdin.readline().split())

def dijstra(start):
    dis = [INF] * n
    dis[start] = 0

    queue = []
    heappush(queue, (start, 0))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        if nex[now]:
            continue
        for i in maps[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    return dis
n, m = inp()

nex = list(inp())

maps = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = inp()
    maps[a].append((b, c))
    maps[b].append((a, c))

S = dijstra(0)
if S[n - 1] == INF:
    print(-1)
else:
    print(S[n - 1])