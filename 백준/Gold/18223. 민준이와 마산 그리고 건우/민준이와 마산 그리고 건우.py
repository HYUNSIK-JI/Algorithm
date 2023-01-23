import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    queue = []
    heappush(queue, (0, start))
    dis = [INF] * (v + 1)
    dis[start] = 0

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        for i in maps[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    return dis

v, e, p = map(int, input().split())
maps = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))


S = dijstra(1)
P = dijstra(p)

print("SAVE HIM" if S[v] == S[p] + P[v] else "GOOD BYE")