import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0, 0))

    visit[0][0] = 1

    cheeze = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not maps[nx][ny]:
                    if not visit[nx][ny]:
                        queue.append((nx, ny))
                else:
                    if visit[nx][ny] >= 2:
                        cheeze.append((nx, ny))
                visit[nx][ny] += 1
    for i in range(n):
        for j in range(m):
            if visit[i][j] >= 2:
                maps[i][j] = 0

def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j]:
                cnt += 1
    return cnt
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

time = 0
while True:
    if not check():
        break
    visit = [[0] * m for _ in range(n)]
    bfs()
    time += 1
print(time)