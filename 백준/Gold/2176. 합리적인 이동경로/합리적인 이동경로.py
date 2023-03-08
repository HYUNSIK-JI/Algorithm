import sys
from heapq import heappush, heappop

INF = sys.maxsize
input = sys.stdin.readline

def dijstra(start):
    queue = []
    heappush(queue, (0, start))

    dis[start] = 0
    dp[start] = 1

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue

        for i in maps[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
            if dis[i[0]] < dist:
                dp[now] += dp[i[0]]

n, m = map(int, input().split())

maps = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)
dp = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

dijstra(2)

print(dp[1])