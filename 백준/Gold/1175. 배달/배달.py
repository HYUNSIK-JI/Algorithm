import sys
from collections import deque

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def input():
    return sys.stdin.readline().rstrip()

def find_delivery(start, points):
    sx, sy = start
    visit = [[[[False] * 4 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    queue = deque()
    
    for d in range(4):
        visit[sx][sy][d][0] = True
        queue.append((sx, sy, d, 0, 0))

    while queue:
        x, y, d, mask, time = queue.popleft()

        if (x, y) in points:
            point_index = points.index((x, y))
            mask |= (1 << point_index)

            if mask == (1 << len(points)) - 1:
                return time

        for nd in range(4):
            if nd == d:
                continue

            k = dir[nd]
            nx = x + k[0]
            ny = y + k[1]

            if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == "#":
                continue

            if visit[nx][ny][nd][mask]:
                continue

            visit[nx][ny][nd][mask] = True
            queue.append((nx, ny, nd, mask, time + 1))
    
    return -1

n, m = map(int, input().split())
start = None
points = []
arr = []

for i in range(n):
    temp = list(input().rstrip())
    for j in range(m):
        if temp[j] == "S":
            start = (i, j)
        elif temp[j] == "C":
            points.append((i, j))
    arr.append(temp)


print(find_delivery(start, points))
