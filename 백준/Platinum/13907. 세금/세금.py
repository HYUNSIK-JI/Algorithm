import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize


def dijstra(start):
    dis = [[INF] * n for _ in range(n + 1)]
    dis[start][0] = 0
    queue = []
    heappush(queue, (0, 0, start))

    while queue:
        dist, now_cnt, now = heappop(queue)
        check = False
        for i in range(now_cnt):
            if dis[now][i] < dist:
                check = True
                break
        if not check:
            if dis[now][now_cnt] < dist or now_cnt == d - 1:
                continue
            for i in maps[now]:
                cost = dist + i[1]
    
                if cost < dis[i[0]][now_cnt + 1]:
                    dis[i[0]][now_cnt + 1] = cost
                    heappush(queue, (cost, now_cnt + 1, i[0]))
    return dis


n, m, k = map(int, input().split())
s, d = map(int, input().split())

maps = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

tax = [0]
for _ in range(k):
    tax.append(int(input()) + tax[-1])
S = dijstra(s)[d]
ans = []

for t in tax:
    mn = INF
    for i, cost in enumerate(S):
        mn = min(mn, cost + i * t)
    ans.append(mn)
print(*ans, sep="\n")

