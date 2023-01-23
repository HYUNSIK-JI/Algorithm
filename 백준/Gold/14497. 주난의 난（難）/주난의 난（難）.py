import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = 0

    while queue:
        x, y = queue.popleft()

        if x == (x2 - 1) and y == (y2 - 1):
            return visit[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
                if maps[nx][ny] == "1":
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
                else:
                    visit[nx][ny] = visit[x][y]
                    queue.appendleft((nx, ny))


n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]
print(bfs(x1 - 1, y1 - 1))