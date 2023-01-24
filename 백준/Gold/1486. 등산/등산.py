import sys
from heapq import heappush, heappop

INF = sys.maxsize
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijstra(s_x, s_y):
    queue = []
    heappush(queue, (0, s_x, s_y))

    dis = [[INF] * m for _ in range(n)]
    dis[s_x][s_y] = 0

    while queue:
        dist, x, y = heappop(queue)

        if dis[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                g = maps[nx][ny] - maps[x][y]

                if abs(g) <= t:
                    if g <= 0:
                        time = 1
                    else:
                        time = g ** 2
                    cost = dist + time
                    if cost < dis[nx][ny]:
                        dis[nx][ny] = cost
                        heappush(queue, (cost, nx, ny))
    return dis
n, m, t, d = map(int, input().split())

maps = []
dis = [[INF] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    row = list(input().rstrip())
    for j in range(m):
        k = ord(row[j])
        if k >= 97:
            row[j] = k - 71
        else:
            row[j] = k - 65
    maps.append(row)

S = dijstra(0, 0)

q = []
ans = 0
for i in range(n):
    for j in range(m):
        if S[i][j] <= d:
            q.append((i, j))

while q:
    x, y = q.pop()
    E = dijstra(x, y)

    if S[x][y] + E[0][0] <= d:
        ans = max(ans, maps[x][y])
print(ans)