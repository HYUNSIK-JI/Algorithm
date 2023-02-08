import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, t):
    visit[a][b] = True


    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        if t == "-":
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and maps[nx][ny] == t:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
        else:
            for i in range(2, 4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and maps[nx][ny] == t:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
n, m = map(int, input().split())
maps = [list(map(str, input().rstrip())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            bfs(i, j, maps[i][j])
            ans += 1
print(ans)