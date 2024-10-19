import sys
from collections import deque

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def input():
    return sys.stdin.readline().rstrip()

def within_bounds(x, y, n):
    return 0 <= x < n and 0 <= y < n

def bfs(altitude, n, start, min_h, max_h):
    queue = deque([start])
    visit = [[False] * n for _ in range(n)]
    visit[start[0]][start[1]] = True
    count = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not within_bounds(nx, ny, n):
                continue

            if visit[nx][ny]:
                continue

            if min_h <= altitude[nx][ny] <= max_h:
                visit[nx][ny] = True
                queue.append((nx, ny))
                if village[nx][ny] == 'K':
                    count += 1
    
    return count == len(house)


n = int(input())
village = []
house = []

start = None

for i in range(n):
    row = list(input())
    village.append(row)
    for j in range(n):
        if row[j] == 'P':
            start = (i, j)
        elif row[j] == 'K':
            house.append((i, j))

altitude = [list(map(int, input().split())) for _ in range(n)]

altitude_list = sorted(set(sum(altitude, [])))

left, right = 0, 0
min_fatigue = int(1e9)

while right < len(altitude_list):
    min_h = altitude_list[left]
    max_h = altitude_list[right]
    
    if min_h <= altitude[start[0]][start[1]] <= max_h:
        if bfs(altitude, n, start, min_h, max_h):
            min_fatigue = min(min_fatigue, max_h - min_h)
            left += 1
        else:
            right += 1
    else:
        right += 1
    
    if left > right:
        right = left

print(min_fatigue)
