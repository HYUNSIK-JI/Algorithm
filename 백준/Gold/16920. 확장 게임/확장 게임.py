import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def input():
    return sys.stdin.readline().rstrip()

def within_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def bfs(snum, dis):
    new_init = deque()
    
    while init_player_start[snum]:
        x, y, dist = init_player_start[snum].popleft()
        
        if dist == dis:
            new_init.append((x, y, 0))
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if within_bounds(nx, ny, n, m) and arr[nx][ny] == "." and not visit[nx][ny]:
                visit[nx][ny] = True
                arr[nx][ny] = snum
                init_player_start[snum].append((nx, ny, dist + 1))
                result[int(snum)] += 1
                
    return new_init

n, m, p = map(int, input().split())
ps = [0] + list(map(int, input().split()))
result = [0] * (p + 1)

init_player_start = {str(i): deque() for i in range(1, p + 1)}
arr = []
visit = [[False] * m for _ in range(n)]

for i in range(n):
    row = list(input())
    for j in range(m):
        if row[j].isdigit():
            init_player_start[row[j]].append((i, j, 0))
            visit[i][j] = True
            result[int(row[j])] += 1
    arr.append(row)


while any(init_player_start[str(i)] for i in range(1, p + 1)):
    for i in range(1, p + 1):
        if init_player_start[str(i)]:
            new_init = bfs(str(i), ps[i])
            init_player_start[str(i)] = new_init
print(*result[1:])