import sys
from collections import deque

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def input():
    return sys.stdin.readline().rstrip()

def within_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def initialize():
    arr = []
    queue = deque()
    h, w = map(int, input().split())
    visit = [[0] * w for _ in range(h)]
    
    for i in range(h):
        temp = list(input())
        for j in range(w):
            if temp[j] == ".":
                temp[j] = 0
                queue.append((i, j))
            else:
                temp[j] = int(temp[j])
        arr.append(temp)
    
    return h, w, arr, queue, visit

def bfs(h, w, arr, queue, visit):
    result = 0
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if not within_bounds(nx, ny, h, w):
                continue
            if not arr[nx][ny]:
                continue
            arr[nx][ny] -= 1
            if not arr[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                result = max(result, visit[nx][ny])
                queue.append((nx, ny))
    return result

print(bfs(*initialize()))
