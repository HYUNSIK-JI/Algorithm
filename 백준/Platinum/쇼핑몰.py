import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    queue = []
    heappush(queue, (0, start))

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
n, m, k = map(int, input().split())

maps = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))
    edge.append((a, b, c))

shopping = [int(input()) for _ in range(k)]
ans = 0
for a in shopping:
    dijstra(a)

for a, b, c in edge:
    ans = max(ans, (dis[a] + dis[b] + c + 1) // 2)
print(ans)