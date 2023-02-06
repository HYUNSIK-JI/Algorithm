import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dr = [1, 2, 4, 8]
def check():
    mx = 0
    for x in range(m):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if visit[x][y] != visit[nx][ny]:
                        mx = max(mx, rooms[visit[x][y] - 1] + rooms[visit[nx][ny] - 1])
    return mx
def bfs(a, b):
    visit[a][b] = f + 1
    queue = deque()
    queue.append((a, b))
    cnt = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and dr[i] & ~ maps[nx][ny]:
                visit[nx][ny] = f + 1
                cnt += 1
                queue.append((nx, ny))
    return cnt
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
visit = [[0] * n for _ in range(m)]

f = 0
s = 0

for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            s = max(s, bfs(i, j))
            f += 1
rooms = [0] * f
for i in range(m):
    for j in range(n):
        rooms[visit[i][j] - 1] += 1

print(f)
print(s)
print(check())