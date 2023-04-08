import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

visit = [[False] * m for _ in range(n)]

maps = []
queue = deque()

for i in range(n):
    row = list(input().rstrip())
    for j in range(m):
        if row[j] == "W":
            queue.append((i, j))
    maps.append(row)

while queue:
    x, y = queue.popleft()
    visit[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == "+":
            tx = nx + dx[i]
            ty = ny + dy[i]

            if maps[tx][ty] == "+":
                nx, ny = tx, ty
            elif maps[tx][ty] == "W" or maps[tx][ty] == ".":
                nx, ny = tx, ty
                break
            else:
                break
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and not maps[nx][ny] == "#":
            visit[nx][ny] = True
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if not visit[i][j] and maps[i][j] == ".":
            print("P", end="")
        else:
            print(maps[i][j], end="")
    print()