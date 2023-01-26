import sys
from heapq import heappush, heappop

inp = lambda: map(int, sys.stdin.readline().split())
INF = sys.maxsize

def dijstra(s, e):
    dis = [INF] * (n + 1)
    dis[1] = 0

    queue = []
    heappush(queue, (0, 1))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        for i in maps[now]:
            cost = dist + i[1]

            if s == now and e == i[0] or s == i[0] and e == now:
                continue
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                near[i[0]] = now
                heappush(queue, (cost, i[0]))
    return dis

n, m = inp()
maps = [[] for _ in range(n + 1)]
near = [0] * (n + 1)
for _ in range(m):
    a, b, c = inp()
    maps[a].append((b, c))
    maps[b].append((a, c))

S = dijstra(0, 0)
ans = -1
k = n
while not k == 1:
    s = near[k]
    dis = dijstra(s, k)
    if dis[n] == INF:
        print(-1)
        exit()
    ans = max(ans, dis[n] - S[n])
    k = s
print(ans)