import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijstra(start):

    dis[start] = 0
    queue = []
    heappush(queue, [0, start])

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        for i in maps[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, [cost, i[0]])

n = int(input())
m = int(input())

maps = [[] for _ in range(n + 1)]
dis = [int(1e9)] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))

s, e = map(int, input().split())

dijstra(s)
print(dis[e])