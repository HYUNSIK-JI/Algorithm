import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    dis = [INF] * m
    dis[start] = 0
    parent = [[] for _ in range(m)]
    parent[start] = [start]
    queue = []
    heappush(queue, (0, start))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue

        for i in maps[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                parent[i[0]] = parent[now] + [i[0]]
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    return parent
for test_case in range(int(input())):
    n, m = map(int, input().split())
    maps = [[] for _ in range(m)]

    for _ in range(n):
        a, b, c = map(int, input().split())
        maps[a].append((b, c))
        maps[b].append((a, c))
    k = dijstra(0)
    if k[-1]:
        print(f"Case #{test_case + 1}:", end=" ")
        print(*k[-1])
    else:
        print(f"Case #{test_case + 1}: {-1}")