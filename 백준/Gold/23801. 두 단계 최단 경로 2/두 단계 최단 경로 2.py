import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    queue = []
    heappush(queue, (0, start))

    dis = [INF] * (n + 1)
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

n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))
s, e = map(int, input().split())
p = int(input())

ans = int(INF)
mid = list(map(int, input().split()))

S = dijstra(s)
E = dijstra(e)

for k in mid:
    ans = min(ans, S[k] + E[k])
print(ans if ans < int(INF) else -1)