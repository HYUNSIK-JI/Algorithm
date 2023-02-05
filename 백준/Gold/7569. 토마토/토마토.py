import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

m, n, h = map(int, input().split())
maps = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[0] * m for _ in range(n)] for _ in range(h)]

queue = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if maps[z][x][y] == 1:
                queue.append((x, y, z))

while queue:
    x, y, z = queue.popleft()
    visit[z][x][y] = 1

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and not visit[nz][nx][ny] and not maps[nz][nx][ny]:
            maps[nz][nx][ny] = maps[z][x][y] + 1
            visit[nz][nx][ny] = 1
            queue.append((nx, ny, nz))

check = False
mx = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if not maps[z][x][y]:
                check = True
            mx = max(mx, maps[z][x][y])
if check:
    print(-1)
else:
    print(mx - 1)