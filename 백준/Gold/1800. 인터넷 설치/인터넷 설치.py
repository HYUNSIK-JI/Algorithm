import sys
from heapq import heappush, heappop

INF = sys.maxsize
inp = lambda: map(int, sys.stdin.readline().split())

def dijstra(start, mx):
    dis = [INF] * n
    dis[start] = 0

    queue = []
    heappush(queue, (0, start))

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        for i in maps[now]:
            cost = dist

            if i[1] > mx:
                cost += 1
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(queue, (cost, i[0]))
    if dis[n - 1] <= k:
        return 1
    return 0

n, p, k = inp()
maps = [[] for _ in range(n)]

mx_cost = -1
for _ in range(p):
    a, b, c = inp()
    a -= 1
    b -= 1
    maps[a].append((b, c))
    maps[b].append((a, c))
    mx_cost = max(mx_cost, c)


start, end = 0, mx_cost
ans = -1
while start <= end:
    mid = (start + end) // 2

    if dijstra(0, mid):
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
print(ans)