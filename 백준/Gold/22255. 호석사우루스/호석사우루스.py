import sys
from heapq import heappush, heappop

INF = sys.maxsize
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dijstra(a, b, start):
    queue = []
    heappush(queue, (0, start, a, b))
    dis[a][b][1] = 0

    while queue:
        dist, c, x, y = heappop(queue)

        if x == (e_x - 1) and y == (e_y - 1):
            return dist

        if not c % 3:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny] == -1:
                    cost = dist + maps[nx][ny]

                    if cost < dis[nx][ny][(c + 1) % 3]:
                        dis[nx][ny][(c + 1) % 3] = cost
                        heappush(queue, (cost, c + 1, nx, ny))

        if c % 3 == 1:
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny] == -1:
                    cost = dist + maps[nx][ny]

                    if cost < dis[nx][ny][(c + 1) % 3]:
                        dis[nx][ny][(c + 1) % 3] = cost
                        heappush(queue, (cost, c + 1, nx, ny))
        else:
            for i in range(2, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny] == -1:
                    cost = dist + maps[nx][ny]

                    if cost < dis[nx][ny][(c + 1) % 3]:
                        dis[nx][ny][(c + 1) % 3] = cost
                        heappush(queue, (cost, c + 1, nx, ny))
    return -1

n, m = map(int, input().split())

s_x, s_y, e_x, e_y = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

dis = [[[INF] * 3 for _ in range(m)] for _ in range(n)]

print(dijstra(s_x - 1, s_y - 1, 1))