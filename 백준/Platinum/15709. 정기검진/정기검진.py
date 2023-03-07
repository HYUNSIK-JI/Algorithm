import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    queue = []
    dis[start - n - m][start] = 0
    heappush(queue, (0, start))

    while queue:
        dist, now = heappop(queue)

        if dis[start - n - m][now] < dist:
            continue
        for i in maps[now]:
            cost = dist + i[1]
            if cost < dis[start - n - m][i[0]]:
                dis[start - n - m][i[0]] = cost
                heappush(queue, (cost, i[0]))

n, m, b, k, q = map(int, input().split())
maps = [[] for _ in range(n + m + b + 1)]
dis = [[INF] * (n + m + b + 1) for _ in range(b + 1)]

for _ in range(k):
    x, y, z = map(int, input().split())
    maps[x].append((y, z))
    maps[y].append((x, z))

for i in range(n + m + 1, n + m + b + 1):
    dijstra(i)
for _ in range(q):
    ss, ee = map(int, input().split())
    ans = INF
    for i in range(n + m + 1, n + m + b + 1):
        ans = min(ans, dis[i - n - m][ss] + dis[i - n - m][ee])
    if ans == INF:
        print(-1)
    else:
        print(ans)