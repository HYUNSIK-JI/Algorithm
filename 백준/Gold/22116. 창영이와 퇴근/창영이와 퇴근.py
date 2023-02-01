import sys
from heapq import heappush, heappop

INF = sys.maxsize

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijstra():
    queue = []
    heappush(queue, (0, 0, 0))

    dis = [[INF] * n for _ in range(n)]
    dis[0][0] = 0

    while queue:
        dist, x, y = heappop(queue)

        if dis[x][y] < dist:
            continue
        if x == n - 1 and y == n - 1:
            print(dis[x][y])
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = max(dist, abs(maps[nx][ny] - maps[x][y]))

                if cost < dis[nx][ny]:
                    dis[nx][ny] = cost
                    heappush(queue, (cost, nx, ny))
    return
n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
dijstra()
