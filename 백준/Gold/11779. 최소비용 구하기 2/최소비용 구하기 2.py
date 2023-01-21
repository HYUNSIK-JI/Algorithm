import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijstra(start):
    queue = []
    heappush(queue, (0, start))
    dis[start] = 0

    while queue:
        dist, now = heappop(queue)

        if dis[now] < dist:
            continue
        for i in maps[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                near[i[0]] = now
                heappush(queue, (cost, i[0]))

n = int(input())
m = int(input())

maps = [[] for _ in range(n + 1)]
dis = [int(1e9)] * (n + 1)
near = [0] * (n + 1)
ans = []
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
s, e = map(int, input().split())

dijstra(s)

temp = e
ans.append(e)
while not temp == s:
    ans.append(near[temp])
    temp = near[temp]
print(dis[e])
print(len(ans))
ans.reverse()
print(*ans)