import sys; input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 파괴 함수
def destroy(k, v):
    if not k % 2:
        for i in range(C):
            if cave[R - v][i] == "x":
                cave[R - v][i] = "."
                break
    else:
        for i in range(C - 1, -1, -1):
            if cave[R - v][i] == "x":
                cave[R - v][i] = '.'
                break
    return cave

def find_cluster(cave):
    cluster = []
    queue = deque()
    visit = [[False] * C for _ in range(R)]

    for i in range(C):
        if cave[R - 1][i] == 'x':
            queue.append((R - 1, i))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny] and cave[nx][ny] == 'x':
                visit[nx][ny] = True
                queue.append((nx, ny))
    for i in range(R - 1, -1, -1):
        for j in range(C):
            if cave[i][j] == 'x' and not visit[i][j]:
                cluster.append([i, j])
    return cluster, 1 if cluster else 0, visit

def move_cluster(cave, cluster, visit):
    _min = R

    for x, y in cluster:
        down = 0
        for i in range(x + 1, R):
            if cave[i][y] == '.':
                down += 1
            elif cave[i][y] == 'x' and visit[i][y]:
                break
        _min = min(_min, down)
    for x, y in cluster:
        cave[x][y] = '.'
        cave[x +_min][y] = 'x'
    return cave

R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
h = list(map(int, input().split()))

for k, v in enumerate(h):
    cave = destroy(k, v)
    cluster, check, visit = find_cluster(cave)
    if check:
        move_cluster(cave, cluster, visit)

for row in cave: print(''.join(row))