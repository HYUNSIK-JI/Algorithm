import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, -1, 1, 0]
dy = [1, -1, 0, 0, 1, -1, 1, -1, 0]

def bfs(a, b):
    visit = [[False] * 8 for _ in range(8)]

    queue = deque()
    queue.append((a, b))

    global walls
    global ans

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x, y) in walls:
                continue
            if x == 0 and y == 7:
                ans = 1
                break
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 8 and 0 <= ny < 8 and not visit[nx][ny] and not (nx, ny) in walls:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
        next = []
        if walls:
            visit = [[False] * 8 for _ in range(8)]
        while walls:
            x, y = walls.pop()
            if 0 <= x + 1 < 8:
                next.append((x + 1, y))
        walls = next

maps = []
walls = []
ans = 0
for i in range(8):
    row = list(map(str, input().rstrip()))
    for j in range(8):
        if row[j] == "#":
            walls.append((i, j))
    maps.append(row)

bfs(7, 0)
print(ans)