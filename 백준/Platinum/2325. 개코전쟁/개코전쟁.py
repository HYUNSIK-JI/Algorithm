import sys
from heapq import heappop, heappush

INF = sys.maxsize
input = sys.stdin.readline

def dijstra(start):
    dis = [INF] * (n + 1)
    dis[start] = 0
    parent[start] = [start]
    queue = []
    heappush(queue, (0, start))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue

        for i in maps[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                parent[i[0]] = parent[now] + [i[0]]
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    return parent
def dijstra2(s, e):
    dis = [INF] * (n + 1)
    dis[1] = 0

    queue = []
    heappush(queue, (0, 1))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        for i in maps[now]:
            if now == s and i[0] == e:
                continue
            elif now == e and i[0] == now:
                continue
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    return dis
n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]
parent = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

k = dijstra(1)
ans = 0
for i in range(len(k[n]) - 1):
    ans = max(ans, dijstra2(k[n][i], k[n][i + 1])[n])
print(ans)