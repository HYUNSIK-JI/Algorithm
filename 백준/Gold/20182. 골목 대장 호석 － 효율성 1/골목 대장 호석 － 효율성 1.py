import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    dis = [INF] * (n + 1)
    dis[s] = 0

    queue = []
    heappush(queue, (0, s))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue

        for i in maps[now]:
            cost = dist + i[1]

            if cost < dis[i[0]] and i[1] <= start:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    if dis[e] > mo:
        return INF
    else:
        return dis[e]
n, m, s, e, mo = map(int, input().split())

maps = [[] for _ in range(n + 1)]
money = []
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))
    money.append(c)

left, right = 0, m - 1
money.sort()
ans = INF

while left <= right:
    mid = (left + right) // 2

    result = dijstra(money[mid])

    if result == INF:
        left = mid + 1
    else:
        right = mid - 1
        ans = min(ans, money[mid])

if ans == INF:
    print(-1)
else:
    print(ans)