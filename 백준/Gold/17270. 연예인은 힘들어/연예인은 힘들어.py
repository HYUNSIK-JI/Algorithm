import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    dis = [INF] * (v + 1)
    dis[start] = 0

    queue = []
    heappush(queue, (0, start))

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

v, m = map(int, input().split())

maps = [[] for _ in range(v + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

j, s = map(int, input().split())
k1 = dijstra(j)
k2 = dijstra(s)

ans = sys.maxsize
answer = []
for i in range(1, v + 1):
    if i != j and i != s:
        ans = min(ans, k1[i] + k2[i])

for i in range(1, v + 1):
    if i != j and i != s:
        if k1[i] + k2[i] == ans and k1[i] <= k2[i]:
            heappush(answer, (k1[i], i))
if not answer:
    print(-1)
else:
    print(answer[0][1])