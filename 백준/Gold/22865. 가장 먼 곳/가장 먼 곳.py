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

n = int(input())
a, b, c = map(int, input().split())
m = int(input())

maps = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    maps[x].append((y, z))
    maps[y].append((x, z))

A = dijstra(a)
B = dijstra(b)
C = dijstra(c)

size = 0
ans = 0

for i in range(1, n + 1):
    if size < min(A[i], B[i], C[i]):
        size = min(A[i], B[i], C[i])
        ans = i
print(ans)

