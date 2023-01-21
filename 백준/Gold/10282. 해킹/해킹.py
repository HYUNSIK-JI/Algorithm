import sys
from heapq import heappush, heappop

input = sys.stdin.readline

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

for _ in range(int(input())):
    n, d, c = map(int, input().split())

    maps = [[] for _ in range(n + 1)]
    dis = [int(1e9)] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        maps[b].append((a, s))
    dijstra(c)
    ans = []
    for i in dis:
        if not i == int(1e9):
            ans.append(i)
    print(len(ans), max(ans))