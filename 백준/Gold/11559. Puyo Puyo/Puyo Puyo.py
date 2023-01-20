import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def change(*kwargs):
    a, b, c, d = kwargs
    temp = maps[a][b]
    maps[a][b] = maps[c][d]
    maps[c][d] = temp

def bfs(*kwargs):
    visit = [[False] * 6 for _ in range(12)]

    a, b = kwargs
    queue = deque()
    queue.append((a, b))
    temp.append((a, b))
    visit[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6 and maps[nx][ny] == maps[a][b] and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny))
                temp.append((nx, ny))
def down():
    for y in range(5, -1, -1):
        for x in range(10, -1, -1):
            for x1 in range(11, x, -1):
                if maps[x1][y] == "." and not maps[x][y] == ".":
                    change(x1, y, x, y)
                    break

maps = [list(input().rstrip()) for _ in range(12)]

a = [i for i in range(11, 0, -1)]

ans = 0
while True:
    check = 0
    for i in range(12):
        for j in range(6):
            if not maps[i][j] == ".":
                temp = []
                bfs(i, j)
                if len(temp) >= 4:
                    check = 1
                    for x, y in temp:
                        maps[x][y] = "."
    if not check:
        break
    ans += 1
    down()
print(ans)