import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0))

    visit[0][0] = 0

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visit[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
                if maps[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
                else:
                    visit[nx][ny] = visit[x][y]
                    queue.appendleft((nx, ny))

m, n = map(int, input().split())

maps = [list(map(int, input().rstrip())) for _ in range(n)]

visit = [[-1] * m for _ in range(n)]

print(bfs())