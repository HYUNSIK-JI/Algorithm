import sys
from collections import deque
from itertools import permutations

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

inf = int(1e9)

def input():
    return sys.stdin.readline().rstrip()

# 특정 지점에서 BFS로 다른 모든 지점까지의 최단 거리를 계산하는 함수
def bfs(a, b):
    dist = [[-1] * m for _ in range(n)]
    dist[a][b] = 0
    queue = deque([(a, b)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if dist[nx][ny] != -1:
                continue
            if arr[nx][ny] == "X":
                continue
            
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))
    
    return dist

# 지점 간의 거리 계산
def calculate_distances():
    distances = [[inf] * len(points) for _ in range(len(points))]
    
    for i, (x1, y1) in enumerate(points):
        dist = bfs(x1, y1)
        for j, (x2, y2) in enumerate(points):
            if dist[x2][y2] != -1:
                distances[i][j] = dist[x2][y2]
    
    return distances

# 재귀적으로 모든 순회 경로를 탐색
def find_min_path(distances):
    min_path = inf
    
    for perm in permutations(range(1, len(points)), 5):  # S를 제외한 5개의 지점을 선택
        current_path_length = distances[0][perm[0]]  # S에서 첫 지점으로 가는 거리
        
        for i in range(4):
            current_path_length += distances[perm[i]][perm[i + 1]]  # 다음 지점으로 가는 거리
        
        min_path = min(min_path, current_path_length)
    
    return min_path

n, m = map(int, input().split())
sx, sy = 0, 0
points = []
arr = []

# 입력 처리 및 'S'와 'K' 지점 수집
for i in range(n):
    temp = list(input())
    for j in range(m):
        if temp[j] == 'K':
            points.append((i, j))  # 식당 위치 저장
        elif temp[j] == 'S':
            sx, sy = i, j  # 시작 지점 저장
            points.insert(0, (sx, sy))  # 시작 지점을 첫 번째로 추가
    arr.append(temp)

# 지점 간 최단 거리 계산
distances = calculate_distances()

# 가능한 경로 중 최소 거리 계산
min_time = find_min_path(distances)

# 결과 출력
print(min_time if min_time != inf else -1)
