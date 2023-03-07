import sys
from heapq import heappush, heappop

INF = sys.maxsize
input = sys.stdin.readline

def dijstra(start):
    queue = []
    heappush(queue, (k, start))

    dis[start] = k
    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue

        for i in maps[now]:
            cost = gondola[now][i[0]]

            if cost and cost[0] <= dist <= cost[1]:
                new_cost = cost[1] + i[1]
            else:
                new_cost = dist + i[1]

            if new_cost < dis[i[0]]:
                dis[i[0]] = new_cost
                heappush(queue, (new_cost, i[0]))

n, m = map(int, input().split())
a, b, k, g = map(int, input().split())

gondola_load = list(map(int, input().split()))

maps = [[] for _ in range(n + 1)]
load = [[0] * (n + 1) for _ in range(n + 1)]
gondola = [[(0, 0)] * (n + 1) for _ in range(n + 1)]
dis = [INF] * (n + 1)

for _ in range(m):
    u, v, l = map(int, input().split())
    maps[u].append((v, l))
    maps[v].append((u, l))
    load[u][v] = l
    load[v][u] = l

time = 0
for i in range(g - 1):
    s, e = gondola_load[i], gondola_load[i + 1]
    t = load[s][e]
    
    gondola[s][e] = (time, time + t)
    gondola[e][s] = (time, time + t)
    
    time += t

dijstra(a)

print(dis[b] - k)