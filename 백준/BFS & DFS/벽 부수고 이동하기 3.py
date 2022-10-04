import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0, 0, 1, 0))

    visit[0][0][0] = 1

    while queue:
        x, y, z, dist, time = queue.popleft()

        if visit[x][y][z] != dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:

                if maps[nx][ny] == 0 and visit[nx][ny][z] > dist + 1:

                    visit[nx][ny][z] = dist + 1
                    queue.append((nx, ny, z, dist + 1, 1 - time))

                elif z < k and maps[nx][ny] == 1:
                    if time == 0 and visit[nx][ny][z + 1] > dist + 1:
                        visit[nx][ny][z + 1] = dist + 1
                        queue.append((nx, ny, z + 1, dist + 1, 1))

                    elif time == 1 and visit[nx][ny][z + 1] > dist + 2:
                        visit[nx][ny][z + 1] = dist + 2
                        queue.append((nx, ny, z + 1, dist + 2, 1))

n, m, k = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
visit = [[[1e9] * (k + 1) for _ in range(m)] for _ in range(n)]
bfs()
answer = min(visit[-1][-1])
print(answer if answer != 1e9 else -1)