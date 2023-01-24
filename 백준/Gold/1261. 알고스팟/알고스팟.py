import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    visit[0][0] = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        if x == m - 1 and y == n - 1:
            return visit[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == -1:
                if maps[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
                else:
                    visit[nx][ny] = visit[x][y]
                    queue.appendleft((nx, ny))

n, m = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(m)]
visit = [[-1] * n for _ in range(m)]
print(bfs())