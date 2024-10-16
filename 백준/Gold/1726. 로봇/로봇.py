import sys
from collections import deque

input = sys.stdin.readline

dir = {
    0: (0, 1),
    1: (0, -1),
    2: (1, 0),
    3: (-1, 0)
}
tur = {
    0: (2, 3),
    1: (2, 3),
    2: (0, 1),
    3: (0, 1)
}

def read_input():
    return list(map(int, input().split()))

def read_position():
    return tuple(map(lambda x: x - 1, read_input()))

def find_exit():
    visit = [[[-1] * 4 for _ in range(n)] for _ in range(m)]
    visit[sx][sy][sd] = 0

    queue = deque([(sx, sy, sd)])

    while queue:
        x, y, d = queue.popleft()

        if (x, y, d) == (ex, ey, ed):
            return visit[x][y][d]

        for k in range(1, 4):
            nx = x + dir[d][0] * k
            ny = y + dir[d][1] * k
            
            if not (0 <= nx < m and 0 <= ny < n) or arr[nx][ny] == 1:
                break

            if visit[nx][ny][d] == -1:
                visit[nx][ny][d] = visit[x][y][d] + 1
                queue.append((nx, ny, d))

        for nd in tur[d]:
            if visit[x][y][nd] == -1:
                visit[x][y][nd] = visit[x][y][d] + 1
                queue.append((x, y, nd))

    return -1

m, n = read_input()
arr = [read_input() for _ in range(m)]

sx, sy, sd = read_position()
ex, ey, ed = read_position()


print(find_exit())