import sys
from heapq import heappush, heappop

INF = sys.maxsize
input = sys.stdin.readline

def dijstra():
    dis = [[INF] * (max(oils) + 1) for _ in range(n + 1)]
    dis[1][oils[1]] = 0

    queue = []
    heappush(queue, (0, oils[1], 1))

    while queue:
        dist, c, now = heappop(queue)

        if now == n:
            return dist
        if dis[now][c] < dist:
            continue

        for i in maps[now]:
            cost = min(oils[i[0]], c)

            if dist + c * i[1] < dis[i[0]][c]:
                dis[i[0]][c] = dist + c * i[1]
                heappush(queue, (dist + c * i[1], cost, i[0]))
n, m = map(int, input().split())
oils = [0] + list(map(int, input().split()))
maps = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

print(dijstra())