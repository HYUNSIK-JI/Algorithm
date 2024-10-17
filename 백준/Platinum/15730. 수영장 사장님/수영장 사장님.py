import sys
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def input():
    return sys.stdin.readline().rstrip()

def is_within_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def fill_water(n, m, arr):
    visit = [[False] * m for _ in range(n)]
    pq = []
    
    for i in range(n):
        for j in range(m):
            if not i or i == n - 1 or not j or j == m - 1:
                heapq.heappush(pq, (arr[i][j], i, j))
                visit[i][j] = True
    
    total_water = 0
    while pq:
        h, x, y = heapq.heappop(pq)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_within_bounds(nx, ny, n, m):
                continue

            if visit[nx][ny]:
                continue
            
            visit[nx][ny] = True
                
            # 현재 위치보다 낮은 지대에 물을 채움
            if arr[nx][ny] < h:
                total_water += h - arr[nx][ny]
                heapq.heappush(pq, (h, nx, ny))
            else:
                heapq.heappush(pq, (arr[nx][ny], nx, ny))
    
    return total_water

# 입력 처리
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

print(fill_water(n, m, arr))