import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0, 1))

    visit[0][0][1] = 1

    while queue:
        x, y, c = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visit[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and c:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append((nx, ny, 0))

                if not maps[nx][ny] and not visit[nx][ny][c]:
                    visit[nx][ny][c] = visit[x][y][c] + 1
                    queue.append((nx, ny, c))
    return -1
n, m = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]

visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())
