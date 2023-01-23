import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijstra(start, check):
    queue = []
    heappush(queue, [0, start])

    dis = [int(1e10)] * (v + 1)
    dis[start] = 0

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        for i in maps[now]:
            if not check and i[0] == m:
                continue
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, [cost, i[0]])
    return dis
v, e = map(int, input().split())
maps = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    maps[a].append([b, c])

s, m, e = map(int, input().split())

S = dijstra(s, 1)
M = dijstra(m, 1)
E = dijstra(s, 0)

ans1 = S[m] + M[e]
ans2 = E[e]

print(ans1 if ans1 < int(1e10) else -1, ans2 if ans2 < int(1e10) else -1)