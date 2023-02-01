
# 각각 팀원들의 집에서 다익스트라 진행 이떄 kist, 씨알 푸드 비용을 구해서 inf이면 -1 아니면 그대로 이합을 어떤 리스트에 넣는다.

import sys
from heapq import heappush, heappop

INF = sys.maxsize
inp = lambda: map(int, sys.stdin.readline().split())

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

n, v, e = inp()

maps = [[] for _ in range(v + 1)]

k_p, f_p = inp()

hs = list(inp())

for _ in range(e):
    a, b, c = inp()
    maps[a].append((b, c))
    maps[b].append((a, c))

ans = 0
for i in hs:
    d = 0
    S = dijstra(i)
    if S[k_p] == INF:
        d -= 1
    else:
        d += S[k_p]
    if S[f_p] == INF:
        d -= 1
    else:
        d += S[f_p]
    ans += d
print(ans)