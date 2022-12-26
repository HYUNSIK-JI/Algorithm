import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def dijstra():
    queue = []
    dis = [INF] * (n + 1)

    for i in p:
        heappush(queue, (0, i))
        dis[i] = 0
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

n, m, k = map(int, input().split())
maps = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[b].append((a, c))

p = list(map(int, input().split()))

size = 0
ans = 0

d = dijstra()

for i in range(1, n + 1):
    if size < d[i]:
        size = d[i]
        ans = i
print(ans)
print(size)
