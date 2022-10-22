import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    sheep, walf = 0, 0
    if maps[a][b] == "v":
        walf += 1
    elif maps[a][b] == "o":
        sheep += 1
    queue = deque()
    queue.append((a, b))
    visit[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if maps[nx][ny] != "#":
                    if maps[nx][ny] == "v":
                        queue.append((nx, ny))
                        visit[nx][ny] = True
                        walf += 1
                    elif maps[nx][ny] == "o":
                        queue.append((nx, ny))
                        visit[nx][ny] = True
                        sheep += 1
                    else:
                        queue.append((nx, ny))
                        visit[nx][ny] = True
    if not sheep and not walf:
        return 0, 0
    elif sheep > walf:
        return sheep, 1
    else:
        return walf, 2


n, m = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
ans = [0, 0]
for i in range(n):
    for j in range(m):
        if maps[i][j] != "#" and not visit[i][j]:
            a, b = bfs(i, j)
            if a:
                if b == 1:
                    ans[0] += a
                elif b == 2:
                    ans[1] += a
print(*ans)