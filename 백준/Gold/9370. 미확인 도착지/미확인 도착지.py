import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijstra(start):
    queue = []
    heappush(queue, (0, start))
    dis = [int(1e9) for _ in range(n + 1)]
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
    return dis
for _ in range(int(input())):
    n, m, t = map(int, input().split())

    maps = [[] for _ in range(n + 1)]


    s, g, h = map(int, input().split())

    for _ in range(m):
        a, b, d = map(int, input().split())
        maps[a].append((b, d))
        maps[b].append((a, d))

    candidate = []
    for _ in range(t):
        candidate.append(int(input()))

    S = dijstra(s)
    G = dijstra(g)
    H = dijstra(h)

    ans = []
    for a in candidate:
        if S[g] + G[h] + H[a] == S[a] or S[h] + H[g] + G[a] == S[a]:
            ans.append(a)
    ans.sort()
    print(*ans)