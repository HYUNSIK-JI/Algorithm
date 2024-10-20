import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def input():
    return sys.stdin.readline().rstrip()

def within_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def update_diamond(x, y, r):
    for i in range(r + 1):
        for dx, dy in [(-i, r - i), (-i, -(r - i)), (i, r - i), (i, -(r - i))]:
            nx, ny = x + dx, y + dy
            if within_bounds(nx, ny, n, m):
                arr[nx][ny] = 1
    

def bfs():
    visit = [[-1] * m for _ in range(n)]
    visit[0][0] = 0
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return True, visit
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not within_bounds(nx, ny, n, m) or arr[nx][ny] or visit[nx][ny] != -1:
                continue
            
            visit[nx][ny] = visit[x][y] + 1
            queue.append((nx, ny))
    
    return False, visit


n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    update_diamond(a - 1, b - 1, c)

result, visit = bfs()

if not result:
    print("NO")
else:
    print("YES")
    print(visit[n - 1][m - 1])
