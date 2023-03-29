import sys
from bisect import bisect_right
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    dis = [INF] * (n + 1)
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
def update(i, val):
    global  arr
    while i < len(arr) and arr[i] > val:
        arr[i] = val
        i |= i + 1

def getmin(i):
    global arr
    res = INF
    while i >= 0:
        res = min(res, arr[i])
        i = (i & (i + 1)) - 1
    return res
n = int(input())
A, B, C = map(int, input().split())

m = int(input())
maps = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a].append((b, c))
    maps[b].append((a, c))

dis_B = dijstra(B)

distance = sorted(zip(dijstra(A), dis_B, dijstra(C), range(n + 1)))
distance.pop()

dis_B.sort()
dis_B.pop()

arr = [INF] * n
check = [False] * (n + 1)

s = []
last = -1

for a, b, c, i in distance:
    if a != last:
        for bi, sc in s:
            update(bi + 1, sc)
        s = []
    last = a

    if b == dis_B[0]:
        check[i] = True
        s.append((-1, c))
        continue
    bi = bisect_right(dis_B, b - 1) - 1
    c_mn = getmin(bi)

    if c_mn >= c:
        check[i] = True
    s.append((bi, c))

for _ in range(int(input())):
    if check[int(input())]:
        print("YES")
    else:
        print("NO")