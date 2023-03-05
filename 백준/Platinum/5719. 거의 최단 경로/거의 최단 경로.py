import sys
from heapq import heappop, heappush

INF = sys.maxsize
input = sys.stdin.readline

def dijstra(start):
    dis[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue

        for i in maps[now]:
            cost = dist + i[1]
            if cost < dis[i[0]] and not check[now][i[0]]:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
def dijstra2(start):
    queue = []
    heappush(queue, (dis[start], start))

    while queue:
        dist, now = heappop(queue)

        if now == s:
            continue

        for i in reverse_maps[now]:
            if check[i[0]][now]:
                continue
            if dis[i[0]] == dis[now] - i[1]:
                check[i[0]][now] = True
                heappush(queue, (dis[i[0]], i[0]))
while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    s, e = map(int, input().split())

    maps = [[] for _ in range(n)]
    reverse_maps = [[] for _ in range(n)]

    check = [[False] * n for _ in range(n)]
    dis = [INF] * n
    for _ in range(m):
        u, v, p = map(int, input().split())
        maps[u].append((v, p))
        reverse_maps[v].append((u, p))
    dijstra(s)
    dijstra2(e)

    for i in range(n):
        dis[i] = INF
    dijstra(s)
    if dis[e] == INF:
        print(-1)
    else:
        print(dis[e])