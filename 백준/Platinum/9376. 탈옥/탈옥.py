import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def input():
    return sys.stdin.readline().rstrip()

def within_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def bfs(sx, sy):
    visit = [[-1] * (w + 2) for _ in range(h + 2)]
    visit[sx][sy] = 0

    queue = deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not within_bounds(nx, ny, h + 2, w + 2):
                continue
            if visit[nx][ny] != -1:
                continue
            if arr[nx][ny] == "*":
                continue

            if arr[nx][ny] == ".":
                visit[nx][ny] = visit[x][y]
                queue.appendleft((nx, ny))
            elif arr[nx][ny] == "#":
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))

    return visit

def find_result(v1, v2, v3):
    result = int(1e9)
    for i in range(h + 2):
        for j in range(w + 2):
            if v1[i][j] != -1 and v2[i][j] != -1 and v3[i][j] != -1:
                c = v1[i][j] + v2[i][j] + v3[i][j]

                if arr[i][j] == "#":
                    c -= 2
                result = min(result, c)
    
    return result

for _ in range(int(input())):
    h, w = map(int, input().split())
    x1, y1, x2, y2 = 0, 0, 0, 0
    arr = [list("." * (w + 2))]

    for i in range(1, h + 1):
        temp = list('.' + input() + '.')
        arr.append(temp)
        for j in range(w + 2):
            if temp[j] == "$":
                if (x1, y1) == (0, 0):
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
                temp[j] = "."
    
    arr.append(list("." * (w + 2)))
    
    sang = bfs(0, 0)
    first = bfs(x1, y1)
    second = bfs(x2, y2)

    print(find_result(sang, first, second))