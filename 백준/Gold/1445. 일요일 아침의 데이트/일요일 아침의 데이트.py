import sys
from heapq import heappush, heappop

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = []
    heappush(queue, (0, 0, a, b))
    visit[a][b] = True

    while queue:
        c1, c2, x, y = heappop(queue)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                visit[nx][ny] = True
                if maps[nx][ny] == ".":
                    heappush(queue, (c1, c2, nx, ny))
                elif maps[nx][ny] == "x":
                    heappush(queue, (c1, c2 + 1, nx, ny))
                elif maps[nx][ny] == "g":
                    heappush(queue, (c1 + 1, c2, nx, ny))
                else:
                    print(c1, c2)
                    return
n, m = map(int, input().split())

s_x, s_y = 0, 0
e_x, e_y = 0, 0

maps = []
G = []
for i in range(n):
    row = list(input().rstrip())
    for j in range(m):
        if row[j] == "S":
            s_x, s_y = i, j
        elif row[j] == "F":
            e_x, e_y = i, j
        elif row[j] == "g":
            G.append((i, j))
    maps.append(row)

for x, y in G:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == ".":
            maps[nx][ny] = "x"

visit = [[False] * m for _ in range(n)]
bfs(s_x, s_y)
