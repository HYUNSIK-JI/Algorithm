import sys
import math
from heapq import heappush, heappop

INF = math.inf
input = sys.stdin.readline

def dijkstra(start, maps, dist):
    queue = []
    dist[start] = 0
    for i in range(len(maps[start])):
        cost, des = maps[start][i]
        queue.append((cost, des, des))
        dist[des] = cost
    while queue:
        cost, vertex, prev = heappop(queue)
        if cost != dist[vertex]:
            continue
        p[vertex] = prev
        for i in maps[vertex]:
            new_cost = cost + i[0]
            if dist[i[1]] > new_cost:
                dist[i[1]] = new_cost
                heappush(queue, (dist[i[1]], i[1], prev))

n, m = map(int, input().split())

# 정방향 간선 리스트
maps = [[] for _ in range(n)]

# 역방향 간선 리스트
maps2 = [[] for _ in range(n)]

queue = []

dist = [INF] * n
dist2 = [INF] * n

p = [-1] * n

for _ in range(m):
    a, b, c, d = map(int, input().split())
    a, b = a - 1, b - 1

    maps[a].append((c, b))
    maps[b].append((d, a))

    maps2[a].append((d, b))
    maps2[b].append((c, a))

dijkstra(0, maps, dist)

ans = INF
for i in range(len(maps2[0])):
    col = maps2[0][i][1]
    heappush(queue, (maps2[0][i][0], col, 0))
    dist2[col] = maps2[0][i][0]
    dist2[0] = 0
    while queue:
        cost, vertex, prev = heappop(queue)
        if cost != dist2[vertex]:
            continue
        if p[vertex] != col:
            ans = min(ans, cost + dist[vertex])
            continue
        for tt in maps2[vertex]:
            if dist2[tt[1]] > cost + tt[0]:
                dist2[tt[1]] = cost + tt[0]
                heappush(queue, (dist2[tt[1]], tt[1], 0))
        if vertex == col:
            dist2[0] = INF

print(ans)