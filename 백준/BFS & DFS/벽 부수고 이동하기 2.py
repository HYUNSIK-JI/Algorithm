<<<<<<< HEAD
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    visit[a][b][c] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visit[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == "1" and z > 0 and not visit[nx][ny][z - 1]:

                    visit[nx][ny][z - 1] = visit[x][y][z] + 1
                    queue.append((nx, ny, z - 1))

                elif maps[nx][ny] == "0" and not visit[nx][ny][z]:

                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append((nx, ny, z))

    return -1

n, m, k = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visit = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, k))
=======
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    visit[a][b][c] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visit[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == "1" and z > 0 and not visit[nx][ny][z - 1]:

                    visit[nx][ny][z - 1] = visit[x][y][z] + 1
                    queue.append((nx, ny, z - 1))

                elif maps[nx][ny] == "0" and not visit[nx][ny][z]:

                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append((nx, ny, z))

    return -1

n, m, k = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visit = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, k))
>>>>>>> 6235ff20caf464fa54259d6b52e3e231f8f03ef4
print(visit)