import sys
import copy

input = sys.stdin.readline
 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, maps2):
    if maps2[x][y] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not maps2[nx][ny]:
                maps2[nx][ny] = 2
                dfs(nx, ny, maps2)
def wall(start, cnt):
    global mx_safe
    if cnt == 3:
        maps2 = copy.deepcopy(maps)
        for i in range(len(v)):
            r = v[i][0]
            c = v[i][1]
            dfs(r, c, maps2)
        area = sum(i.count(0) for i in maps2) # 안전지대 계산
        mx_safe = max(mx_safe, area) # 안전지대 가장 넓은 곳을 찾기위한 비교
    else:
        for i in range(start, n * m): # 맵전체를 벽 3개로 돌리기 위한 반복문
            r = i // m
            c = i % m
            if not maps[r][c]: # 빈칸이라면
                maps[r][c] = 1 # 벽을 세우고
                wall(start, cnt + 1) # 벽을 세운것으로 측정
                maps[r][c] = 0 # 벽을 다시 허문다.
n, m = map(int, input().split()) # 세로, 가로
maps = [] # 맵
v = [] #바이러스 위치
mx_safe = 0 # 안전지대
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        if a[j] == 2:
            v.append((i, j)) # 바이러스 위치
    maps.append(a)

wall(0, 0) # 브루트포스를 위해서 0, 0부터 시작
print(mx_safe)
